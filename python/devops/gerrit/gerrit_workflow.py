#!/usr/bin/env python
#-*- coding:utf-8 -*-

import subprocess
import json
from optparse import OptionParser, OptionGroup

EXCLUDED_CHANGE=[]

# Not include QA for QA may has many issue state as 'to-be-verified' to 
# manage, it would be a large of noise
team_member = [
    '@companyxxx.com.cn', 
    '@companyxxx.com.cn', 
    '@companyxxx.com.cn', 
    '@companyxxx.com.cn',
    '@companyxxx.com.cn',
    '@companyxxx.com.cn',
    '@companyxxx.com.cn',
    '@companyxxx.com.cn',
    '@companyxxx.com.cn'
]

def get_owner(review):
    if not review:
        print "None content review"
    return review.get('owner', {}).get('email', None)

def is_team_review(review):
    member = get_owner(review[0])
    return True if member in team_member else False

def get_review_workflow_state(review):
    submit_record = review.get("submitRecords", [])[0]
    submit_labels = submit_record.get("labels", [])
    review_state = {}
    for label in submit_labels:
        if label.get("label", "") == "Code-Review":
            review_state['code_review'] = label.get('status', '')
        elif label.get("label", "") == "Verified":
            review_state['verify'] = label.get('status', '')
        elif label.get("label", "") == "Workflow":
            review_state['workflow'] = label.get('status', '')
        else:
            print "Unknown label: ", label
    return review_state['workflow']

def get_review_code_review_state(review):
    all_approvals = review['currentPatchSet'].get('approvals', [])
    if not all_approvals:
        return []
    all_code_review_states = []
    for approval in all_approvals:
        if approval.get('type', "") == "Code-Review":
            all_code_review_states.append(approval.get('value', None))
    return all_code_review_states
    
def get_review_verified_state(review):
    # import pdb;pdb.set_trace()
    all_approvals = review['currentPatchSet'].get('approvals', [])
    if not all_approvals:
        return []
    all_verified_states = []
    for approval in all_approvals:
        if approval.get('type', "") == "Verified":
            all_verified_states.append(approval.get('value', None))
    return all_verified_states

def need_review(review):
    if review[0].get('number', '') in EXCLUDED_CHANGE:
        return False
    states = get_review_code_review_state(review[0])
    return False if '2' in states else True

def need_recheck(review):
    if review[0].get('number', '') in EXCLUDED_CHANGE:
        return False
    # No need to recheck if code-review scored '-1' or '-2'
    states = get_review_code_review_state(review[0])
    if '-1' in states or '-2' in states:
        return False
    states = get_review_verified_state(review[0])
    return False if '1' in states else True

def need_regate(review):
    if review[0].get('number', '') in EXCLUDED_CHANGE:
        return False
    if need_review(review) or need_recheck(review):
        return False
    workflow_state = get_review_workflow_state(review[0])
    return True if workflow_state == "OK" else False

def need_workflow(review):
    if review[0].get('number', '') in EXCLUDED_CHANGE:
        return False
    if need_review(review) or need_recheck(review):
        return False
    workflow_state = get_review_workflow_state(review[0])
    return True if workflow_state == "NEED" else False

def can_auto_workflow(review):
    branch = review[0].get('branch', '')
    if branch == 'upstreamfirst' or \
        branch == 'dev3.0':
        return True
    return False


