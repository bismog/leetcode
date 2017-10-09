from BeautifulSoup import BeautifulSoup
doc = ['<html><head><title>PythonClub.org</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b> of ptyhonclub.org.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b> of pythonclub.org.',
       '</html>']
soup = BeautifulSoup(''.join(doc))
