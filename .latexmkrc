#!/usr/bin/env perl
$latex = 'platex -synctex=1 -halt-on-error -file-line-error -interaction=nonstopmode %O %S';
$bibtex = 'pbibtex %O %S';
$dvipdf = 'dvipdfmx %O -o %D %S';
$makeindex = 'mendex %O -o %D %S';
$pdf_mode = 3;  # platex -> dvipdfmx -> PDF
$max_repeat = 5;
$pdf_previewer = 'open -a Preview %S';
$pdf_update_method = 4;  # 自動更新
$pvc_view_file_via_temporary = 0;
