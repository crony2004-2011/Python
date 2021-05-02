from pygeocoder import Geocoder
import feedparser
import time
import os
os.chdir(r'C:\Users\hp\Desktop\jupyter')
import playsound
from playsound import playsound
#x = input('Enter sound to play')
#y = '.mp3'
#xx = x + y
#playsound(xx)

#address = "sunrise colving, gafoornagar, hydrabad"
#x = Geocoder.geocode(address)
#for i in x:
#    print(i)

#REVERSE NUMBER
#name = 'ococ'
#print(name[::-1])
l = [1,2,3,2,1]
for i in enumerate(l):
    print(i)
id = [1,2,3,4]
name = ['aman','milo','coco','tuktuk']
for i,j in zip(id,name):
    print(i,j)

a = ['coco','milo','tuktuk']
#x = input('Which name to remove??')
#a.remove(x) # pop is for array index numbers
print(a)

import pathlib
file_name = os.path.basename(r'C:\Users\hp\Desktop\jupyter\model\model.onxx')
print(os.path.splitext(file_name)) #get file name exact but split by '.'
print(pathlib.Path(file_name).suffix) #get file type

with open('wdsr.py', encoding = 'utf-8') as f:
    print(f.readlines())

class adhar:
    religon = 'hindu'
    #self
    def __init__(self,name,age,image):
        self.name = name
        self.age = age
        self.image = image

    def add(self,address):
        self.__add = address

class pan(adhar):
    def __init__(self,bank):
        self.bank = bank

obj1 = pan('sbi')
print(obj1.__class__.religon)
print("Hi my bank account is in {}".format(obj1.bank))
#ISINSTANCE
print(isinstance(obj1, adhar))

#two lists to dictionaries
states = ['Georgia','Florida','North Carolina']
city = ['Atalanta','Jacksonville','Charleston']
dic = zip(states,city)
print(dic)
dictionary = dict(zip(states,city))
print(dictionary)

#get class name from instance object
print(type(obj1).__name__)

#time
import time
import datetime
from datetime import datetime
a = time.time()
a_strp = '22 March, 2011'
time.sleep(2)
aa = time.time()
b = datetime.now()
bb = str(b)
formatted_b = b.strftime("%m/%d/%Y/%H/%M/%S") #m d Y H M S
#formatted_c = datetime.strptime(a_strp, "%d  %m , %Y")
print(a,"-----------------",b,'--------------------------',formatted_b)
print(aa-a)

l = [1,2,3,4,5,3,2,4,2,1,1,4,7,8,9]
print(set(l)) #prints uniques values
print(l.count(2))  #counts number of values of the particular number

import random
print(random.choice(l))

#find datatype
def t(num):
    try:
        float(num)
        print('True')
    except:
        print('False')
t('22.3')

my_string = "My name is Aman"
print(my_string[:7])  #first seven
print(my_string[10:15]) #from 10th to 15th
print(my_string[::-1])  #prints whole string opposite

#SPLITTING ARRAYS
import numpy as np
q = [1,2,3,4,5,6]
print(np.array_split(q,3))

#dictionary and JSON
import json
d = {'name':'aman','adhar':'585571228003','pan':'AYWPT9657Q'} #this is dictionary
print('keys: ',d.keys(), '  Values: ',d.values())
person = '{"name": "aman", "adhar":"585577128003"}'  #this is json
p = json.loads(person) #json has become list through loads
j_new = json.dumps(p) #the list is back in json
print(type(j_new))

#REGEX search findall sub
import re
pwd = 'aabacdxyz'
x = re.search('^a.*z$', pwd)
if x:
    print('match')
else:
    print("Not Match")
xx = re.findall('a',pwd)
print(xx)
xxxx = re.sub('x','e',pwd)   #replace letter with sub
print(xxxx)

#calculate area of circle with function
#radius = int(input('Enter radius :'))
print("The area is ",int(3.14*4**2))

#weresource PRACTICE https://www.w3resource.com/python-exercises/python-basic-exercises.php
#5
x = 'aman'
y = 'takshak'
r = str(x) + str(y)
r = r[::-1]
print(r)
#7 get file type, we can use os.path.basename and os.path.splittext also but path has to be legitimate
#file = input('Enter file name')
file = 'a.csv'
file_type = file.split('.')
print(file_type[1])
#14
from datetime import date
d1 = date(2014,5,5)
d2 = date(2021,5,1)
print(d2-d1, ' days since modi got elected')
#28
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
]
for i in numbers:
    if i % 2 == 0:
        print('Even numbers are :',i)
    else:
        pass

#x = input('first letter')
x = 'a'
if ord(x) == 97:
    print('correct')
else:
    print('false')

#w3resource practice https://www.w3resource.com/python-exercises/basic/
#1
x = [2,3,4,3,2,3,5,6,7,9]
if len(x) == len(set(x)):
    print('same numbers exist')
else:
    pass

import platform as pl

os_profile = [
    'platform',
    'processor',
]
for key in os_profile:
    if hasattr(pl, key):
        print(key +  ": " + str(getattr(pl, key)()))




