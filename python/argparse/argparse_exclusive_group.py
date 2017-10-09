import argparse

parser = argparse.ArgumentParser()

#group = parser.add_mutually_exclusive_group(required=True)
#group.add_argument('a', action='store_true')
#group.add_argument('b', action="store_true")
# parser.add_argument('mode', choices=['limit', 'uuid'])
# parser.add_argument('limit_id', nargs='?')

# parser.add_argument('--start', action='store_true', help='start')
# parser.add_argument('--stop', action='store_true', help='stop')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--start', action='store_true', help='start')
group.add_argument('--stop', action='store_true', help='stop')
group.add_argument('--status', action='store_true', help='status')
parser.add_argument('--xxx', action='store_true', help='fuck GFW')

print parser.parse_args()
