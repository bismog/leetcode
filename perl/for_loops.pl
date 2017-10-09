#!/usr/bin/env perl

use feature ':5.10';

for my $index (1, 2, 3, 4, 5) {
    say $index;
}

# The same as (1, 2, 3, 4, 5)
# for my $i (1 .. 5) {
#     say $i;
# }

# say 1, 2, 3, 4, 5;

# my @one_to_ten = (1 .. 10);
# my $top_limit  = 25;
# 
# for my $i (@one_to_ten, 15, 20 .. $top_limit) {
#     say $i;
# }

# Output month day number in shuffle order.
%month_has = ('January'=>31, 'February'=>28, 'March'=>31, 'April'=>30, 'May'=>31, 'June'=>30, 'July'=>31, 'August'=>31, 'September'=>30, 'October'=>31, 'November'=>30, 'December'=>31);
for my $mon (keys %month_has) {
    say "$mon has $month_has{$mon} days.";
}
