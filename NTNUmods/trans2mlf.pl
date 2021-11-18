#!/usr/bin/perl
# 
# Script for transforming LingIt's transcribe format to a standard mlf. 
# In addition to the format changes, the phone set is reduced and the new phone codes are "HTK-proof" (i.e. not
# e.g. starting with a numeral, )
#
# Use: trasn2mlf.pl -h
#
# T. Svendsen
#
$infile="part_1.trans";
$outfile="part_1.mlf";
$labfile="labels.list";


use Getopt::Std;
use File::Basename;

$scale=10000;

if ($opt_i){$infile=$opt_i;}
if ($opt_o){$outfile=$opt_o;}
if ($opt_l){$labfile=$opt_l;}
if ($opt_h){&Usage;}

open(IN,"$infile") || die "Could not open $infile for reading\n";
open(OUT,">$outfile") || die "Could not open $outfile for writing\n";

%labels=();

while(<IN>){
	chomp;
    # Some stuff to convert to MLF format
	if ($_ =~ /TRANSCRIPTION/){
		print OUT "#!MLF!#\n";
		next;
	}
	if ($_ =~ /part_1/){
		print OUT "$_\n";
		next;
	}
	if ($_ eq "."){
		print OUT ".\n";
		next;
	}
	@line=split(/\t/,$_);
    
    # Scale timing info
	$line[0]=$scale*$line[0];
	$line[1]=$scale*$line[1];
    
    # Remove stress info
	$line[2] =~ s/\"//g;
	$line[2] =~ s/\%//g;
    
    # Remove non-linguistic info
	if ($line[2] =~ /^</){$line[2]="sil";}
	if ($line[3] =~ /^</){delete($line[3]);}
    #
    # Transformation of symbols to "HTK-safe" versions
    #
	# Vowels
	if ($line[2] eq "{"){$line[2]="ae";}
	if ($line[2] eq "{:"){$line[2]="ae:";}
	if ($line[2] eq "2"){$line[2]="oe";}
	if ($line[2] eq "2:"){$line[2]="oe:";}
	if ($line[2] eq "}"){$line[2]="ou";}
	if ($line[2] eq "}:"){$line[2]="ou:";}
	# Diphthongs
	if ($line[2] eq "{i"){$line[2]="ei";}
	if ($line[2] eq "A}"){$line[2]="oev";}
	if ($line[2] eq "2y"){$line[2]="oei";}
	# Plosives
		# (no substitutions)
		
	# Fricatives and approximants
		# ( no substitutions)
		
	# Nasals, laterals and trills
		# ( no substitutions)
		
	# Retroflex
	if ($line[2] eq "t`"){$line[2]="rt";}
	if ($line[2] eq "d`"){$line[2]="rd";}
	if ($line[2] eq "n`"){$line[2]="rn";}
	if ($line[2] eq "l`"){$line[2]="rl";}
	if ($line[2] eq "s`"){$line[2]="rs";}
#
# Reductions
#
	# Vowels
	if ($line[2] eq "U"){$line[2]="ou";}
	if ($line[2] eq "3:"){$line[2]="oe:";}
	if ($line[2] eq "V"){$line[2]="oe:";}
	if ($line[2] eq "I"){$line[2]="i";}
	# Diphthongs
	if ($line[2] eq "aU"){$line[2]="oev";}
	if ($line[2] eq "@U"){$line[2]="oev";}
	if ($line[2] eq "2}"){$line[2]="oev";}
	if ($line[2] eq "eI"){$line[2]="ei";}
	if ($line[2] eq "}i"){$line[2]="Oy";}
	if ($line[2] eq "ui"){$line[2]="Oy";}
	
	# Plosives
	if ($line[2] eq "c"){$line[2]="C";}
	if ($line[2] eq "J\\"){$line[2]="d";}
    
    # Glottal stop
	if ($line[2] eq "?"){next;}
	
    # Fricatives and approximants
	if ($line[2] eq "w"){$line[2]="O";}
	if ($line[2] eq "z"){$line[2]="s";}
	if ($line[2] eq "Z"){$line[2]="S";}
	if ($line[2] eq "c__C"){$line[2]="C";}
	if ($line[2] eq "t__S"){$line[2]="tS";}
	if ($line[2] eq "d__Z"){$line[2]="C";}
	if ($line[2] eq "T"){$line[2]="f";}
	if ($line[2] eq "D"){$line[2]="d";}
	if ($line[2] eq "x"){$line[2]="h";}
	
    # Nasals, laterals and trills
	if ($line[2] eq "4"){$line[2]="r";}
	if ($line[2] eq "R"){$line[2]="r";}
	if ($line[2] eq "r\\"){$line[2]="r";}
	if ($line[2] eq "J"){$line[2]="n";} # should be changed
	if ($line[2] eq "L"){$line[2]="l";} # should be changed
	
    # Retroflex
	if ($line[2] eq "r`"){$line[2]="l";}
	
    # Syllabic consonants - reduced to their non-syllabic counterparts due to lack
	# of training data
	if ($line[2] eq "l_="){$line[2]="l";}
	if ($line[2] eq "l`_="){$line[2]="rl";}
	if ($line[2] eq "m_="){$line[2]="m";}
	if ($line[2] eq "n_="){$line[2]="n";}
	if ($line[2] eq "n`_="){$line[2]="rn";}
	if ($line[2] eq "4_="){$line[2]="r";}
	if ($line[2] eq "J_="){$line[2]="n";}
	if ($line[2] eq "L_="){$line[2]="l";}
	if ($line[2] eq "R_="){$line[2]="r";} 
	if ($line[2] eq "N_="){$line[2]="N";}
	if ($line[2] eq "r\\_="){$line[2]="r";}
	if ($line[2] eq "s_="){$line[2]="s";}
	if ($line[2] eq "t`_="){$line[2]="rt";}
	if ($line[2] eq "v_="){$line[2]="v";}
	
	
	$labels{$line[2]}=1;
	print OUT "$line[0]";
	for ($i=1;$i<=$#line;$i++){print OUT "\t$line[$i]";}
	print OUT "\n";
}
close(IN);
close(OUT);
open(LAB,">$labfile") || die "Could not open $labfile for writing\n";
foreach $lab (sort keys %labels){
	print LAB "$lab\n";
}
close(LAB);

sub Usage{
	print "Script that reads original NB_Tale transcriptions (.trans), reduces the symbol inventory\n";
	print "and writes the reduced phonemic transcriptions to an HTK mlf file. \n";
	print "The output files have the same name as the basename in the mlf file, and the extension .phn\n\n";
	print "Use: mlf2nist.pl -i <mlffile> -o <nistfile directory>  [-F <samplerate>]\n";
	print "\t -i input .trans file\n";
	print "\t -o output .mlf file\n";
	print "\t -l output list containing reduced phone set \n";
	print "\t -h this message\n";
	exit;
}