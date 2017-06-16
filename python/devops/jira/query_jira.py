#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Create report from analysis based on defining a set of features
and policies for a set of stories.

Simeon Warner, 2015-09...
"""

import sys
import re
import urllib
import ConfigParser
# import xml.etree.ElementTree as ElementTree
import xml.etree.cElementTree as ElementTree
import json
from optparse import OptionParser, OptionGroup
import html2text
from datetime import datetime,date
import os
from pygments import highlight, lexers, formatters


# Global setup
PRIORITY_TO_VALUE = { 'Critical': 3, 'Major': 2, 'Low': 1 }
VALUE_TO_PRIORITY = dict((v, k) for k, v in PRIORITY_TO_VALUE.iteritems())
PRIORITIES = sorted(PRIORITY_TO_VALUE.keys(), key=lambda x: -PRIORITY_TO_VALUE[x]) #highest first

def html_to_tex(html):
    """Simple wrapper for html2txt with some options and tweak to make TeX."""
    h = html2text.HTML2Text()
    h.body_width = 0 #no wrapping
    txt = h.handle(html).encode('utf-8').strip()
    # Remove linebreaks
    txt = re.sub(r'[\r\n]', ' ', txt)
    # Deal with some TeX issues
    # http://tex.stackexchange.com/questions/34580/escape-character-in-latex
    txt = re.sub(r'([\&%$#_\{\}])', r'\\\g<1>', txt)
    # Replace markdown links with TeX hyperlinks
    txt = re.sub(r'\[[A-Z]+-\d+\]\([^\)]+/([A-Z]+-\d+)\)',
                 r'\\hyperlink{\g<1>}{\g<1>}',
                 txt)
    # Ditch any trailing period
    txt = re.sub(r'\s*\.\s*$', '', txt)
    return txt 


def issue_number(issue):
    """Return issue number extracted from issue['key']."""
    m = re.match(r'[A-Z]+\-(\d+)',issue['key'])
    return( int(m.group(1)) if (m) else 0 )


def key_number(key):
    """Return issue number extracted from key."""
    m = re.match(r'[A-Z]+\-(\d+)',key)
    return( int(m.group(1)) if (m) else 0 )



relation_translations = {
    'relates to': 'Is related to',
    'is related to': 'Is related to',
    'is relied upon by': 'Is relied upon by',
    'relies on': 'Relies on',
}


def parse_issue_links(el):
    """Parse issuelinks in etree element el

    Example XML:
    <issuelinks>
      <issuelinktype id="10061">
        <name>Relation</name>
        <outwardlinks description="relates to">
          <issuelink>
            <issuekey id="67236">IRS-203</issuekey>
          </issuelink>
        </outwardlinks>
      </issuelinktype>
      <issuelinktype id="10062">
        <name>Rely</name>
        <inwardlinks description="is relied upon by">
          <issuelink>
            <issuekey id="66269">IRS-111</issuekey>
          </issuelink>
          <issuelink>
            <issuekey id="66270">IRS-112</issuekey>
          </issuelink>
        </inwardlinks>
      </issuelinktype>
    </issuelinks>
    """
    links = {}
    if (el is None):
        return(links)
    for issuelinktype in el.findall('./issuelinktype'):
        for outwardlink in issuelinktype.findall('./outwardlinks'):
            linktype = outwardlink.attrib['description']
            if (linktype in relation_translations):
                linktype = relation_translations[linktype]
            else:
                raise Exception("Unexpected outward link: %s" % (linktype))
            for issuekey in outwardlink.findall('./issuelink/issuekey'):
                #print(issuekey.text)
                if (linktype not in links):
                    links[linktype]=[]
                links[linktype].append(issuekey.text)
        for inwardlink in issuelinktype.findall('./inwardlinks'):
            linktype = inwardlink.attrib['description']
            if (linktype in relation_translations):
                linktype = relation_translations[linktype]
            else:
                raise Exception("Unexpected inward link: %s" % (linktype))
            for issuekey in inwardlink.findall('./issuelink/issuekey'):
                #print(issuekey.text)
                if (linktype not in links):
                    links[linktype]=[]
                links[linktype].append(issuekey.text)
    return(links)


def parse_epic_link(el):
    """Extract key of epic this issue belongs to (if given), else ''.

    Example XML:
    <customfields>
      <customfield id="customfield_10730" key="com.pyxis.greenhopper.jira:gh-epic-link">
        <customfieldname>Epic Link</customfieldname>
        <customfieldvalues>
          <customfieldvalue>IRS-4</customfieldvalue>
        </customfieldvalues>
      </customfield>
      ...
    </customfields>
    """
    if (el is None):
        return('')
    for customfield in el.findall('./customfield'):
        if (customfield.attrib['id'] == "customfield_10730"):
            return(customfield.find('./customfieldvalues/customfieldvalue').text)
    return('')

def classify(tree, fields):
    """Separate results into features, policies and user_stories"""
    """
