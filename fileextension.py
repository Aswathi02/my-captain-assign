#to accept the filename and print the extension of the file
name=input("enter the name of the file:")
s=name.split('.')
(repr(s[-1]))
if(s[-1]=='py'):
    print('the extenion of the file:python')
else:
    print('the extension of the file is',(repr(s[-1])))
