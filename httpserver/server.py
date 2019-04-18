#!/usr/bin/python
# encoding=utf-8

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # print 'get'+self.path[1:]
            # print 'index'.find(self.path[1:])
            if self.path[1:].find('index') < 0:
                print 'index'
                self.send_response(404)
            else:
                print 'else'
                f = open(self.path[1:], 'r')  # 获取客户端输入的页面文件名称
                self.send_response(200)  # 如果正确返回200
                self.send_header('Content-type', 'text/html')  # 定义下处理的文件的类型
                self.end_headers()  # 结束处理
                self.wfile.write(f.read())  # 通过wfile将下载的页面传给客户
                f.close()  # 关闭

        except IOError:
            self.send_error(404, 'file not found: %s' % self.path)


class CustomHTTPServer(ThreadingMixIn, HTTPServer):
    pass
    # def __init__(self, host, port):
    #     HTTPServer.__init__(self, (host, port), CustomHTTPRequestHandler)


def main():
    server = CustomHTTPServer(('172.31.76.85', 8000), CustomHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print e