class Gerrit(object):

    def __init__(self, option):
        self.review_list = []
        self.review_data = []
        self.redo = option.redo

    def get_review_list(self, members):
        owner_list = ['o:'+ow for ow in members]
        owner_syntax = ' OR '.join(owner_list)
        command_query = 'ssh workidxxx@gerrit.companyxxx.com.cn -p 29418 gerrit query ' + '\(' + owner_syntax + '\) ' + 'status:open'
        command_grep = 'grep number'
        query = subprocess.Popen(command_query.split(), stdout=subprocess.PIPE)
        grep = subprocess.Popen(command_grep.split(), stdin=query.stdout, stdout=subprocess.PIPE)
        out = grep.communicate()[0]
        out_lb = out.split('\n')
        for ol in out_lb:
            if not ol: continue
            self.review_list.append(ol.strip().split()[1])

    def trim_object(self, data_in):
        '''
           Replace '}\\n{' to '},{'
           Replace '\\x' to ''
           Insert [ and append ] around data string.
           Make data string can be consume in json.loads().
        '''
        data_out = data_in.replace('true', 'True')
        data_out = data_out.replace('false', 'False')
        data_out = data_out.replace('}\n{', '},{')
        data_out = data_out.replace('\n', '')
        data_out = '[' + data_out + ']'
        data_out = eval(data_out.decode('utf-8'))
        return data_out

    def review_detail(self, number):
        '''
        Assume review be something like following:
        {
            "branch": "upstreamfirst",
            "commitMessage": "Jira: projectxxx-1962... Change-Id: Iabe5fc389fbc032098452b9e5c82d10e98d468c9\n",
            "createdOn": 1496318601,
            "currentPatchSet": {
                "approvals": [
                    {
                        "by": {
                            "email": "jenkins_tfg@companyxxx.com.cn",
                            "name": "Jenkins_TFG",
                            "username": "jenkins_tfg"
                        },
                        "description": "Code-Review",
                        "grantedOn": 1496318607,
                        "type": "Code-Review",
                        "value": "1"
                    },
                    {
                        "by": {
                            "email": "zuul-ci@companyxxx.com.cn",
                            "name": "Niv Zuul CI",
                            "username": "zuul-ci"
                        },
                        "description": "Verified",
                        "grantedOn": 1496319531,
                        "type": "Verified",
                        "value": "-1"
                    },
                    {
                        "by": {
                            "email": "cheng.maolin@companyxxx.com.cn",
                            "name": "workidxxx",
                            "username": "workidxxx"
                        },
                        "description": "Code-Review",
                        "grantedOn": 1496388308,
                        "type": "Code-Review",
                        "value": "2"
                    }
                ],
                "author": {
                    "email": "zhao.shanshan3@companyxxx.com.cn",
                    "name": "00168455",
                    "username": "00168455"
                },
                "createdOn": 1496318601,
                "isDraft": false,
                "kind": "REWORK",
                "number": "1",
                "parents": [
                    "b1cd2d0c64ecc3353063e6221ef713cc94f35d37"
                ],
                "ref": "refs/changes/63/258963/1",
                "revision": "080b27b396b0839fd0e2e99d19531c6df30868bd",
                "sizeDeletions": -25,
                "sizeInsertions": 24,
                "uploader": {
                    "email": "zhao.shanshan3@companyxxx.com.cn",
                    "name": "00168455",
                    "username": "00168455"
                }
            },
            "id": "Iabe5fc389fbc032098452b9e5c82d10e98d468c9",
            "lastUpdated": 1496470258,
            "number": "258963",
            "open": true,
            "owner": {
                "email": "zhao.shanshan3@companyxxx.com.cn",
                "name": "00168455",
                "username": "00168455"
            },
            "project": "project0xxx/projectxxx",
            "status": "NEW",
            "subject": "Jira: projectxxx-1962...",
            "submitRecords": [
                {
                    "labels": [
                        {
                            "by": {
                                "email": "cheng.maolin@companyxxx.com.cn",
                                "name": "workidxxx",
                                "username": "workidxxx"
                            },
                            "label": "Code-Review",
                            "status": "OK"
                        },
                        {
                            "label": "Verified",
                            "status": "NEED"
                        },
                        {
                            "label": "Workflow",
                            "status": "NEED"
                        }
                    ],
                    "status": "NOT_READY"
                }
            ],
            "url": "http://gerrit.companyxxx.com.cn/258963"
        }
        '''
        cmd_gerrit_query = ['ssh', 'workidxxx@gerrit.companyxxx.com.cn', '-p', '29418', 'gerrit', 'query', '--format', 'json', '--current-patch-set', '--submit-records', str(number)]
        p = subprocess.Popen(cmd_gerrit_query, stdout=subprocess.PIPE)
        out = p.communicate()
        out = self.trim_object(out[0])
        self.review_data.append(out)

    def reviews_detail(self):
        ''' Get details of each review, and output a list of objects.
        '''
        reviews_detail = []
        for review in self.review_list:
            self.review_detail(review)

    def get_commit_hash(self, review, short=True):
        current_patch_set = review.get('currentPatchSet', {})
        commit = current_patch_set.get('revision', None)
        return commit[:7] if short else commit
        
    def get_project(self, review):
        return review.get('project')

    def get_branch(self, review):
        return review.get('branch')

    def get_change_info(self, review, short=True):
        c_info = {
            'change': '',
            'project': '',
            'branch': '',
            'commit': ''
        }
        current_patch_set = review.get('currentPatchSet', {})
        commit = current_patch_set.get('revision', None)
        c_info['commit'] =  commit[:7] if short else commit
        c_info['change'] = review.get('number', '')
        c_info['project'] = review.get('project', '').split('/')[1]
        c_info['branch'] = review.get('branch', '')
        return c_info
        
    def review(self, review):
        '''
             gerrit review --code-review +2 ${change,patchset}
             gerrit review --code-review +2 $commit_id
        '''
        ci = self.get_change_info(review)
        cmd_recheck = ['ssh', 'workidxxx@gerrit.companyxxx.com.cn', '-p', '29418', 'gerrit', 'review', '--code-review', '+2', str(ci['commit'])]
        p = subprocess.Popen(cmd_recheck, stdout=subprocess.PIPE)
        p.communicate()
        print "%s(%s: %s) reviewed." % (ci['change'], ci['project'], ci['commit'])

    def recheck(self, review):
        '''
            gerrit review -m "recheck\ niv" ${change,patchset}
            gerrit review -m "recheck\ niv" $commit_id
        '''
        ci = self.get_change_info(review)
        cmd_recheck = ['ssh', 'workidxxx@gerrit.companyxxx.com.cn', '-p', '29418', 'gerrit', 'review', '-m', '"recheck\ niv"', str(ci['commit'])]
        p = subprocess.Popen(cmd_recheck, stdout=subprocess.PIPE)
        p.communicate()
        print "%s(%s: %s) rechecked." % (ci['change'], ci['project'], ci['commit'])

    def regate(self, review):
        '''
            gerrit review -m "regate\ niv" ${change,patchset} or 
            gerrit review -m "regate\ niv" $commit
        '''
        ci = self.get_change_info(review)
        cmd_regate = ['ssh', 'workidxxx@gerrit.companyxxx.com.cn', '-p', '29418', 'gerrit', 'review', '-m', '"regate\ niv"', str(ci['commit'])]
        p = subprocess.Popen(cmd_regate, stdout=subprocess.PIPE)
        p.communicate()
        print "%s(%s: %s) regated." % (ci['change'], ci['project'], ci['commit'])

    def workflow(self, review):
        ''' 
            gerrit review --workflow +1 ${change,patchset} or
            gerrit review --workflow +1 $commit_id
        '''
        ci = self.get_change_info(review)
        cmd_workflow = ['ssh', 'workidxxx@gerrit.companyxxx.com.cn', '-p', '29418', 'gerrit', 'review', '--workflow', '+1', str(ci['commit'])]
        p = subprocess.Popen(cmd_workflow, stdout=subprocess.PIPE)
        p.communicate()
        print "%s(%s: %s) workflow+1." % (ci['change'], ci['project'], ci['commit'])

