# from configparser import ConfigParser
# parser = ConfigParser()
# parser.read('database.config')
# print(parser.get('database_config', 'url'))
#
#
#
# import sys
# if sys.version_info[0] >= 3:
#     import urllib2 as compat_urllib_request
#     print("python 2 version")
# else:
#     import urllib.request as compat_urllib_request
#     print("python 3 version")

def getConfigDict():
    try:
        import ConfigParser as cp
        print("python 2")
        print("test")
    except ImportError:
        import configparser as cp
        print("python 3")
    parser = cp.ConfigParser()
    parser.read('database.config')
    print(parser.get('database_config', 'url'))

getConfigDict()