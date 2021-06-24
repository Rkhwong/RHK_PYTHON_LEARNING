# write the function is_anagram
def is_anagram(test, original):
    if (len(test) == len(original)):
        if( sorted(test) == sorted(original)):
            return True
        else:
            return False
    return False

test = "foefet"
original = "toffee"
print ( is_anagram( test, original) )
