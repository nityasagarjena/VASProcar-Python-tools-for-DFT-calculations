# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print("#######################################################")
print("## Gerador de arquivo KPOINTS (Plano 2D ou Malha 3D) ##")
print("#######################################################")
print(" ")

#==============================================================================
# Verificando a presença dos arquivos scf.out, nscf.in, nscf.out e bands.in ---
#==============================================================================

n_scf_o = 0

try:
    f = open(dir_files + '/scf.out')
    f.close()
    n_scf_o = 1
except:
    print('')
    print('... Arquivo scf.out ausente ...')

#-----------------------------------

n_nscf_i = 0

try:
    f = open(dir_files + '/nscf.in')
    f.close()
    n_nscf_i = 1
except:
    print('')
    print('... Arquivo nscf.in ausente ...')

#-----------------------------------

n_nscf_o = 0

try:
    f = open(dir_files + '/nscf.out')
    f.close()
    n_nscf_o = 1
except:
    print('')
    print('... Arquivo nscf.out ausente ...')

#-----------------------------------

n_bands_i = 0

try:
    f = open(dir_files + '/bands.in')
    f.close()
    n_bands_i = 1
except:
    print('')
    print('... Arquivo bands.in ausente ...')

#-----------------------------------  

if (n_scf_o != 0 and n_nscf_i != 0 and n_nscf_o != 0 and n_bands_i != 0):  
   execute_python_file(filename = DFT + '_info_b.py')
   
   print("##############################################################")
   print("# Obtendo informacoes da rede e do calculo efetuado: ======= #")
   print("##############################################################")

   print(" ")
   print(".........................")
   print("... Espere um momento ...")
   print(".........................")
   print(" ")

#=========================================================================
# Obtendo parâmetros de input: -------------------------------------------
#=========================================================================

print("#######################################################")
print("## Que tipo de KPOINTS deseja gerar? ==============  ##")
print("#######################################################")
print("## [1] Plano 2D na Zona de Brolluin                  ##")
print("## [2] Malha 3D na Zona de Brolluin                  ##")
print("#######################################################")
tipo = input (" "); tipo = int(tipo)
print(" ")

print("#######################################################")
print("## Quanto a estrutura do arquivo KPOINTS, deseja que ##")
print("#######################################################")
print("## [0] Cada ponto-k seja escrito explicitamente      ##")
print("## [1] Seja escrito no modo de linha (menor tamanho) ##")
print("#######################################################")
estrutura = input (" "); estrutura = int(estrutura)
print(" ")

print("#######################################################")
print("## Deseja escolher um ponto-k central ? ============ ##")
print("#######################################################")
print("## [0] SIM                                           ##")
print("## [1] NAO                                           ##")
print("#######################################################")
point = input (" "); point = int(point)
print(" ")

if (n_scf_o != 0 and n_nscf_i != 0 and n_nscf_o != 0 and n_bands_i != 0):
   print("=======================================================")
   print("Vetores Primitivos da Rede Reciproca:                  ")
   print("-------------------------------------------------------")
   print(f'Param. = {Parametro} Angs.                            ')
   print(f'B1 = 2pi/Param.({B1x}, {B1y}, {B1z})                  ')
   print(f'B2 = 2pi/Param.({B2x}, {B2y}, {B2z})                  ')
   print(f'B3 = 2pi/Param.({B3x}, {B3y}, {B3z})                  ')
   print("=======================================================")
   print(" ")

print("#######################################################")
print("## Qual sistema de coordenadas quer adotar? ======== ##")
print("#######################################################")
print("## [1] Coordenadas Diretas (k1, k2, k3):             ##")
print("##     K =  k1*B1 + k2*B2 + k3*B3                    ##")
print("## [2] Coordenadas Cartesianas (kx, ky, kz)          ##")
print("##     K =  2pi/Param.(kx, ky, kz)                   ##")
print("#######################################################")
coord = input (" "); coord = int(coord)
print(" ")

if (coord == 1):
   ch1 = 'k1'; ch2 = 'k2'; ch3 = 'k3'
if (coord == 2):
   ch1 = 'kx'; ch2 = 'ky'; ch3 = 'kz' 

