# Before "make install", this script should be runnable with "make test".
# After "make install" it should work as "perl t/Jpeg2000.t".

BEGIN {
    $| = 1; print "1..3\n"; $Image::ExifTool::configFile = '';
    require './t/TestLib.pm'; t::TestLib->import();
}
END {print "not ok 1\n" unless $loaded;}

# test 1: Load the module(s)
use Image::ExifTool 'ImageInfo';
use Image::ExifTool::Jpeg2000;
$loaded = 1;
print "ok 1\n";

my $testname = 'JXL';
my $testnum = 1;

# test 2: Extract information from JXL.jxl
{
    ++$testnum;
    my $exifTool = new Image::ExifTool;
    my $info = $exifTool->ImageInfo('t/images/JXL.jxl', '-system:all');
    print 'not ' unless check($exifTool, $info, $testname, $testnum);
    print "ok $testnum\n";
}

# test 3: Write some new information
{
    ++$testnum;
    my $exifTool = new Image::ExifTool;
    my $testfile = "t/${testname}_${testnum}_failed.jxl";
    unlink $testfile;
    my @writeInfo = (
        [ 'XMP:Subject' => 'test subject' ],
        [ 'EXIF:Artist' => 'test artist' ],
    );
    $exifTool->Options(IgnoreMinorErrors => 1);
    $exifTool->SetNewValue(@$_) foreach @writeInfo;
    my $ok = writeInfo($exifTool, 't/images/JXL.jxl', $testfile, undef, 1);
    my $info = $exifTool->ImageInfo($testfile, '-system:all');
    if (check($exifTool, $info, $testname, $testnum) and $ok) {
        unlink $testfile;
    } else {
        print 'not ';
    }
    print "ok $testnum\n";
}

# end
