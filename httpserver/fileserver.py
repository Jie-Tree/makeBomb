#!/usr/bin/python
#encoding=utf-8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import shutil


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try: 
            q = self.path[2:]
            print q
            ql = q.split('&')
            print ql
            for ss in ql:
                if 'username' in ss:
                    username = ss.split('=')[1]
                if 'password' in ss:
                    password = ss.split('=')[1]
            print username, password
            bomb = MakeBomb(username, password)
            bomb.makebomb()
            # f=open(self.path[1:],'r') # 获取客户端输入的页面文件名称
            # self.send_response(200)#如果正确返回200
            # self.send_header('Content-type','text/html') #定义下处理的文件的类型
            # self.end_headers()#结束处理
            # self.wfile.write(f.read())#通过wfile将下载的页面传给客户
            # f.close() #关闭
            # f = open('904615562/bomb.c')
            f = open('../'+password+'/bombs/bomb0/bomb')
            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header("Content-disposition","attachment;filename=bomb")
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            os.system('cd .. ; rm -R '+password)
            print 'delete--------'

        except Exception, e:
            print e
            self.send_error(404, 'file not found: %s'%self.path)


class CustomHTTPServer(HTTPServer):
    def __init__(self, host, port):
        HTTPServer.__init__(self, (host, port), CustomHTTPRequestHandler)


def main():
    server = CustomHTTPServer('172.31.76.85', 8001)
    server.serve_forever()


class MakeBomb():
    def __init__(self, u, p):
        self.username = u
        self.password = p

    def makebomb(self):

        userfolder = '../'+self.password
        # folder = os.path.exists(userfolder)
        # if not folder:
        #     os.mkdir(self.password)
        # else:
        #     os.system('cd ..; rm -R '+self.password)
        #     print 'folder existed'

        os.system(
            'cd .. ; cp lab2 -R ' + self.password + ' ; cd ' + self.password
        )

        newstr = self.username+'('+self.password+')'

        userfile = userfolder+'/src/makephases.pl'

        lines = open(userfile).readlines()
        fp = open(userfile, 'w')
        for s in lines:
            fp.write(s.replace('username(password)', newstr))
        fp.close()

        os.system('cd ../'+self.password + ' ; ./makebomb.pl -s ./src -b ./bombs')


if __name__ == '__main__':
    # m = MakeBomb('ceshi-2', '904615562')
    # m.makebomb()
    try:
        main()
    except Exception as e:
        print e