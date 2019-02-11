#if True:
#    Print('True')
#----------------------
#language ='Python'
#if language =='Python':
#    print('True')
#----------------------
# language ='Python'
# if language =='Python':
#     print('True')
# else:
#     print('False')
#----------------------
# language ='Java'
# if language =='Python':
#     print('True')
# elif language =='Java':
#     print('Java')
# else:
#     print('False')
#----------------------
# and
# or
# not
#----------------------
# language ='Java'
# user='allow'
# if language =='Python' and user=='allow':
#     print('True')
# elif language =='Java':
#     print('Java')
# else:
#     print('False')
#----------------------
# language ='Java'
# user='allow'
# if not language =='Python' and user=='allow':
#     print('True')
# elif language =='Java':
#     print('Java')
# else:
#     print('False')
#----------------------
# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(b))
#----------------------
a=[1,2,3]
b=a
print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(a)==id(b))
#----------------------
