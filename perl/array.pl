#!/usr/bin/env perl


use feature ':5.10';

my @weekday = ('Monday', 'Tuesday', 'Sunday');
say "The second weekday is $weekday[1].";

$weekday[2] = 'Wednesday';
say "The third weekday is $weekday[2].";

$number_of_weekday = @weekday;
say "There are $number_of_weekday days in a week.";
