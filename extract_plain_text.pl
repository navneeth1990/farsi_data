#!/usr/bin/perl
$list="$ARGV[0]";
#open(FP_LIST,"<:encoding(UTF-8)",$list);
open(FP_LIST,$list);
while(<FP_LIST>) {
    $extracted_file=$_;
    #open(FP_TEXT_FILE,"<encoding(UTF-8)",$extracted_file);
    open(FP_TEXT_FILE,$extracted_file);
    while(<FP_TEXT_FILE>) {
        chomp;
        $line=$_;
        if($line !~ /:/ && $line !~ /</ && $line !~ /\/\*/ ) {
            print $line,"\n";
        }
    }
    close(FP_TEXT_FILE);
}
close(FP_LIST);
