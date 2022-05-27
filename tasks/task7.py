import random
from string import ascii_lowercase

def random_str():
  name_len = random.randint(3, 9)
  list_ = []
  for i in range(name_len):
    list_.append(random.choice(ascii_lowercase))
  name =''.join(list_)
  return name

def person():
    d ={'name': random_str().title(),
    'surename': random_str().title()}

    d['login'] = "@"+random_str()+"_"+ d.get('name')
    d['password'] = random_str()
    d['email'] = d.get('name')+"_"+d.get('surename')+"@"+random_str()+".com"
    d['phone'] = "+7("+str(random.randint(100, 999))+")"+\
str(random.randint(100, 999))+'-'+str(random.randint(10, 99))+'-'+\
str(random.randint(10, 99))
    d['register_time'] = str(random.randint(2001, 2021))\
+"-"+str(random.randint(1, 12))+"-"+\
str(random.randint(1, 30))+"T"+str(random.randint(1, 60))+":"+\
str(random.randint(1, 60))+":"+str(random.randint(1, 60))


    return d