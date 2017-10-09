#!/usr/bin/env python
import os
import os.path
import sys
import glob
def getalltxtfilename2(path): 
    txtfilenames=[] 
    for dirpath,dirnames,filenames in os.walk(path): 
        filenames=filter(lambda filename:filename[-3:]=='.py',filenames) 
        filenames=map(lambda filename:os.path.join(dirpath,filename),filenames) 
        txtfilenames.extend(filenames)
        #print filenames
    return txtfilenames
   
  
    
if __name__ == "__main__" :
 try :
    filenames=getalltxtfilename2("/home/chml/python/")
    for filename in filenames:
        print filename
 except :
  print "execute list_file_dir fun error"

