#!/usr/bin/env python
#-*- coding:utf-8 -*-

# (c) UbuntuChina, http://www.ubuntu.org.cn
# (c) free software, GPLv3
# Created by chml

import BaseHTTPServer,SocketServer, cgi
from os import curdir,sep, path, chmod

uploadhtml='''<html><body>
<p>上传RPM包到project0xxx版本服务器</p>
<form enctype="multipart/form-data" action="/" method="post" target="_blank">
<br />
<p>Project: 
<input type="radio" name="project" value="projectxxx" /> projectxxx
<input type="radio" name="project" value="project0xxx" checked /> project0xxx
</p>
<p>RPM files: <input type="file" name="files" multiple="" ></p>
<br />
<p><input type="submit" value="上传"></p>
</form>
'''

BASEDIR = '/var/www/html/repo/yum/'

class WebHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/':
           self.send_response(200)
           self.send_header('Content-Type','text/html; charset=utf-8')
           self.end_headers()
           self.wfile.write(uploadhtml)
           return
        try:
           f = open(curdir+sep+self.path)
           self.send_response(200)
           self.end_headers()
           self.wfile.write(f.read())
           f.close()
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def save(self, file_name, file_data):
        if path.exists(file_name):
           self.wfile.write('文件 <a href="%s">%s</a> 已经存在，忽略上传。<br/>' % (file_name,file_name))
        else:
           upfile=open(file_name,'w')
           upfile.write(file_data);
           upfile.close()
           file_len = len(file_data)
           del file_data
           chmod(file_name, 0755)
           self.wfile.write('文件 <a href="%s">%s</a> 成功上传，大小为：%d bytes<br/>' % (file_name,file_name,file_len))


    def do_POST(self):
        form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],})
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.end_headers()
        # self.wfile.write('客户端: %s<br/>' % str(self.client_address))
        try:
            # fields = form.keys()  # fields should be ['project', 'files']
            # 'form.getvalue()', quote from http://www.w3big.com/zh-TW/python/python-cgi.html
            projectxxx_or_project0xxx = form.getvalue('project')
            target_dir = BASEDIR + projectxxx_or_project0xxx
            field_items = form['files']
            # https://stackoverflow.com/questions/12240267/uploading-multiple-files-via-single-form-field-via-python-cgi
            if isinstance(field_items, list):
                for field_item in field_items:
                    if field_item.filename:
                        file_name=target_dir+sep+field_item.filename
                        file_data=field_item.file.read()
                        self.save(file_name, file_data)
            else:
                field_item = field_items
                if field_item.filename:
                    file_name=target_dir+sep+field_item.filename
                    file_data=field_item.file.read()
                    self.save(file_name, file_data)
        except Exception as e:
            self.wfile.write('<Html>上传失败，请重试。<br/><br/>');
        else:
            self.wfile.write('<Html>上传完毕。<br/><br/>');
        self.wfile.write('</html>')


class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer): pass

if __name__ == '__main__':
    server_address = ('0.0.0.0', 12345)
    httpd = ThreadingHTTPServer(server_address, WebHandler)
    print "Web Server On %s:%d" % server_address
    httpd.serve_forever()
