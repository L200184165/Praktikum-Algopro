Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Name = "Muhammad Irfan"
>>> ##this command put string "Muhammad Irfan" to the function of Name, if we call it.
>>> Name
'Muhammad Irfan'
>>> NIM = "L200184165"
>>> ##this command put string "L200184165" to the function of NIM. if we call it
>>> NIM
'L200184165'
>>> X= "1" + NIM[7:]
>>> ##this command add a slice of NIM data (from 7th character until the last string) and added "1" in front of it
>>> X
'1165'
>>> a = int(X)
>>> ##this command is to change a the type of X/NIM, from string type to integer type.
>>> a
1165
>>> b =len (Name)
>>> ##this command is to know how many the character of a Name.
>>> b
14
>>> type(a)
<class 'int'>
>>> ##this command is to know, what is the type of function a.
>>> type(b)
<class 'int'>
>>> ## this command is to know, what is the type of function b.
>>> a/b
83.21428571428571
>>> ##this command is to devide 'a with b' the result is not rounded off
>>> a//b
83
>>> ##this command is to divide 'a with b' the result is rounded off
>>> 10*(a-999)
1660
>>> ##this command is to subtract value of a-999, and then multiply by 10.
>>> b**2
196
>>> ##this command is to rooted function b.
>>> a%b
3
>>> ##this command give result after dividing the value of a and b.
>>> c = 12.5
>>> ## this command put float "12.5" to the function of c, if we call it
>>> c
12.5
>>> type(c)
<class 'float'>
>>> ##this command is to know what is the type of function c.
>>> a/c
93.2
>>> ##this command is to devide 'a with c' with the result is not rounded off
>>> a//c
93.0
>>> ##this command is to divide 'a with c' with the result is rounded off
>>> a%c
2.5
>>> ##this command give result after dividing the value of a and c.
>>> c>b
False
>>> ##this command is to know who had the biggest number/value, in this case the function 'c' had the biggest number/value
>>> type(c > b)
<class 'bool'>
>>> ##this command is to know what is the type of 'c > b'
>>> a > b and b > c
True
>>> ##this command is to know who had the biggest number/value, in this case the function 'a' had biggest number than function 'b', and function 'b' had biggest number than function 'c'
>>> a > 1100 or b < 10
True
>>> ##this command is to know who had the biggest number/value, in this case function 'a' had biggest number than 1100 and 'b' is smaller than 10 or 10 is biggest than 'b'
