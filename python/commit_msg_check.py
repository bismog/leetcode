#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, commands, sys

__CASE_INSENSITIVE = True
reload(sys)
sys.setdefaultencoding( "utf-8" )

def input_parse(argv, jobinfo):
    ret = 0
    foundkey = ''
    paramlist = [ '--' + one for one in jobinfo.keys() ]
    #print argv
    for i in range(0,len(argv)):
        #print argv[i]
        if argv[i] in paramlist:
            foundkey = argv[i].replace('--','')
            continue
        else:
            if foundkey:
                jobinfo[foundkey] = argv[i]
                foundkey = ''
                continue
            else:
                print 'invalid argument, %s'%argv[i]
                ret = -1
                break
    
    for key in jobinfo.keys():
        if not jobinfo[key]:
            if os.environ.has_key(key):
                jobinfo[key] = os.environ[key]
            else:
                sys.stderr.write('%s was null\n'%key)
                return -1
    
    return ret
    
def __check_ec(jobinfo):
    # subject: GERRIT_CHANGE_SUBJECT
    subject = jobinfo['GERRIT_CHANGE_SUBJECT']
    if len(subject) > 12 and subject[0:12].isdigit() and subject[13:].strip() and subject[12] == ' ':
        return 0
    return -1

def __find_keyword(string, keyword):
    numstart = len(keyword)
    numend   = string.find(' ', numstart)
    if keyword[0] == '[':
        numend   = string.find(']', numstart)
    #print "%s,%s,%s,%s,%s,%s,%s"%(keyword,numstart,numend,string[numstart:numend],string[numend+1:],string[numend+1:].strip(),string[numstart:numstart+12])
    if numend > 0 and string[numstart:numend].isdigit() and string[numend+1:].strip():
        return 0
    return -1
    
def __check_refs(jobinfo, keywords):
    # subject: GERRIT_CHANGE_SUBJECT
    subject = jobinfo['GERRIT_CHANGE_SUBJECT'].lower() if __CASE_INSENSITIVE else jobinfo['GERRIT_CHANGE_SUBJECT']
    newstr = ''
    for one in keywords:
        one = one.lower() if __CASE_INSENSITIVE else one
        if subject.startswith(one):
            ret = __find_keyword(subject, one)
            if not ret:
               return ret

    #
    return -1

def __check(jobinfo):
    # [refs #12345] [Refs #xxxxx] [Feature #xxxxx] [Story #xxxxx]
    keywords = {'[EC':'614000123456',
                '[Refs #':'12345', 
                '[Feature #':'12345', '[Story #':'12345', 
                'Jira: projectxxx-':'345',
                'Revert "Jira: projectxxx-': '345',
                }
    # check ec
    #ret = __check_ec(jobinfo)
    #if not ret:
    #    return ret

    # check refs
    ret = __check_refs(jobinfo, keywords.keys())
    if not ret:
        return ret

    sys.stderr.write("error, Invalid format for subject\n\n")
    sys.stderr.write("Valid formats(case insensitive):\n")
    for one in sorted(keywords.keys()):
        tmp_msg = one + keywords[one]
        tmp_msg += ']' if one[0] == '[' else ' '
        tmp_msg += 'commit message\n'
        sys.stderr.write(tmp_msg)
    return ret
    
def __do_handle(argv,jobinfo):
    #print argv
    ret = input_parse(argv, jobinfo)
    if not ret:
        ret = __check(jobinfo)
    return ret    

def CommitMesgCheck(argv):
    jobinfo = {'GERRIT_CHANGE_SUBJECT':''}
    return __do_handle(argv, jobinfo)

if __name__ == '__main__':
    #jobinfo = {'GERRIT_CHANGE_SUBJECT':'', 'GERRIT_CHANGE_COMMIT_MESSAGE':''}
    jobinfo = {'GERRIT_CHANGE_SUBJECT':'Revert "Jira: projectxxx-506 Disable haproxy logging"'}
    ret = __do_handle(sys.argv[1:], jobinfo)
    sys.exit(ret)

