import numpy as np
import re

#                         Strings

a = "I am Abdelrahman Wael"   # Defining
a = 'I am Abdelrahman Wael'   # Defining

print(a[0])                   # Importing an item from the string
print(a[5])                   # Importing an item from the string
print(a[-1])                  # Importing an item from the string

#-----------------------------------------------------------------------------

b = ' ( Hello World ) '       # Declaring

print(b * 3)                  # To repeat the string 3 times

#-----------------------------------------------------------------------------

c = 'I have 13 Years Old'     # Declaring

print(c [ 4 : 12])            # To count from the item 5 to 12
print(c [   : 12])            # To count from the start to the item 12
print(c [ 4 :   ])            # To count from the item 4 to the end
print(c [   :   ])            # To Count from the start to the end
print(c [ 4 : 12 : 2 ])       # to count from item 4 to 12 by 2
print(c [   : 7  : 3 ])       # To count from the start to the item 7 by 3
print(c [ 8 :    : 4 ])       # To count from item 8 to the end by 4
print(c [   :    : 2 ])       # To count from the start to the end by 2

#-----------------------------------------------------------------------------

X = 'I love Alexandraia City than Cairo City'  # Declaring

print(list(X))                # To sort the items of the string randomly
print(sorted(list(X)))        # To sort the items of the string acsendingly 
print(set(X))                 # To sort the items of the string by non-reapeating
print(X.split())              # To sort the words not letters

#-----------------------------------------------------------------------------

Y = '41653675537574376375367368583475413245367694543551365362354'

print(Y.split("5"))

#-----------------------------------------------------------------------------

Z = 'bodiwael999@gmail.com,bodiwael111@gmail.com,bodiwael123@gmail.com'

print(Z.split(','))
print(Z.partition("@"))
print(Z.rpartition("@"))
print(Z.find("com"))
print(Z.rfind("com"))
print(Z.index("com"))
print(Z.replace('a' , 'l'))
print(Z.count("@"))
print(Z.capitalize())
print(Z.title())
print(Z.upper())
print(Z.swapcase())
print(Z.center(100))

#-----------------------------------------------------------------------------

K = 'Borg El_Arab'

print(K.ljust(30))     #  To make spaces in right of sentence with total 30
print(K.rjust(30))       #  To make spaces in left of sentence with total 30
print(K.ljust(30,'*'))     #  To make spaces with stars
print(K.rjust(30, '-'))      #  To make spaces with lines

#-----------------------------------------------------------------------------

W = '322006'
M = '1972009'
F = '11620013'

print(W.zfill(10))       # fill with zeros with total 10
print(M.zfill(10))         # fill with zeros with total 10
print(F.zfill(10))           # fill with zeros with total 10

#-----------------------------------------------------------------------------

A = 'Hello'  # It is all letters , there isn't any symbols or dots or spaces
B = 'Hello Python'   # It make the spaces as symbols
C = 'Hello#$..-='           # There is many symbols and dots

print(A.isalpha())
print(B.isalpha())
print(C.isalpha())

#-----------------------------------------------------------------------------

X = '****Hello World     '

print(X.strip())      # clear any spaces before or after the sentence
print(X.rstrip())       # clear any spaces after the sentence
print(X.lstrip())         # clear any spaces before the sentence
print(X.strip('*'))         # clear any starts

#-----------------------------------------------------------------------------

A = 'My name is\n\t\t\t:Abdelrahman wael'
print(A)  # To make lines and spaces , we use \n & \t

#-----------------------------------------------------------------------------

A = 'Abdelrahman '
B = 'Wael'

print(A,end = '') # print B in the same line of A
print(B)

#-----------------------------------------------------------------------------

A = 'Abdelrahman Wael'
B = 15

print('I am %s'%A)
print('I have %d Years old'%B)
print('My name is %s and I have %d years old'%(A,B))
print('There are %5d'%7)
print('There are %05d'%7)

#----------------------------------------------------------------------------

print('doesn\'t')
print("doesn't")
print('yes,"he said.')
print("\"yes,\"he said.")
print('"isn\'t,"she said')

#----------------------------------------------------------------------------

A = '32200654555'
B = '3d548252559'
C = 'HELLO'
D = 'hello'
E = 'Hello'

print(A.isdigit())
print(B.isdigit())
print(C.isupper())
print(D.islower())
print(E.istitle())

#----------------------------------------------------------------------------

a = 'Abdelrahman Wael Abdelrahman Rashad Ammar'

print(a.endswith('Ammar'))
print(a.startswith('Abd'))

#----------------------------------------------------------------------------

a = ' is friend of '.join(('Ahmed','Mohamed','Mahmoud'))

print(a)

#----------------------------------------------------------------------------

a = "The value of pi is {}".format(np.pi)

print(a)

#----------------------------------------------------------------------------

a = '{0} and {1}'.format('red','blue')
b = '{1} and {0}'.format('red','blue')

print(a)
print(b)

#----------------------------------------------------------------------------

a = "pi = {0:.3f} ".format(np.pi)

print(a)

#----------------------------------------------------------------------------

email = re.compile('\w+@\w+\.[a-z]{3}')
text = "try guido@python.org or guido@google.com"
print(email.findall(text))

#----------------------------------------------------------------------------