if (tipo == 1):
   print("#######################################################")
   print("## Defina qual plano deseja varrer na ZB: ========== ##")
   print(f'## [1] Plano {ch1}{ch2}  ({ch3} fixo) ======================= ##')
   print(f'## [2] Plano {ch1}{ch3}  ({ch2} fixo) ======================= ##')
   print(f'## [3] Plano {ch2}{ch3}  ({ch1} fixo) ======================= ##')
   print("#######################################################")
   esc = input (" "); esc = int(esc)
   print(" ")

print("#######################################################")
print("###### Defina as coordenadas a serem utilizadas: ######")
if (point == 1):
   print("## ================================================= ##")
   print("## Exemplo -- Plano 2D:                              ##")
   print(f'## {ch1}_inicial {ch1}_final Grid_pontos: -0.25 0.25 25    ##')
   print(f'## {ch2}_inicial {ch2}_final Grid_pontos:  0.35 0.50 31    ##')
   print(f'## Coordenada_fixa_{ch3}:                  0.50            ##')
   print("## ================================================= ##")
   print("## Exemplo Malha -- 3D:                              ##")
   print(f'## {ch1}_inicial {ch1}_final Grid_pontos: -0.10 0.10 25    ##')
   print(f'## {ch2}_inicial {ch2}_final Grid_pontos: -0.15 0.15 15    ##')
   print(f'## {ch3}_inicial {ch3}_final Grid_pontos:  0.00 0.50 31    ##')
   print("## ================================================= ##")
if (point == 0):
   print("## ================================================= ##")
   print("## Exemplo -- Plano 2D:                              ##")
   print(f'## ponto central ({ch1} {ch2} {ch3}):           0.5  0.0  0.0 ##')
   print(f'## (eixo-{ch1}) comprimento GRID_pontos:  0.25 25       ##')
   print(f'## (eixo-{ch2}) comprimento GRID_pontos:  0.10 15       #')
   print("## ================================================= ##")
   print("## Exemplo -- Malha 3D:                              ##")
   print(f'## ponto central ({ch1} {ch2} {ch3}):           0.0  0.0  0.0 ##')
   print(f'## (eixo-{ch1}) comprimento GRID_pontos:  0.50 31       ##')
   print(f'## (eixo-{ch2}) comprimento GRID_pontos:  0.25 25       ##')
   print(f'## (eixo-{ch3}) comprimento GRID_pontos:  0.11 15       ##')
   print("## ================================================= ##")
print("#######################################################")
print(" ")

#=========================================================================
# Definindo os limites do Plano 2D ou da Malha 3D manualmente: -----------
#=========================================================================

if (point == 1):
   
   if ((tipo == 1 and esc != 3) or (tipo == 2)):
      print(f'eixo-{ch1} --------------------------------------------')
      c1_i, c1_f, grid_1 = input (f'{ch1}_inicial {ch1}_final Grid_pontos: ').split()
      c1_i = float(c1_i); c1_f = float(c1_f); grid_1 = int(grid_1)
   #---------------------------  
   if (tipo == 1 and esc == 3):
      print(f'eixo-{ch1} --------------------------------------------')
      c1_i = input (f'Coordenada_fixa_{ch1}: '); c1_i = float(c1_i)
      c1_f = c1_i; grid_1 = 1
   #---------------------------    
   print(" ")

   if ((tipo == 1 and esc != 2) or (tipo == 2)):
      print(f'eixo-{ch2} --------------------------------------------')
      c2_i, c2_f, grid_2 = input (f'{ch2}_inicial {ch2}_final Grid_pontos: ').split()
      c2_i = float(c2_i); c2_f = float(c2_f); grid_2 = int(grid_2)
   #---------------------------    
   if (tipo == 1 and esc == 2):
      print(f'eixo-{ch2} --------------------------------------------')
      c2_i = input (f'Coordenada_fixa_{ch2}: '); c2_i = float(c2_i)
      c2_f = c2_i; grid_2 = 1
   #---------------------------    
   print(" ")

   if ((tipo == 1 and esc != 1) or (tipo == 2)):
      print(f'eixo-{ch3} --------------------------------------------')
      c3_i, c3_f, grid_3 = input (f'{ch3}_inicial {ch3}_final Grid_pontos: ').split()
      c3_i = float(c3_i); c3_f = float(c3_f); grid_3 = int(grid_3)
   #---------------------------    
   if (tipo == 1 and esc == 1):
      print(f'eixo-{ch3} --------------------------------------------')
      c3_i = input (f'Coordenada_fixa_{ch3}: '); c3_i = float(c3_i)
      c3_f = c3_i; grid_3 = 1
   #---------------------------    
   print(" ")

