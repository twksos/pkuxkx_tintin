#!/usr/bin/python

import sys
import os
full_dir = os.path.dirname(os.path.realpath(__file__))
ifile_dir = os.path.join(full_dir,'tins_utf8')
ofile_dir = os.path.join(full_dir,'bin')

def utf8_to_gbk(file_name):
	ifile_path = os.path.join(ifile_dir,file_name)
	fi = open(ifile_path, "r")
	utf8_str = fi.read()
	fi.close()

	gbk_str = utf8_str.decode('UTF-8').encode('GBK')

	ofile_path = os.path.join(ofile_dir,file_name)
	fo = open(ofile_path, "w")
	fo.write(gbk_str);
	fo.close()

for root, dirs, files in os.walk(ifile_dir):
  for name in files:
  	if name != '.DS_Store':
  	  print 'transfer file: ' + name
  	  utf8_to_gbk(name)