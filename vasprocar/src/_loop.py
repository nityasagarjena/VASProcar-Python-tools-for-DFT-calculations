# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print (" ")
print (" ")
print (" ")
print ("##############################################################")
print ("want to perform another task? ================================")
print ("[0] NOT                                                       ")
print ("[1] YES                                                       ")
print ("##############################################################") 
opcao = input (" "); opcao = int(opcao)
print (" ")

if (opcao == 0):
   exit()
   
if (opcao == 1):
   execute_python_file(filename = '_settings.py')
