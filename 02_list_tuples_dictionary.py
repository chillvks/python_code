#! /usr/bin/python

tup1 = (1,2,3, 'vikas', 'singh')
tup2 = ('one', 'two', 'three', 'four')

tup3 = tup1 + tup2
print(tup1[3])
print(tup2[3])
print tup3

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
   t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, word in t:
    res.append(word)

print res

print("!!! Dictionary Demo !!!")
dict01 = {"vikas":10, "mohini":20,"reyansh":30}
print(dict01["vikas"])
dict01['anay'] = 40
print(dict01)
del dict01['vikas']
print(dict01)
dict01.clear()
print(dict01)
del dict01

# print(dict01); # As this is already deleted.
