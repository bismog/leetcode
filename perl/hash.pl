#!/usr/bin/env perl

use feature ':5.10';

my %bloosom = ('rose'=> 'red', 'lily'=>'white', 'tulip'=>'orange');
say "I know that rose is $bloosom{rose}.";

say "Do some change...";
$bloosom{rose} = 'black';
say "And now we get a $bloosom{rose} rose.";

my @flower_list = keys %bloosom;
my $flower_number = keys %bloosom;
say "Here flowers list as \"@flower_list\", there are $flower_number flowers in all.";

# Can key in hash be integer?
my %int_hash = (0=>'000', 1=>'111', 2=>'222');
my %str_hash = ('0'=>'000', '1'=>'111', '2'=>'222');
say "Show member with key 0: $int_hash{0}. ";
say "Show memeber with key \'0\': $str_hash{0}.";