#============================================================================================
# Obtendo os limites do Plano 2D ou da Malha 3D de acordo com a escolha do ponto central: ---
#============================================================================================

if (point == 0):
   
   print("----------------------------------------------------")
   print(f'Digite as coordenadas ({ch1}, {ch2}, {ch3}) do ponto central: ')
   pc_1, pc_2, pc_3 = input (f'ponto central ({ch1} {ch2} {ch3}): ').split()
   pc_1 = float(pc_1); pc_2 = float(pc_2); pc_3 = float(pc_3)
   print(" ")

   print("----------------------------------------------------")
   print("Para cada eixo, digite o comprimento a ser varrido  ")
   print("neste eixo, bem como o Grid de pontos-k a ser usado ")
   print("----------------------------------------------------")   
   print("Utilize um numero IMPAR para o Grid de pontos-k ----")
   print("----------------------------------------------------")
   print(" ")
   
   if ((tipo == 1 and (esc == 1 or esc == 2)) or tipo == 2):
      print(f'eixo-{ch1} ----------------------------------------')
      comp_1, grid_1 = input (f'comprimento Grid_pontos: ').split()
      comp_1 = float(comp_1); grid_1 = int(grid_1)
      print(" ")

   if ((tipo == 1 and (esc == 1 or esc == 3)) or tipo == 2):
      print(f'eixo-{ch2} ----------------------------------------')
      comp_2, grid_2 = input (f'comprimento Grid_pontos: ').split()
      comp_2 = float(comp_2); grid_2 = int(grid_2)
      print(" ")

   if ((tipo == 1 and (esc == 2 or esc == 3)) or tipo == 2):
      print(f'eixo-{ch3} ----------------------------------------')
      comp_3, grid_3 = input (f'comprimento Grid_pontos: ').split()
      comp_3 = float(comp_3); grid_3 = int(grid_3)
      print(" ")

   if (tipo == 1 and esc == 1):
      grid_3 = 1; comp_3 = 0.0
   if (tipo == 1 and esc == 2):
      grid_2 = 1; comp_2 = 0.0
   if (tipo == 1 and esc == 3):
      grid_1 = 1; comp_1 = 0.0

   #----------------------------------------------------

   resto1 = (grid_1 % 2)
   resto2 = (grid_2 % 2)
   resto3 = (grid_3 % 2)
   
   if (resto1 == 0): grid_1 = grid_1 + 1
   if (resto2 == 0): grid_2 = grid_2 + 1
   if (resto3 == 0): grid_3 = grid_3 + 1 

   #----------------------------------------------------

   c1_i = pc_1 - (comp_1/2); c1_f = pc_1 + (comp_1/2)
   c2_i = pc_2 - (comp_2/2); c2_f = pc_2 + (comp_2/2)
   c3_i = pc_3 - (comp_3/2); c3_f = pc_3 + (comp_3/2)

#=========================================================================
# Inicialização dos vetores k1, k2 e k3 ----------------------------------
#=========================================================================

c1 = [0]*(grid_1 + 1)
c2 = [0]*(grid_2 + 1)
c3 = [0]*(grid_3 + 1)
number_pk = 0

#=========================================================================
# Obtenção da ordem do Loop e da escrita dos pontos-k no arquivo KPOINTS =
#=========================================================================

# Plano 2D na ZB =========================================================

if (tipo == 1 and estrutura == 1):

   if (esc == 1):
      grid_e1 = grid_1
      grid_e2 = grid_2

   if (esc == 2):
      grid_e1 = grid_1
      grid_e2 = grid_3
   
   if (esc == 3):
      grid_e1 = grid_2
      grid_e2 = grid_3

