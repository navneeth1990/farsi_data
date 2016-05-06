#!/bin/bash

perl extract_plain_text.pl list > temp_files/perlout
sh remove_images.sh temp_files/perlout temp_files/shellout
python read_unicode.py -i temp_files/shellout -o temp_files/chars
sort -k2 -n temp_files/chars > temp_files/chars_out
exit

if [ 0 -eq 1 ]; then
sed "s:^u'::g" temp  | sed "s:.*[A-Z].*::g" | sed "s:^<.*::g" |  sed "s:'::g"

awk -F "\\" '{
    for(i=1;i<NF;i++) {
      if($i!="" && !seen[$i]) {
             printf("\\%s\n",$i);
             ++seen[$i];
      }
    }
}' temp1  > temp2
fi
