#!/usr/bin/env ruby
# puts ARGV[0].scan(/(?<=from:)([^\]]*)|(?<=to:)([^\]]*)|(?<=flags:)([^\]]*)/).join(",")
puts ARGV[0].scan(/(?<=from:).*?(?=\])|(?<=to:).*?(?=\])|(?<=flags:).*?(?=\])/).join(",")
# add comment
