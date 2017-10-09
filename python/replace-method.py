import os

def get_replace_str():
    with open(os.path.join("/home/python/","file-to-be-replaced")) as fp:
        return fp.read() % "CONFIG_CONTROLLER_HOST = 10.20.30.40"


def main():
    data = get_replace_str()
    print 'data:' % data
