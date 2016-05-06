#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import codecs
import sys, getopt, re

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
     farsi_text=[]
     f=open(inputfile,'r')
     for filename in f:
          with codecs.open(filename.split( '\n' )[0],encoding='utf-8') as f:
               for line in f:
                    for word in line:
                         #print(repr(word))
                         if re.search(r"u\'\\u06.*\'",repr(word)):
                              #farsi_text.append(repr(word))
                              print(word.encode('utf-8'),end="",file=fwr)
                         else:
                              print(' ',end="",file=fwr)
                              #farsi_text.append('\n')
          print('\n',file=fwr)

     #for i in range(len(farsi_text)):
         # print(farsi_text[i].encode('utf-8'),end=" ",file=fwr)
if __name__ == "__main__":
     main(sys.argv[1:])
 #    inputfile='list'

