from string import ascii_lowercase

def word_value(string):
    val = []
    for letter in string.lower():
        for index, value in enumerate(ascii_lowercase, start=1):
            if letter == value:
                val.append(index)
    return sum(val)

def find_mostvalued(*args):
  max_value = 0
  most_valued =''
  for i in args:
    if max_value < word_value(i):
      max_value = word_value(i)
      most_valued = i
  return i


