#!/bin/bash
infile=$1
outfile=$2
cat $infile | sed "s:\![A-Za-z].*|::g" | sed "s:colspan=.*|::g" | sed "s:rowspan=.*|::" | sed "s:{{col.*::g" | sed "s:span\..*{::g" |\
    sed "s:^\.[a-zA-Z][a-zA-Z]*::g" > $outfile
