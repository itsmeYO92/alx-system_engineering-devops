#!/usr/bin/env ruby
a = ARGV[0].scan(/(?<=from:)\+?\w+/).join
b = ARGV[0].scan(/(?<=to:)\+?\w+/).join
c = ARGV[0].scan(/(?<=flags:)[-:0-9]+/).join
printf("%s,%s,%s\n", a, b, c)
