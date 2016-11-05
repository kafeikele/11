#!/usr/bin/env python

import paramiko
f = file('C:\\project\\pt_mon\\server\\views\\ip.txt', 'r')
cs_111 = []
for line in f.readlines():
    line = line.strip('\n')

    hostname = line
    port     = 22
    username = 'root'
    password = 'Putao2015hw'
    Known_host = "C:\\Users\\Administrator\\.ssh\\known_hosts"

    if __name__ == "__main__":
        paramiko.util.log_to_file('paramiko.log')
        s = paramiko.SSHClient()
        s.load_system_host_keys(Known_host)
        s.connect(hostname, port, username, password)
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        stdin, stdout, stderr = s.exec_command('ps aux |grep -E "java|nginx|uwsgi" |grep -v grep')

        a = stdout.read()
        lists = a.split('\n')
        for i in lists:
            i = i.split(' ')
            def not_empty(i):
                return i and i.strip()
            ret = filter(not_empty, i)
            if len(ret) < 10: continue
            c = [ret[0], ret[1], ret[8], ret[10]]
            cs_111.append(line)
            cs_111.append(c)

print cs_111