def parse_option():
    parser = OptionParser(description="Make query to gerrit")
    group = OptionGroup(parser, "Debug Options")
    group.add_option("-x", "--redo", dest="redo", action="store_true",
                     help="Redo workflow, such as recheck, regate, workflow+1, etc.")
    parser.add_option_group(group)
    (options, args) = parser.parse_args()
    return options


def main():
    op = parse_option()
    gerrit = Gerrit(op)
    gerrit.get_review_list(team_member)
    gerrit.reviews_detail()
    # Here is_team_review can also a method from class, a example:
    # https://stackoverflow.com/questions/7750982/can-pythons-map-function-call-object-member-functions
    team_reviews = filter(is_team_review, gerrit.review_data)

    # For each review, gerrit query and render code-reviewer points, CI points, 
    # Command line tool 'gerrit query/review' cann't check out code-review scores 
    # and CI scores. So refer to https://stackoverflow.com/questions/34899239/
    # query-gerrit-using-rest-apis, RESTful API may be better choice.
    # Give up of RESTful API for there was no "POST" method available.
    reviews_need_review = filter(need_review, team_reviews)
    for review_need_review in reviews_need_review:
        ci = gerrit.get_change_info(review_need_review[0])
        print "%s(%s: %s) needs review." % (ci['change'], ci['project'], ci['commit'])
        # gerrit.review(review_need_review[0])
    
    # Recheck those failed to verify
    reviews_need_recheck = filter(need_recheck, team_reviews)
    for review_need_recheck in reviews_need_recheck:
        ci = gerrit.get_change_info(review_need_recheck[0])
        print "%s(%s: %s) needs recheck." % (ci['change'], ci['project'], ci['commit'])
        if gerrit.redo:
            gerrit.recheck(review_need_recheck[0])

    # Workflow +1 if all set
    reviews_need_workflow = filter(need_workflow, team_reviews)
    for review_need_workflow in reviews_need_workflow:
        ci = gerrit.get_change_info(review_need_workflow[0])
        print "%s(%s: %s) needs workflow." % (ci['change'], ci['project'], ci['commit'])
    reviews_can_auto_workflow = filter(can_auto_workflow, reviews_need_workflow)
    for review_can_auto_workflow in reviews_can_auto_workflow:
        ci = gerrit.get_change_info(review_can_auto_workflow[0])
        print "%s(%s: %s) can auto workflow." % (ci['change'], ci['project'], ci['commit'])
        if gerrit.redo:
            gerrit.workflow(review_can_auto_workflow[0])

    # Regate those failed to workflow+1
    reviews_need_regate = filter(need_regate, team_reviews)
    for review_need_regate in reviews_need_regate:
        ci = gerrit.get_change_info(review_need_regate[0])
        print "%s(%s: %s) needs regate." % (ci['change'], ci['project'], ci['commit'])
        if gerrit.redo:
            gerrit.regate(review_need_regate[0])

if __name__  == "__main__":
    main()
