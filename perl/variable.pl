#!/usr/bin/env perl

use feature ':5.10';

my $xxx = 'apple';
say "This is a $xxx.";

my $count = 55;
say "There are $count ${xxx}s.";

my $a = 8;
my $b = $a + 1;
say "Variable b is $b";

my $aa = '8';
my $bb = $aa + '1';
my $bb2 = $aa . '1';
say "Variable bb is $bb";
say "Variable bb2 is $bb2";
