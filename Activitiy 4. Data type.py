Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Muhammad Irfan"
>>> NIM = 165
>>> Tinggi = 1.68
>>> Berat = 56
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type (Aku)
<class 'tuple'>
>>> ##this command is to know what is the type of Aku, the type of aku is class tuple so the python print <class 'tuple'>
>>> Aku [0]
2000
>>> ##this command call word in the tuple. its 2000 because in tuple the row of object is start at (0,1,2,...),if you write Aku[0] the python print 2000.
>>> a = NIM % 4 ; Aku [a]
56
>>> ##this command is to slice word in the tuple. its 56 because the value of 'a' is 1. so Aku[a] call the row 1 on Berat
>>> type (Aku[a])
<class 'int'>
>>> ##this command is to know what is type of Aku[a], type is int because value Aku[a] is 56. 
>>> Aku[a:4]
(56, 1.68, 165)
>>> ##this command slice word in the tuple. The answer is 56, 1.68, 165 because The value of 'a' is 1 so Aku[a:4] is from 1 to 4 it means from berat to nama.
>>> type(Aku[4])
<class 'str'>
>>> ##this command is to know what is the type of Aku[4]. its class string because in Aku[4] is Nama. the value of Nama is "Muhammad Irfan".
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> ##Aku[0] can't be changed to "ok" because tuple element is can't be changed
>>> type(Data)
<class 'tuple'>
>>> ##this command is to know what is the type of Data. the type of Data is tuple
>>> type(Data[4])
<class 'str'>
>>> ##this command is to know what is the type of Data[4]. its class string because in Data[4] is Nama. The value of Nama is "Muhammad Irfan"
>>> Data[4][5]
'm'
>>> ##This command is to slice word, the answer is 'm' because there is m in fifth object.
>>> Data[4][a:6]
'uhamm'
>>> ##This command is to slice word, the answer is 'uhamm' because in Data[4] is Nama, the value of Nama is "Muhammad Irfan" and Then the value of 'a' is 1 so [a:6] means [1:6]
>>> Data[0] = 'ok'; Data
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> ##Data[0] can't be changed because tuple element can't be changed
>>> Data[-a]
'Muhammad Irfan'
>>> ##This command is to slice word, The answer is "Muhammad Irfan" because The value of 'a' is 1 so it means [-1], The [-1] is Nama and the value of Nama is "Muhammad Irfan"
>>> range(a)
range(0, 1)
>>> ##because in the "a" data there is only 1 object.

