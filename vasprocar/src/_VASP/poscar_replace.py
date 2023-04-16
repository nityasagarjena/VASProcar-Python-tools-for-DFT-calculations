# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print("#######################################################")
print("###### POSCAR - Ion substitution in the lattice: ######")
print("#######################################################")
print(" ")

import random

#--------------------------------------------------------
poscar = open(dir_files + '/POSCAR', "r")
new_poscar = open(dir_files + '/output//POSCAR_new', "w")
#--------------------------------------------------------

#===============================================
# Copiando as linhas iniciais do arquivo POSCAR:
#===============================================

for i in range(5):
    VTemp = poscar.readline()
    VTemp = str(VTemp)
    new_poscar.write(f'{VTemp}')

#============================================================
# Obtendo o numero total de diferentes tipos de ions da rede:
# Armazenando os rotulos dos diferentes tipos de ions:
#============================================================

VTemp = poscar.readline().split()
n_tipo = len(VTemp)

rotulo = []

for i in range(n_tipo):
    rotulo.append(str(VTemp[i]))

#============================================================
# Obtendo o numero total de ions da rede:
# Armazenando o numero de ions para cada tipo de ion da rede:
#============================================================

VTemp = poscar.readline().split()

ni = 0
n_ion = [0]*n_tipo

for i in range(n_tipo):
    ni += int(VTemp[i])
    n_ion[i] = int(VTemp[i])

label = [0]*ni

for i in range(n_tipo):
    name = rotulo[i]
    for j in range(n_ion[i]):
        contador = (i)*n_ion[i] + (j)
        label[contador] = name

#===============================================================
# Armazenando o tipo de coordenadas utilizada no arquivo POSCAR:
#===============================================================

VTemp = poscar.readline()
t_coord = str(VTemp)

#=====================================================
# Armazenando as coordenadas de todos os ions da rede:
#=====================================================

ni_coord = [[0]*(4) for i in range(ni)]  # ni_coord[ni][4]

for i in range(ni):
    VTemp = poscar.readline().split()
    for j in range(4):
        if (j <= 2):
           ni_coord[i][j] = float(VTemp[j])
        if (j == 3):
           ni_coord[i][j] = label[i]

#======================================
# Obtendo os ions a serem substituidos: 
#======================================

print(" ")
print ("##############################################################")
print ("Para realizar a substituicao, Digite como nos exemplos abaixo:")
print ("ion a ser substituido, novo ion, numero de substituicoes =====")
print ("Observacao [1]: Os ions sao substituidos de forma aleatoria ==")
print ("Observacao [2]: Para excluir um ion da rede, utilize a palavra")
print ("                null para designar o ion New. ----------------")
print ("Exemplos: ====================================================")
print ("ion OLD, ion New, Substituicoes:  C  Si 7 ")
print ("ion OLD, ion New, Substituicoes:  H  N  24")
print ("ion OLD, ion New, Substituicoes:  Se W  64")
print ("ion OLD, ion New, Substituicoes:  O null 9")
print ("##############################################################")
print(" ")

print ("##############################################################")
print ("# ions atuais da rede: =======================================")
for j in range(n_tipo):
    print (f'# {rotulo[j]} ({n_ion[j]} ions) ===============================================')
print ("##############################################################")
print(" ")
print ("##############################################################")
print ("### Realize a substituicao: ==================================")
print ("##############################################################")
selected_replace = input ("ion OLD, ion NEW, Substituicoes:  ").replace(':',' ').replace('-',' ').replace(',',' ').replace('*',' ').replace('Null','null').replace('NULL','null').split()

ion_OLD = str(selected_replace[0])
ion_NEW = str(selected_replace[1])
Subst   = int(selected_replace[2])

ion_NEW = ion_NEW

#==================================================
# Obtendo o intervalo de ions a serem substituidos: 
#==================================================

cont1 = 0

for i in range(ni):
    if (ion_OLD == ni_coord[i][3]):
       cont1 += 1
       if (cont1 == 1):
          int_i = i
          int_f = i
       if (cont1 > 1):
          int_f += 1

#=========================================================
# Adicionando um novo rotulo aos diferentes tipos de ions: 
#=========================================================

cont2 = 0

for i in range(n_tipo):
    if (ion_NEW == rotulo[i]):
       cont2 += 1

if (cont2 == 0 and Subst > 0):
   rotulo.append(ion_NEW)

#===============================================
# Obtendo a sequencia aleatoria de substituicao: 
#===============================================

sequencia_full = list(range(int_i,(int_f+1))) # Criar uma vetor com numeros distribuidos aleatoriamente entre [int_i] e [int_f]
random.shuffle(sequencia_full)

if (Subst > 0):
   sequencia = [0]*Subst
   for i in range(Subst):
       sequencia[i] = sequencia_full[i] 

sequencia = sorted(sequencia) # Reorganiza a sequencia de substituicoes em ordem crescente

#============================
# Efetuando as substituicoes: 
#============================

cont2 = 0

for i in range(ni): 
    if (i == sequencia[cont2]):
       if (cont2 < (Subst -1)): cont2 += 1
       ni_coord[i][3] = ion_NEW

#==================================
# Escrevendo o novo arquivo POSCAR: 
#==================================

new_rotulo = []
new_n_tipo = []

for i in range(len(rotulo)):
    cont3 = 0
    for j in range(ni):
        if (ni_coord[j][3] == rotulo[i]): cont3 += 1
        if (j == (ni-1)): new_n_tipo.append(cont3)

#----------------------------------

for i in range(len(rotulo)):
    if (new_n_tipo[i] > 0):
       new_rotulo.append(rotulo[i])
       if (rotulo[i] != 'null'): 
          new_poscar.write(f'{rotulo[i]} ') 
new_poscar.write(f' \n')

#----------------------------------

for i in range(len(rotulo)):
    if (new_n_tipo[i] > 0 and new_rotulo[i] != 'null'):
       new_poscar.write(f'{new_n_tipo[i]} ')
new_poscar.write(f' \n') 

#---------------------------------- 

new_poscar.write(f'{t_coord}')

#---------------------------------- 
           
for i in range(len(new_rotulo)):
    name = new_rotulo[i]
    for j in range(ni):
        if (ni_coord[j][3] == name and new_rotulo[i] != 'null'):
           new_poscar.write(f'{ni_coord[j][0]} {ni_coord[j][1]} {ni_coord[j][2]} \n')

#---------------------------------- 

poscar.close()
new_poscar.close()

#---------------------------------------------------------------
print(" ")
print("======================= Completed =====================")
#---------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
