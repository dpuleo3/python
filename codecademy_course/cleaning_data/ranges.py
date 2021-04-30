#The regex I adopted [2-9] [b-h]ats will match 
# the text I adopted 4 bats as well as I adopted 8 cats and even I adopted 5 hats.

#With ranges we can match any single capital letter with the regex [A-Z], 
# lowercase letter with the regex [a-z], any digit with the regex [0-9]. 


#shorthand classes include:

#\w: the “word character” class represents the regex range [A-Za-z0-9_], 
#   and it matches a single uppercase character, lowercase character, digit or underscore

#\d: the “digit character” class represents the regex range [0-9], 
#   and it matches a single digit character

#\s: the “whitespace character” class represents the regex range [ \t\r\n\f\v], 
#   matching a single space, tab, carriage return, line break, form feed, or vertical tab


#Fixed quantifiers, denoted with curly braces {}, let us indicate the exact quantity of a character we wish to match, or allow us to provide a quantity range to match on.

# \w{3} will match exactly 3 word characters
# \w{4,7} will match at minimum 4 word characters and at maximum 7 word characters
# The regex roa{3}r will match the characters ro followed by 3 as, and then the character r, such as in the text roaaar.