# Malha 3D na ZB =========================================================

if (tipo == 2 and estrutura == 1):

   c_e = 1
   grid_e1 = grid_1
   grid_e2 = grid_2
   grid_e3 = grid_3

   if (grid_2 > grid_e1):
      c_e = 2
      grid_e1 = grid_2
      grid_e2 = grid_1
      grid_e3 = grid_3
   
   if (grid_3 > grid_e1):
      c_e = 3
      grid_e1 = grid_3
      grid_e2 = grid_1
      grid_e3 = grid_2

#=========================================================================
# Escrita do arquivo KPOINTS ---------------------------------------------
#=========================================================================

#-------------------------------------------------
kpoints = open(dir_files + '/output/KPOINTS', 'w')
#-------------------------------------------------

if (tipo == 1):
   n_tipo = 'Plano_2D VASProcar'
if (tipo == 2):
   n_tipo = 'Malha_3D VASProcar'

if (coord == 1):
   kpoints.write(f'K_POINTS crystal_b  ! {n_tipo}  ({grid_1*grid_2*grid_3} pontos-k) \n')
if (coord == 2):
   kpoints.write(f'K_POINTS tpiba_b  ! {n_tipo}  ({grid_1*grid_2*grid_3} pontos-k) \n' )
   
# Plano 2D na ZB (modo de linha) =========================================

if (tipo == 1 and estrutura == 1):

   for i in range (1,(grid_e2+1)):

       number_pk += 2      

       if (tipo == 1 and esc == 1):
          #----------------------------------------------
          c2[i] = c2_i + (i-1)*(c2_f - c2_i)/(grid_2 - 1)
          c3_fixo = c3_i
          #----------------------------------------------
          kpoints.write(f'{c1_i:17.12f} {c2[i]:17.12f} {c3_fixo:17.12f}   {grid_e1 -1} \n')
          kpoints.write(f'{c1_f:17.12f} {c2[i]:17.12f} {c3_fixo:17.12f}   1 \n')

       if (tipo == 1 and esc == 2):
          #----------------------------------------------
          c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
          c2_fixo = c2_i
          #----------------------------------------------            
          kpoints.write(f'{c1_i:17.12f} {c2_fixo:17.12f} {c3[i]:17.12f}   {grid_e1 -1} \n')
          kpoints.write(f'{c1_f:17.12f} {c2_fixo:17.12f} {c3[i]:17.12f}   1 \n')

       if (tipo == 1 and esc == 3):
          #----------------------------------------------
          c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
          c1_fixo = c1_i
          #----------------------------------------------            
          kpoints.write(f'{c1_fixo:17.12f} {c2_i:17.12f} {c3[i]:17.12f}   {grid_e1 -1} \n')
          kpoints.write(f'{c1_fixo:17.12f} {c2_f:17.12f} {c3[i]:17.12f}   1 \n')

# Malha 3D na ZB (modo de linha) =========================================

if (tipo == 2 and estrutura == 1):

   for i in range (1,(grid_e2+1)):
       for j in range (1,(grid_e3+1)):

           number_pk += 2

           if (c_e == 1):
              #----------------------------------------------
              c2[i] = c2_i + (i-1)*(c2_f - c2_i)/(grid_2 - 1)
              c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
              #----------------------------------------------
              kpoints.write(f'{c1_i:17.12f} {c2[i]:17.12f} {c3[j]:17.12f}   {grid_e1 -1} \n')
              kpoints.write(f'{c1_f:17.12f} {c2[i]:17.12f} {c3[j]:17.12f}   1 \n')

           if (c_e == 2):
              #----------------------------------------------
              c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
              c3[j] = c3_i + (j-1)*(c3_f - c3_i)/(grid_3 - 1)
              #----------------------------------------------            
              kpoints.write(f'{c1[i]:17.12f} {c2_i:17.12f} {c3[j]:17.12f}   {grid_e1 -1} \n')
              kpoints.write(f'{c1[i]:17.12f} {c2_f:17.12f} {c3[j]:17.12f}   1 \n')

           if (c_e == 3):
              #----------------------------------------------
              c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
              c2[j] = c2_i + (j-1)*(c2_f - c2_i)/(grid_2 - 1)
              #----------------------------------------------            
              kpoints.write(f'{c1[i]:17.12f} {c2[j]:17.12f} {c3_i:17.12f}   {grid_e1 -1} \n')
              kpoints.write(f'{c1[i]:17.12f} {c2[j]:17.12f} {c3_f:17.12f}   1 \n')

