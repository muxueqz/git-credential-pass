#!/usr/bin/env python2
import sys
import re
import os
import subprocess
import ConfigParser
config = ConfigParser.ConfigParser()
home_path = os.getenv('HOME')
config_path = os.path.join(home_path, '.config/git-credential-pass.ini')
config.read(config_path)

repo_info_regex = r'(\S+)=(.*)'
password_store_path = os.path.join(home_path, '.password-store')

operation = sys.argv[1]
if operation != "get":
    sys.exit(1)


repo_info_string = sys.stdin.read()
repo_info = dict(re.findall(repo_info_regex, repo_info_string))

if 'host' not in repo_info:
    sys.stderr.write("Host not set\n")
    sys.exit(1)

if operation == "get":

    find_path = None
    try:
        find_path = config.get(repo_info['host'], 'target')
    except:
        pass
    if not find_path:
        cmd = '''
        find {0} -name "*.gpg" | grep {1}| head -n1 | sed 's/.gpg$//g'
        '''.format(password_store_path, repo_info['host'])
        _find_path = subprocess.check_output(
            cmd,
            shell=True
        )
        find_path = _find_path.replace(password_store_path, '').strip('\n')

    client = subprocess.check_output(
        [
        'pass',
        'show',
        find_path,
        ]
    )
    extractor = client.split('\n')
    repo_logins = {}
    repo_logins['login'] = ': '.join(extractor[1].split(': ')[1:])
    repo_logins['password'] = extractor[0]

    if repo_logins:
        print("username=%s" % repo_logins['login'])
        print("password=%s" % repo_logins['password'])
    else:
        sys.stderr.write("Couldn't find credentials for host\n")
        sys.exit(1)
