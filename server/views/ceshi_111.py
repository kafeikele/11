# -*- coding: utf-8 -*-
import paramiko
import MySQLdb
# from django.template import Template ,Context
# from django.http import HttpResponse
from django.db import connection


# rom models import student

def index(req, template_name):
    from django.shortcuts import render_to_response
    f = file('E:\\code\\pt_mon\\pt_mon\\server\\views\\ip.txt', 'r')
    cs_111 = []

    for line in f.readlines():
        line = line.strip('\n')
        hostname = line
        port = 22
        username = 'root'
        password = 'putao123'
        Known_host = "C:\\Users\\Administrator\\.ssh\\known_hosts"
        paramiko.util.log_to_file('paramiko.log')
        s = paramiko.SSHClient()
        s.load_system_host_keys(Known_host)
        s.connect(hostname, port, username, password)
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        stdin, stdout, stderr = s.exec_command('ps aux |grep -E "java|nginx|uwsgi" |grep -v grep')

        a = stdout.read()
        lists = a.split('\n')

        cs_111.append(line)
        for i in lists:
            i = i.split(' ')

            def not_empty(i):
                return i and i.strip()

            ret = filter(not_empty, i)
            if len(ret) < 10: continue
            c = [ret[0], ret[1], ret[10], ret[11]]
            try:
                cursor = connection.cursor()
                sql = "INSERT INTO student (NAME,classes,age) VALUES( 'wxh', '3 year 2 class', '2')"
                cursor.execute(sql)
                connection.commit()
                cursor.close()
                connection.close()
            except Exception as e:
                print e

            cs_111.append(c)
    print cs_111
    return render_to_response('test.html', {'cs_111': cs_111})
    # return render_to_response('test.html',{'cs_111':cs_111})
    # return HttpResponse(c)


'''
        cursor = connections.cursor
        sql = "INSERT INTO student values( 'tom', '3 year 2 class', '2')"
        cursor.execute(sql)
        connections.commit()
        cursor.close()
        connections.close()
'''
