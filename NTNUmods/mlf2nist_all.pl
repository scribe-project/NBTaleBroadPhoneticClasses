#!/usr/bin/perl
#
# 	Script that extracts labeling information for all files in a HTK MLF file,\n";
#	and writes the information to a NIST (TIMIT) format label files. \n";
#	The output files have the same name as the mlf file basename, and the extension .phn
#	Use: mlf2nist.pl -i <mlffile> -o <nistfile directory>  [-F <samplerate>]\n";
#		-i input mlf file\n";
#		-o output directory for nist format files (include path)\n";
#		-t -F sampling frequency in Hz (default 16000)\n";
# 
# T.Svendsen
#
use Getopt::Std;
use File::Basename;

getopts('i:o:F:h');
$Fs=16000;
$HtkConst=10000000;
if ($opt_F){$Fs=$opt_F;}
if ($opt_i){
    $Mlf=$opt_i;
} else {
	&Usage;
}
if ($opt_o){
    $nist=$opt_o;
} else {
	&Usage;
}
if ($opt_h){&Usage;}

open(MLF,"$Mlf") || die "Cannot open $Mlf for reading\n";
$inside=0;
#$finished=0;
while(<MLF>){
#    if ($finished == 1){exit;}
    chomp;
    if ($_ =~ /#!MLF!#/){next;}
    if (($_ =~ /\"/) && ($inside != 1)){
		$line=$_;
		$line =~ s/\"//g;
		($base,$path,$ext)=fileparse($line,'\..*');
		$outfile="$nist"."/"."$base".".phn";
		open(NIST,">$outfile") || die "Cannot open $outfile for writing\n";
		$inside=1;
        next;
    } else {
        if ($_ =~ /^\./){
            $inside=0;
			close(NIST);
            next;
        } else {
			if ($_ =~ '\t'){
            	($sstart,$end,$lab)=split('\t',$_);
            	$sstart = $Fs*$sstart/$HtkConst;
            	$end = $Fs*$end/$HtkConst;
            	print NIST "$sstart $end $lab\n";
			} else {
            	($sstart,$end,$lab)=split(' ',$_);
            	$sstart = $Fs*$sstart/$HtkConst;
           	 	$end = $Fs*$end/$HtkConst;
            	print NIST "$sstart $end $lab\n";
			}	
        }
    }
}

sub Usage{
	print "Script that extracts labeling information for all files in a HTK MLF file,\n";
	print "and writes the information to NIST (TIMIT) format label files. \n";
	print "The output files have the same name as the basename in the mlf file, and the extension .phn\n\n";
	print "Use: mlf2nist.pl -i <mlffile> -o <nistfile directory>  [-F <samplerate>]\n";
	print "\t -i input mlf file\n";
	print "\t -o output directory for nist format file (include path)\n";
	print "\t -t -F sampling frequency in Hz (default 16000)\n";
	exit;
}