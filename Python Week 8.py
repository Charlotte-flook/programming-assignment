from random import*

names = ['Charlotte','Jasmine','Elise','Josie','Toby','Kyle','Luke']
shuffle(names)
sent = names[0]
for name in names[1:len(names)-1]: sent+=f', {name}'
sent+= f' and {names[-1]}'
print(sent)
