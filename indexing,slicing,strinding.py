Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a = "i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[1]
' '
a[0]
'i'
a[5]+a[6]
'in'
a[2]
'a'
a[4]+a[5]
' i'


b = "I am learning python"
b[5]+b[6]+b[7]+b[8]+b[9]
'learn'
b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'python'

c="codegnan IT Solutions"
c[0]+c[1]+c[2]+c[3]
'code'
c[12]+c13]+c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
SyntaxError: unmatched ']'
c[12]+c[13]+c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'Solution'

r = "time is very precious"
r[-1]+r[-2]+r[-3]+r[-4]+r[-5]+r[-6]+r[-7]+r[-8]
'suoicerp'
r[-8]+r[-7]+r[-6]+r[-5]+r[-4]+r[-3]+r[-2]+r[-1]
'precious'
r[-13]+r[-12]+r[-11]+r[-10]
'very'
r[-16]+r[-15]
'is'
r[-21]+r[-20]+r[-19]+r[-18]
'time'

a = "hello hi how are you"
a[-3]+a[-2]+a[-1]
'you'
a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
'hello'
a[-11]+a[-10]+a[-9]
'how'

#slicing
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'

a="work until you succeed"
a[0:4]
'work'
a[5:10]
'until'
a[11:14]
'you'
a[15:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[15:]
'succeed'

b="simple is better than complex"
b[:6]
'simple'
b[7:9]
'is'
b[10:16]
'better'
b[17:21]
'than'
b[22:]
'complex'
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
SyntaxError: invalid syntax. Is this intended to be part of the string?
c="vizag is city of destiny"
c[-7:]
'destiny'
c[-10:-8]
'of'
c[-15:-11]
'city'
c[-18:-16]
'is'
c[:-19]
'vizag'
>>> 
>>> a = "vijayawada is a royal city"
>>> a[-4:]
'city'
>>> a[-10:-5]
'royal'
>>> a[-12:-11]
'a'
>>> a[-15:-13]
'is'
>>> a[:-16]
'vijayawada'
>>> 
>>> #striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a[::-1]
'ecneics atad'
>>> 
>>> a="machine learing"
>>> a="machine learning"
>>> a[::5]
'mnag'
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a[::6]
'men'
>>> a[7:]
' learning'
>>> a[:9]
'machine l'
>>> a[6:11]
'e lea'
>>> a[2:8]
'chine '
>>> a[5:12]
'ne lear'
