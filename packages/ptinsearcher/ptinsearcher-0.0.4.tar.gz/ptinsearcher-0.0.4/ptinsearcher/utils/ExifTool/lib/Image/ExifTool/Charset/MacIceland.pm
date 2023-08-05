#------------------------------------------------------------------------------
# File:         MacIceland.pm
#
# Description:  Mac Icelandic to Unicode
#
# Revisions:    2010/01/20 - P. Harvey created
#
# References:   1) http://unicode.org/Public/MAPPINGS/VENDORS/APPLE/ICELAND.TXT
#
# Notes:        The table omits 1-byte characters with the same values as Unicode
#------------------------------------------------------------------------------
use strict;

%Image::ExifTool::Charset::MacIceland = (
  0x80 => 0xc4, 0x81 => 0xc5, 0x82 => 0xc7, 0x83 => 0xc9, 0x84 => 0xd1,
  0x85 => 0xd6, 0x86 => 0xdc, 0x87 => 0xe1, 0x88 => 0xe0, 0x89 => 0xe2,
  0x8a => 0xe4, 0x8b => 0xe3, 0x8c => 0xe5, 0x8d => 0xe7, 0x8e => 0xe9,
  0x8f => 0xe8, 0x90 => 0xea, 0x91 => 0xeb, 0x92 => 0xed, 0x93 => 0xec,
  0x94 => 0xee, 0x95 => 0xef, 0x96 => 0xf1, 0x97 => 0xf3, 0x98 => 0xf2,
  0x99 => 0xf4, 0x9a => 0xf6, 0x9b => 0xf5, 0x9c => 0xfa, 0x9d => 0xf9,
  0x9e => 0xfb, 0x9f => 0xfc, 0xa0 => 0xdd, 0xa1 => 0xb0, 0xa4 => 0xa7,
  0xa5 => 0x2022, 0xa6 => 0xb6, 0xa7 => 0xdf, 0xa8 => 0xae, 0xaa => 0x2122,
  0xab => 0xb4, 0xac => 0xa8, 0xad => 0x2260, 0xae => 0xc6, 0xaf => 0xd8,
  0xb0 => 0x221e, 0xb2 => 0x2264, 0xb3 => 0x2265, 0xb4 => 0xa5, 0xb6 => 0x2202,
  0xb7 => 0x2211, 0xb8 => 0x220f, 0xb9 => 0x03c0, 0xba => 0x222b, 0xbb => 0xaa,
  0xbc => 0xba, 0xbd => 0x03a9, 0xbe => 0xe6, 0xbf => 0xf8, 0xc0 => 0xbf,
  0xc1 => 0xa1, 0xc2 => 0xac, 0xc3 => 0x221a, 0xc4 => 0x0192, 0xc5 => 0x2248,
  0xc6 => 0x2206, 0xc7 => 0xab, 0xc8 => 0xbb, 0xc9 => 0x2026, 0xca => 0xa0,
  0xcb => 0xc0, 0xcc => 0xc3, 0xcd => 0xd5, 0xce => 0x0152, 0xcf => 0x0153,
  0xd0 => 0x2013, 0xd1 => 0x2014, 0xd2 => 0x201c, 0xd3 => 0x201d,
  0xd4 => 0x2018, 0xd5 => 0x2019, 0xd6 => 0xf7, 0xd7 => 0x25ca, 0xd8 => 0xff,
  0xd9 => 0x0178, 0xda => 0x2044, 0xdb => 0x20ac, 0xdc => 0xd0, 0xdd => 0xf0,
  0xdf => 0xfe, 0xe0 => 0xfd, 0xe1 => 0xb7, 0xe2 => 0x201a, 0xe3 => 0x201e,
  0xe4 => 0x2030, 0xe5 => 0xc2, 0xe6 => 0xca, 0xe7 => 0xc1, 0xe8 => 0xcb,
  0xe9 => 0xc8, 0xea => 0xcd, 0xeb => 0xce, 0xec => 0xcf, 0xed => 0xcc,
  0xee => 0xd3, 0xef => 0xd4, 0xf0 => 0xf8ff, 0xf1 => 0xd2, 0xf2 => 0xda,
  0xf3 => 0xdb, 0xf4 => 0xd9, 0xf5 => 0x0131, 0xf6 => 0x02c6, 0xf7 => 0x02dc,
  0xf8 => 0xaf, 0xf9 => 0x02d8, 0xfa => 0x02d9, 0xfb => 0x02da, 0xfc => 0xb8,
  0xfd => 0x02dd, 0xfe => 0x02db, 0xff => 0x02c7,
);

1; # end
