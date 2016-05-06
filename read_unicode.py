#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import codecs
import sys, getopt

unique_list=dict()
def main(argv):
     inputfile = ' '
     outputfile = ' '
     try:
          opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile"])

     except getopt.GetoptError:
          print('read_unicode.py -i <inputfile> -o <outputfile')
          sys.exit(2)
     for opt, arg in opts:
          if opt == '-h':
               print('read_unicode.py.py -i <inputfile> -o <outputfile>')
               sys.exit()
          elif opt in ("-i", "--ifile"):
               inputfile = arg
               #print inputfile
          elif opt in ("-o", "--ofile"):
               outputfile = arg

     fwr=open(outputfile,'w');
     count=0
     final_percent=0.000
     curr_percent=0.000
     with codecs.open(inputfile,encoding='utf-8') as f:
          for line in f:
               for word in line:
                    if repr(word) != 'u\'\\n\'' and repr(word) != 'u\' \'':
                         if repr(word) in unique_list:
                              unique_list[repr(word)] += 1
                         else:
                              unique_list[repr(word)]=1
                         count += 1
     print("Total no .of characters %d" %count)                     
     for key in unique_list:
          curr_percent= float(100.0 *unique_list[key]/count)
          final_percent += curr_percent
          print("%s %d %2.3f" %(key,unique_list[key],curr_percent),file=fwr)
     print(final_percent)

if __name__ == "__main__":
     main(sys.argv[1:])
 #    inputfile='list'

