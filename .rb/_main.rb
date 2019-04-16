#!/usr/bin/env ruby
# coding: UTF-8

# - - -  Require's  - - -

require 'json'


# - - - - - - - - - - - - -


file = File.open "vars.json"
data = JSON.parse(file)





# - - -  Ending  - - -

file.close
