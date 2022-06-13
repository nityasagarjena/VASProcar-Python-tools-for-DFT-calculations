
print ("##############################################################")
print ("## Digite o nome do arquivo a ser corrigido: ============== ##")
print ("## Por exemplo: PROCAR, DOSCAR, PARCHG, OUTCAR ============ ##")
print ("##############################################################") 
print ("Exemplos das correcoes aplicadas =============================")
print ("0.50000000-0.50000000   >>   0.50000000 -0.50000000")
print ("0.12345000-123   >>   0.12345000e-123")
print ("0.86000000-209   >>   0.86000000e-209")
print ("##############################################################") 
name = input ("name: "); name = str(name)
print (" ")

print ("..................")
print ("... Corrigindo ...")
print ("..................")
print (" ")

#---------------------------------------------------------------------------

original = dir_files + '/' + name
copia    = dir_files + '/' + name + '_Original'
shutil.copyfile(original, copia)

#---------------------------------------------------------------------------

with open(dir_files + '/' + name, 'rt') as file:
     r = file.read()

for i in range (10):     
    with open(dir_files + '/' + name, 'wt') as file:
         r = r.replace('-' + str(i) + '.', ' -' + str(i) + '.')
         file.write(r)

for i in range (10):     
    with open(dir_files + '/' + name, 'wt') as file:
         r = r.replace(str(i) + '-', str(i) + 'E-')
         file.write(r)

file.close()

#-----------------------------------------------------------------
print("======================= Concluido =======================")
#-----------------------------------------------------------------

#=======================================================================
# Opcao do usuario de realizar outro calculo ou finalizar o codigo =====
#=======================================================================
execute_python_file(filename = '_loop.py')
