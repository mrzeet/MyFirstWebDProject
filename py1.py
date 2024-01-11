Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+7
9
"hello"
'hello'
name="ram"
type(name)
<class 'str'>
age=26
type(age)
<class 'int'>
height=5.10
type(height)
<class 'float'>
company
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    company
NameError: name 'company' is not defined
company=None
type(company)
<class 'NoneType'>
eq=["10th","12th","BCA"]
type(eq)
<class 'list'>
#mutable, add something new , remove old element
eq
['10th', '12th', 'BCA']
eq[2]
'BCA'
eq[2]="BSCIT"
eq
['10th', '12th', 'BSCIT']
eq.pop()
'BSCIT'
eq
['10th', '12th']
eq.append("BCA")
eq
['10th', '12th', 'BCA']

eq.insert(1,"11th")
eq
['10th', '11th', '12th', 'BCA']
eq.remove("11th")
eq
['10th', '12th', 'BCA']
student=["amit","Nikhil","Abhishek","Idrajeet","Vishal","Akaram","Kirtan","shivani"]
student
['amit', 'Nikhil', 'Abhishek', 'Idrajeet', 'Vishal', 'Akaram', 'Kirtan', 'shivani']
course=["python","sq1","FSD","Java","Networking"]
course
['python', 'sq1', 'FSD', 'Java', 'Networking']
cos=student+course
cos
['amit', 'Nikhil', 'Abhishek', 'Idrajeet', 'Vishal', 'Akaram', 'Kirtan', 'shivani', 'python', 'sq1', 'FSD', 'Java', 'Networking']
parents=("father","mother")
type(parents)
<class 'tuple'>
parents[1]
'mother'
parents[0]
'father'
parents[0]="monterh India"
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    parents[0]="monterh India"
TypeError: 'tuple' object does not support item assignment
parents.append("gpa")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    parents.append("gpa")
AttributeError: 'tuple' object has no attribute 'append'



parents=("father","mother","father","mom")
type(parents)
<class 'tuple'>
parents
('father', 'mother', 'father', 'mom')
parents=set(parents)
parents
{'mother', 'mom', 'father'}
parents=tuple(parents)
type(parents)
<class 'tuple'>
parents
('mother', 'mom', 'father')
personalid={9334206244,7777788888,9334206244}
personalid
{7777788888, 9334206244}
type(personalid)
<class 'set'>

male=Ture
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    male=Ture
NameError: name 'Ture' is not defined
male=True
type(male)
<class 'bool'>
male
True
contact={"Rahul":5566566,"Rohan":8888888,"Mohit":999999}
type(contact)
<class 'dict'>
contact.val("Rohan")
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    contact.val("Rohan")
AttributeError: 'dict' object has no attribute 'val'

contact.get("Rohan")
8888888
contact.get("Rahul")
5566566
contact["Aman"]=111112222
contact
{'Rahul': 5566566, 'Rohan': 8888888, 'Mohit': 999999, 'Aman': 111112222}



name=["ram","shyam","mohan","Krishna"]
type(name)
<class 'list'>
phone=[1111111,222222,3333333,4444444]
type(phone)
<class 'list'>
phonebook=dict(zip(name,phone))
type(phonebook)
<class 'dict'>
phonebook
{'ram': 1111111, 'shyam': 222222, 'mohan': 3333333, 'Krishna': 4444444}
phonebook.get("mohan")
3333333
phonebook["mohan"]=55555
phonebook
{'ram': 1111111, 'shyam': 222222, 'mohan': 55555, 'Krishna': 4444444}



a=7
b=9
c=a+b
c
16


add=a+b
>>> add
16
>>> sub=a-b
>>> sub
-2
>>> mul=a*b
>>> power=a**b
>>> power
40353607
>>> div=b//a
>>> div
1
>>> rem=b%a
>>> rem
2
>>> 
>>> age=25
>>> res=age>25
>>> res
False
>>> res=age==25
>>> res
True
>>> 
>>> 
>>> user="admin"
>>> pas="123"
>>> 
>>> login=user=="Admin" and pas=="123"
>>> login
False
>>> login=user=="admin" and pas=="123"
>>> login
True
>>> login=user=="Admin" or pas=="123"
>>> login
True
>>> login=user=="Admin" or pas=="1234"
>>> login
False
