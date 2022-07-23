
print (" ")
print (" ")
print (" ")
print ("##############################################################")
print ("Deseja realizar outro calculo? ===============================")
print ("[0] NAO                                                       ")
print ("[1] SIM                                                       ")
print ("##############################################################") 
opcao = input (" "); opcao = int(opcao)
print (" ")

if (opcao == 0):
   exit()
   
if (opcao == 1):
   execute_python_file(filename = '_settings.py')