# Escrita de cada ponto-k explicitamente no arquivo KPOINTS ==============

for i in range (1,(grid_1+1)):
    if (grid_1 > 1):
       c1[i] = c1_i + (i-1)*(c1_f - c1_i)/(grid_1 - 1)
    if (grid_1 == 1):
       c1[i] = c1_i
       
    for j in range (1,(grid_2+1)):
        if (grid_2 > 1):
           c2[j] = c2_i + (j-1)*(c2_f - c2_i)/(grid_2 - 1)
        if (grid_2 == 1):
           c2[j] = c2_i    
     
        for k in range (1,(grid_3+1)):
            if (grid_3 > 1):
               c3[k] = c3_i + (k-1)*(c3_f - c3_i)/(grid_3 - 1)
            if (grid_3 == 1):
               c3[k] = c3_i   
            
            if (estrutura == 0):
               number_pk += 1
               kpoints.write(f'{c1[i]:17.12f} {c2[j]:17.12f} {c3[k]:17.12f}   1 \n')

#============================================================================================           

#--------------
kpoints.close()
#--------------

#============================================================================================
# Obtenção das coordenadas cartesianas (kx,ky,kz) dos pontos-k gerados no arquivo KPOINTS ---
#============================================================================================

if (n_scf_o != 0 and n_nscf_i != 0 and n_nscf_o != 0 and n_bands_i != 0): 
    
   if (coord == 1):
      #-------------------------------------------------------------------------
      pontos_k = open(dir_files + '/output/k-points_Coord_Cartesianas.txt', 'w')
      #-------------------------------------------------------------------------

      pontos_k.write(" \n")
      pontos_k.write("========================================================================================= \n")
      pontos_k.write("Pontos-k do arquivo KPOINTS em Coordenadas Cartesianas (kx,ky,kz) em função de 2pi/Param. \n")
      pontos_k.write("========================================================================================= \n")
      pontos_k.write(" \n")

      for i in range (1,(grid_1+1)):
          for j in range (1,(grid_2+1)):
              for k in range (1,(grid_3+1)):
                  Coord_X = ((c1[i]*B1x) + (c2[j]*B2x) + (c3[k]*B3x))
                  Coord_Y = ((c1[i]*B1y) + (c2[j]*B2y) + (c3[k]*B3y))
                  Coord_Z = ((c1[i]*B1z) + (c2[j]*B2z) + (c3[k]*B3z))
                  pontos_k.write(f'{Coord_X:17.12f} {Coord_Y:17.12f} {Coord_Z:17.12f} \n')  

      #---------------
      pontos_k.close()
      #---------------

#============================================================================================
# Inserindo o numero total de pontos-k escritos no arquivo KPOINTS --------------------------
#============================================================================================

file = open(dir_files + '/output/KPOINTS', 'r')
lines = file.readlines()
file.close()

linha = 1
lines.insert(linha, f'{number_pk} \n')

file = open(dir_files + '/output/KPOINTS', 'w')
file.writelines(lines)
file.close()

#============================================================================================
# Informando a quantidade de pontos-k que o arquivo KPOINTS fornece -------------------------
#============================================================================================

print("#######################################################")
print(f'# O arquivo KPOINTS gerado fornece {grid_1*grid_2*grid_3} pontos-k na ZB')
print("#######################################################")   

if (coord == 1):
   print("## Um arquivo com as coordenadas cartesianas dos === ##")
   print("## pontos do arquivo KPOINTS esta na pasta output == ##")
   print("#######################################################")

#---------------------------------------------------------------
print(" ")
print("======================= Concluido =====================")
#---------------------------------------------------------------

#=======================================================================
# User option to perform another calculation or finished the code ======
#=======================================================================
execute_python_file(filename = '_loop.py')
