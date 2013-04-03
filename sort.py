#!/usr/bin/python

import os
import sys
import getpass
import shutil

_user = getpass.getuser()

print "Enter type of OS \n1.Windows \n2.Linux "
num =int( raw_input())
if num is 1 :
	dir='C:/Users/'+_user+'/Downloads/'
else :
	dir="/home/"+_user+"/Downloads/"
print dir 
def sort(f_type):
  try:  
      dirname=f_type.upper()
      os.chdir(dir)
      for files in os.listdir("."):
  
	  if files.endswith(f_type):
	
	      if os.path.isdir(dir+dirname):
		  shutil.move(dir+files,dir+dirname)
        
	      else:
		  os.mkdir(dir+dirname)
		  shutil.move(dir+files,dir+dirname)
		
      return	  
  
  except IOError:
      print "Error in reading file :IO ERROR "
str1="mp3 rpm zip pdf doc jpg flv tar torrent txt zip exe "
print "Enter a Different Extensions seprated by space , Already in library : "+str1+"\n",
stri = raw_input()
str1=str1+stri
stri.split(' ');
for a in stri :
	#print a 
	sort(a)

print "\nDone"

