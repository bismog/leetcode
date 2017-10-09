import argparse 
parser = argparse.ArgumentParser()
parser.add_argument('--limit', nargs=3)
parser.add_argument('lmt', nargs='*', help='positional limitation')
#parser.add_argument('--pos', nargs=2)

print parser.parse_args()
