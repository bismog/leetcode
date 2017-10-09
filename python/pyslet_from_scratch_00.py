#!/usr/bin/env python

from pyslet.odata2.client import Client  
 
class index(object):  
    def GET(self):  
        #c=Client("http://services.odata.org/V2/Northwind/Northwind.svc/")  
        import pdb;pdb.set_trace()
        #c=Client("http://localhost:13579/demo.svc/users?$top=3")  
        c=Client("http://localhost:8080/odata.svc/")  
        products=c.feeds['Pet'].OpenCollection()  
        productNames = []  
        for k,p in products.iteritems():  
            productNames.append(p['ProductName'].value)  
            web.header('Content-Type', 'text/html')  
            return render_template('index.html', products = productNames)  

if __name__ == '__main__':
    xxx = index()
    zzz = xxx.GET()
