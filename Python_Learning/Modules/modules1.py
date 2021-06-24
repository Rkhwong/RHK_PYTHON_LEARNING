import modules2 as s

s.printer()
s.anotherModule2()
print( s.tuplet )
print(s.list)
print(s.dict)

#Using DICT
a = s.dict
b = s.dict

a['name'] = 'A'
a['password'] = 'kjahsd213'

b['name'] = 'B'
b['password'] = ' 12lkj321 '

print(a)
print(b)

#Creating CLass
a = s.myClass("A","1232131412",1)
print(a)
print(a.name)
print(a.password)
print(a.keycode)

