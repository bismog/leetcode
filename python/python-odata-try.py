
from odata import ODataService

#import pdb;pdb.set_trace()
url = 'http://services.odata.org/V4/Northwind/Northwind.svc/'
Service = ODataService(url, reflect_entities=True)
Supplier = Service.entities['Supplier']

query = Service.query(Supplier)
query = query.limit(2)
query = query.order_by(Supplier.CompanyName.asc())

for supplier in query:
    print('Company:', supplier.CompanyName)

    for product in supplier.Products:
        print('- Product:', product.ProductName)