<rss version="0.92">
    <channel>
        <title>ZTE JIRA</title>
        <link>http://jira.zte.com.cn/issues/?jql=...</link>
        <description>An XML representation of a search request</description>
        <language>en-us</language>
        <issue start="0" end="7" total="7"/>
        <build-info>
            <version>7.1.2</version>
            <build-number>71006</build-number>
            <build-date>09-03-2016</build-date>
        </build-info>
<item>
    <link>http://jira.zte.com.cn/browse/DAISY-1985</link>
    <key id="96952">DAISY-1985</key>
    <summary>...</summary>
    <type id="10004" iconUrl="http://jira.zte.com.cn/secure/viewavatar?size=xsmall&amp;avatarId=10303&amp;avatarType=issuetype">Bug</type>
    <priority id="4" iconUrl="http://jira.zte.com.cn/images/icons/priorities/low.svg">Low</priority>
    <status id="10000" iconUrl="http://jira.zte.com.cn/" description="">To Do</status>
    <statusCategory id="2" key="new" colorName="blue-gray"/>
    <assignee username="00024906">&#38472;&#20122;&#29618;00024906</assignee>
</item>
<item>
    ...
</item>
    """
    bugs = []
    sub_tasks = []
    tasks = []
    epics = []
    root = tree.getroot()
    for item in root.findall('./channel/item'):
        args = {}
        for field in fields:
            el =item.find(field)
            # Fetch attrib 'username' to fill 'assignee'
            if field == 'assignee':
                # import pdb;pdb.set_trace()
                args[field] = el.attrib.get('username', None)
                continue
            if el is None:
                args[field] = 'fixme - missing %s' % (field)
            elif el.text is None:
                args[field] = None
            else:
                args[field] = el.text
        if args.get('summary', ''):
            args['summary'] = html_to_tex(args['summary'])
            if args.get('description', ''):
                args['description'] = html_to_tex(args['description'])
                if not re.search(r'[\?\!\.]$',args['description']):
                    args['description'] += '.'
            else: 
                args['description'] = ''
        # import pdb;pdb.set_trace()
        if (args['type'] == 'Bug'):
            bugs.append(args)
        elif (args['type'] == 'Sub-task'):
            sub_tasks.append(args)
        elif (args['type'] == 'Task'):
            tasks.append(args)
        elif (args['type'] == 'Epic'):
            epics.append(args)
        else:
            raise Exception("%s: Unexpected type %s" % (args['key'], args['type']))
    
    return (bugs, sub_tasks, tasks, epics)

    

def add_epic_names(issues, epics):
    """Add a field epic_name to each issue."""
    for issue in issues:
        if ('epic' in issue):
            epic_key = issue['epic']
            for epic in epics:
                if (epic['key'] == epic_key):
                    issue['epic_name'] = epic['summary']
                    issue['epic_ref'] = '\\hyperlink{%s}{%s}' % (issue['epic_name'],issue['epic_name'])
                    break
            if ('epic_name' not in issue):
                raise Exception("%s: Failed to find epic name for %s" % (issue['key'],epic_key))

def add_story_epics(issues, user_stories_by_key):
    """Add a field story_epics to each issue in issues base on the epics its stories rely on"""
    linktype = 'Is relied upon by'
    for issue in issues:
        epic_names = set()
        if (issue['issuelinks'] and linktype in issue['issuelinks']):
            keep = []
            for target in issue['issuelinks'][linktype]:
                if (target in user_stories_by_key):
                    story = user_stories_by_key[target]
                    epic_names.add(story['epic_name'])
                    keep.append(target)
                else:
                    print("Non-story %s linked from %s, link ignored" % (target,issue['key']))
            # replace with the list of keepers
            issue['issuelinks'][linktype] = keep
        issue['issuelinks']['User story groups'] = list(epic_names)


def add_related(issues):
    """Add related field built from issuelink."""
    for issue in issues:
        issue['related'] = ''
        if (issue['issuelinks']):
            for linktype in sorted(issue['issuelinks'].keys()):
                targets = []
                for target in sorted(issue['issuelinks'][linktype], key = key_number):
                    targets.append("\\hyperlink{%s}{%s}" % (target, target))
                issue['related'] += '\n'+linktype+': '+', '.join(targets)+'\n'


def get_issue(issues, target, msg="issues"):
    """Lookup issue based on the key.

    FIXME - This is mindblowingly inefficient! need lookup by key
    """
    for t in (issues):
        if (t['key'] == target):
            return(t)
    raise Exception("Cannot find %s in %s" % (target,msg))
    

def infer_feature_policy_priorities(user_stories, other, fp, modify=True):
    """Infer feature and policy priorities from user_story priorities

    The inferred feature or policy priority will be the highest of the priorities
    of the stories that rely upon it. For policies we also look through 
    the other issues which will be features and take the highest of these
    priorities. This implies that feature priorities must be inferred 
    before policy priorities.

    
    """
    for issue in fp:
        priority = None
        if ('Is relied upon by' in issue['issuelinks']):
            for target in issue['issuelinks']['Is relied upon by']:
                t = get_issue(user_stories + other, target)
                p = t['priority']
                if (priority is None or PRIORITY_TO_VALUE[p]>PRIORITY_TO_VALUE[priority]):
                    priority = p
        else:
            print("Issue %s is not relied upon by any issue" % (issue['key']))
        if (priority is None):
            print("No priority calculated for %s, treating as Low" % (issue['key']))
            priority = 'Low'
        elif (PRIORITY_TO_VALUE[issue['priority']]<PRIORITY_TO_VALUE[priority]):
            print("INCONSISTENCY: %s has priority %s, which is lower from inferred priority %s" % (issue['key'], issue['priority'], priority))
            if (modify):
                print("%s priority changed %s -> %s" % (issue['key'], issue['priority'], priority))
                issue['priority'] = priority
        elif (PRIORITY_TO_VALUE[issue['priority']]>PRIORITY_TO_VALUE[priority]):
            print("%s has priority %s, which is higher than inferred priority %s" % (issue['key'], issue['priority'], priority))
            

def check_story_priorities(features, policies, user_stories, modify=False):
    """Infer story priorities from feature and policy priorities as a sanity check.

    The story priority calculated will be the lowest of the priorities of the 
    features and policies it relies upon. An inconsistency warning will be shown
    if the actual story priority is higher than this, a simple note if it is 
    lower.

    If modify is true, then instead of showing a warning, the priority will be
    changed. This is a BACKWARDS process, it makes more sense
    to prioritize the user stories and then infer feature and policy 
    priorities from that. See infer_feature_policy_priorities().
    """
    for issue in user_stories:
        priority = None
        if ('Relies on' in issue['issuelinks']):
            for target in issue['issuelinks']['Relies on']:
                t = get_issue(features + policies, target)
                p = t['priority']
                if (p is None):
                    raise Exception("Cannot find %s in features or priorities" % (target))
                if (priority is None or PRIORITY_TO_VALUE[p]<PRIORITY_TO_VALUE[priority]):
                    priority = p
        else:
            print("Issue %s does not rely on any feature or policy" % (issue['key']))
        if (priority is None):
            print("No priority calculated for %s, treating as Low" % (issue['key']))
            priority = 'Low'
        elif (PRIORITY_TO_VALUE[issue['priority']]>PRIORITY_TO_VALUE[priority]):
            print("INCONSISTENCY: %s has priority %s, higher than inferred priority %s" % (issue['key'], issue['priority'], priority))
            if (modify):
                print("Setting %s to priority %s" % (issue['key'],priority))
                issue['priority'] = priority
        elif (PRIORITY_TO_VALUE[issue['priority']]<PRIORITY_TO_VALUE[priority]):
            print("%s has priority %s, lower than inferred priority %s" % (issue['key'], issue['priority'], priority))

class Jira(object):

    def __init__(self):
        self.filters = ['all_open', 'today', 'unassigned', 'p8b3', 'upstreamfirst']
        self.fields = [ 'key', 'type', 'summary', 'status', 'assignee', 'link', 'priority', 'updated']
        self.data = {}
        pass

    def config(self, conf):
        # Look in current dirs, user home, script install
        config = ConfigParser.RawConfigParser()
        for loc in os.curdir, os.path.expanduser("~"), os.path.dirname(__file__):
            try: 
                with open(os.path.join(loc, conf)) as source:
                    config.readfp( source )
                break #one success is enough
            except IOError:
                pass
        section = 'default'
        self.project = config.get(section,'project')
        self.username = config.get(section,'username')
        self.password = config.get(section,'password')
        self.baseuri = config.get(section,'baseuri')

        self.rules = {}
        for fl in self.filters:
            #as cut-paste from advanced search box in Jira
            self.rules[fl] = config.get('filter', fl) 
        

    def _query(self,rule,options=None):
        """ Extract from Jira 5.2.5 XML response:
        It is possible to restrict the fields that are returned in this document 
        by specifying the 'field' parameter in your request. For example, to 
        request only the issue key and summary add field=key&field=summary to 
        the URL of your request.
        For example:
        https://issues.library.cornell.edu/sr/jira.issueviews:searchrequest-xml/
        temp/SearchRequest.xml?jqlQuery=project+%3D+ARXIVDEV+AND+resolution+%3D+
        Unresolved+AND+fixVersion+%3D+%22Roadmap+%28Epics%29%22+ORDER+BY+priority+
        DESC&tempMax=1000&field=key&field=summary
        """
        params = [('jqlQuery', rule), ('tempMax', 1000)]
        if (self.username is not None or self.password is not None):
            params.append(('os_username', self.username))
            params.append(('os_password', self.password))
        for field in self.fields:
            params.append(('field', field))
            
        uri = "%s/sr/jira.issueviews:searchrequest-xml/temp/SearchRequest.xml?%s"\
            % (self.baseuri,urllib.urlencode(params))
        if (options.show_uri):
            print(uri)
            sys.exit(0)
        # import pdb;pdb.set_trace()
        f = urllib.urlopen(uri)
        if (options.show_xml):
            print(f.read())
            sys.exit(0)
        # return parsed etree
        return ElementTree.parse(f)

    def query(self, rule, options=None):
        return self._query(rule=rule, options=options)

    def query_all(self, options):
        """
        Get data from Jira
        """
        for rule_name,rule in self.rules.iteritems():
            # import pdb;pdb.set_trace()
            self.data[rule_name] = {}
            data = self.query(rule, options=options)
            # import pdb;pdb.set_trace()
            (bugs, sub_tasks, tasks, epics) = classify(data, self.fields)
            # import pdb;pdb.set_trace()
            self.data[rule_name]['bug'] = bugs
            self.data[rule_name]['subtask'] = sub_tasks
            self.data[rule_name]['task'] = tasks
            self.data[rule_name]['epic'] = epics
            
    def pretty_show(self, rule_name, type):
        # import pdb;pdb.set_trace()
        rule_data = self.data.get(rule_name, {})
        if rule_data:
            obj = rule_data.get(type, {})
        if obj:
            formatted_obj = json.dumps(obj, sort_keys=True, indent=4)
            colorful_json = highlight(unicode(formatted_obj, 'UTF-8'), 
                lexers.JsonLexer(), formatters.TerminalFormatter())
            print colorful_json


def parse_option():
    parser = OptionParser(description="Make query to Jira and format results as"
        "text message to stdout")
    group = OptionGroup(parser, "Debug Options")
    group.add_option("-u", "--show-uri", dest="show_uri", action="store_true",
                     help="show query URI and exit")
    group.add_option("-s", "--show-xml", dest="show_xml", action="store_true",
                     help="show XML response from Jira and exit")
    parser.add_option_group(group)
    (options, args) = parser.parse_args()
    return options


def main():
    """ 
    See https://confluence.atlassian.com/jira/
    displaying-search-results-in-xml-185729644.html
    """
    # Options
    op = parse_option()
    jira = Jira()
    jira.config('jira.conf')
    jira.query_all(op)
    # jira.pretty_show('all_open', 'bug')
    jira.pretty_show('all_open', 'subtask')

if __name__ == "__main__":
    main()
