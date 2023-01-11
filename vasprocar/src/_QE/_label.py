# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

#===============================================================================
# Copiando a imagem contendo a lista do Alfabeto Grego para a pasta de saida ===
#===============================================================================

if (dest_k == 2):
   source = main_dir + '/etc/Greek_alphabet.jpg'
   destination = dir_files + '/output/Greek_alphabet.jpg'
   shutil.copyfile(source, destination)

#======================================================================
# Mensagem de aviso para o usuario editar o arquivo KPOINTS ===========
#======================================================================

if (n_procar == 1 and dest_k == 2):

   #=======================================================================
   # Obtendo o nº de pontos-k a serem destacados na estrutura de Bandas ===
   #=======================================================================

   print("")
   print ("=============================================================================================")
   print ("Atencao: Edite o arquivo nscf.in, inserindo o rotulo desejado nos pontos-k do arquivo.       ")
   print ("         !!!! Todos os pontos-k presentes no arquivo nscf.in, devem ser rotulados !!!!       ")
   print ("=============================================================================================")
   print ("Exemplo:                                                                                     ")
   print ("         K_POINTS crystal_b                                                                  ")
   print ("         6                                                                                   ")
   print ("         0.375 0.375 0.750 100  K                                                            ")
   print ("         0.000 0.000 0.000 100  #1 (Gamma)                                                   ")
   print ("         0.500 0.500 0.500 100  L                                                            ")
   print ("         0.500 0.000 0.500 100  X                                                            ")
   print ("         0.500 0.250 0.750 100  W                                                            ")
   print ("         0.375 0.375 0.750 1    K                                                            ")
   print ("=============================================================================================")
   print ("Utilize os seguintes codigos (#number) para a utilizacao de simbolos Gregos como rotulos     ")
   print ("                                                                                             ")
   print ("#1  = Gamma       |  #2  = gamma        |  #3  = Delta     |  #4  = delta       |               ")
   print ("#5  = Lambda      |  #6  = lambda       |  #7  = Sigma     |  #8  = sigma       |               ")
   print ("#9  = Theta       |  #10 = tetha        |  #11 = Omega     |  #12 = omega       |               ")
   print ("#13 = Psi         |  #14 = psi          |  #15 = Phi       |  #16 = phi         |  #17 = varphi ")
   print ("#18 = alfa        |  #19 = beta         |  #20 = pi        |  #21 = rho         |               ")
   print ("#22 = tau         |  #23 = upsilon      |  #24 = mu        |  #25 = nu          |               ")
   print ("#26 = epsilon     |  #27 = eta          |  #28 = kappa     |  #29 = xi          |  #30 = zeta   ")
   print ("#31 = left_arrow  |  #32 = right_arrow  |  #33 = up_arrow  |  #34 = down_arrow  |               ")
   print ("=============================================================================================")
   print ("Apos editar o arquivo nscf.in, aperte [ENTER] para continuar                                 ")
   print ("=============================================================================================")
   confirmacao = input (" "); confirmacao = str(confirmacao)       

#===================================================================================

number = 0
contador2 = 0
n_pk = []     # Vetor formado pelos indices dos pontos-k selecionados
dest_pk = []  # Vetor formado pelas coordenadas no eixo-x do plot dos pontos-k selecionados
label_pk = [] # Vetor formado pelas rótulos dos pontos-k selecionados
symmetry_pk = [] # Vetor formado pelas simetrias dos pontos-k selecionados
kx_pk = []; ky_pk = []; kz_pk = []  # Coordenadas diretas (k1, k2, k3) dos pontos-k selecionados

#------------------------------------------
kpoints = open(dir_files + '/nscf.in', "r")
#------------------------------------------                      

for line in kpoints:   
    if 'K_POINTS' in line: 
       break

VTemp = kpoints.readline()
passo = int(VTemp)

for i in range(passo):
    #---------------------------------
    VTemp = kpoints.readline().split()
    #---------------------------------
    if (dest_k == 2 and n_procar == 1):
       label_pk.append(str(VTemp[4]))
    #---------------------------------------
    k_point = number + 1
    n_pk.append(k_point)
    dest_pk.append(separacao[1][k_point])
    symmetry_pk.append(symmetry[1][k_point])
    #---------------------------------------
    kx_pk.append(kx[wp][k_point]/fator_zb)
    ky_pk.append(ky[wp][k_point]/fator_zb)
    kz_pk.append(kz[wp][k_point]/fator_zb)
    #-------------------------------------
    number = number + int(VTemp[3])

contador2 = len(dest_pk)

#--------------
kpoints.close()
#--------------
   


#======================================================================
# Gerando o arquivo label.txt =========================================
#======================================================================

if (dest_k == 2):

   #-------------------------------------------------
   label = open(dir_files + '/output/label.txt', "w")
   #-------------------------------------------------

   if (n_procar > 1):
       label.write(f'{contador2}                     ! Numero de pontos-k a serem rotulados \n')

# Criando uma lista com as letras de a-z ==============================

   lab = []

   for i in range(ord('a'), ord('z') + 1): # lista as letras de a-z
       lab.append(chr(i))
       

#======================================================================

   if (n_procar > 1):
      for i in range (contador2):
          label.write(f'{dest_pk[i]:<18,.14f} {lab[i]}  ! Point-k {n_pk[i]:<4}  ({kx_pk[i]}, {ky_pk[i]}, {kz_pk[i]}) \n')

#======================================================================

   if (n_procar > 1):
      label.write(f' \n')
      label.write(f'Na edicao deste arquivo, vc pode alterar o número de pontos-k a serem rotulados. \n')
      label.write(f'As coordenadas (kx,ky,kz) de cada ponto-k podem ser verificadas no arquivo output/informacoes.txt \n')
      
   label.write(f' \n')
   label.write(f'===================================================================================================== \n')
   label.write(f'Para inserir simbolos gregos como rotulo dos pontos-k, utilize os codigos (#number) abaixo:           \n')
   label.write(f'===================================================================================================== \n')
   label.write(f' \n')
   label.write("#1  = Gamma       |  #2  = gamma        |  #3  = Delta     |  #4  = delta       |               \n") 
   label.write("#5  = Lambda      |  #6  = lambda       |  #7  = Sigma     |  #8  = sigma       |               \n") 
   label.write("#9  = Theta       |  #10 = tetha        |  #11 = Omega     |  #12 = omega       |               \n") 
   label.write("#13 = Psi         |  #14 = psi          |  #15 = Phi       |  #16 = phi         |  #17 = varphi \n") 
   label.write("#18 = alfa        |  #19 = beta         |  #20 = pi        |  #21 = rho         |               \n") 
   label.write("#22 = tau         |  #23 = upsilon      |  #24 = mu        |  #25 = nu          |               \n") 
   label.write("#26 = epsilon     |  #27 = eta          |  #28 = kappa     |  #29 = xi          |  #30 = zeta   \n")
   label.write("#31 = left_arrow  |  #32 = right_arrow  |  #33 = up_arrow  |  #34 = down_arrow  |               \n") 
   label.write(f' \n')

   #------------
   label.close()
   #------------



#======================================================================
# Mensagem de aviso para o usuario editar o arquivo label.txt =========
#======================================================================

if (dest_k == 2 and n_procar > 1):
   print (" ")
   print ("################################################################")
   print ("Atencao: Edite o rotulo dos pontos-k no arquivo label.txt       ") 
   print ("         Apos a edicao, confirme apertando o botao [ENTER]      ")
   print ("================================================================")
   print ("Consulte as coordenadas dos pontos-k no arquivo informacoes.txt ")
   print ("################################################################")
   confirmacao = input (" "); confirmacao = str(confirmacao)

   #======================================================================
   # Leitura do arquivo label.txt para a obtencao dos rotulos dos pontos-k
   #======================================================================

   #-------------------------------------------------
   label = open(dir_files + '/output/label.txt', "r")
   #-------------------------------------------------

   VTemp = label.readline().split()
   contador2 = int(VTemp[0])

   dest_pk = []
   label_pk = []

   for i in range(contador2):
       VTemp = label.readline().split()
       dest_pk.append(float(VTemp[0]))
       label_pk.append(str(VTemp[1]))

   #------------
   label.close()
   #------------



#======================================================================
# Definindo as correspondentes nomenclaturas para o GRACE e Matplotlib
#======================================================================

if (dest_k == 2):

   r_grace = []

   r_grace.append('\\f{Symbol}G');     r_grace.append('\\f{Symbol}g');     r_grace.append('\\f{Symbol}D')
   r_grace.append('\\f{Symbol}d');     r_grace.append('\\f{Symbol}L');     r_grace.append('\\f{Symbol}l')
   r_grace.append('\\f{Symbol}S');     r_grace.append('\\f{Symbol}s');     r_grace.append('\\f{Symbol}Q')
   r_grace.append('\\f{Symbol}q');     r_grace.append('\\f{Symbol}W');     r_grace.append('\\f{Symbol}w') 
   r_grace.append('\\f{Symbol}Y');     r_grace.append('\\f{Symbol}y');     r_grace.append('\\f{Symbol}F')
   r_grace.append('\\f{Symbol}f');     r_grace.append('\\f{Symbol}j');     r_grace.append('\\f{Symbol}a')
   r_grace.append('\\f{Symbol}b');     r_grace.append('\\f{Symbol}p');     r_grace.append('\\f{Symbol}r') 
   r_grace.append('\\f{Symbol}t');     r_grace.append('\\f{Symbol}u');     r_grace.append('\\f{Symbol}m')
   r_grace.append('\\f{Symbol}n');     r_grace.append('\\f{Symbol}e');     r_grace.append('\\f{Symbol}h')
   r_grace.append('\\f{Symbol}k');     r_grace.append('\\f{Symbol}x');     r_grace.append('\\f{Symbol}z')
   r_grace.append('\\f{Symbol}\c,\C'); r_grace.append('\\f{Symbol}\c.\C'); r_grace.append('\\f{Symbol}\c-\C');  r_grace.append('\\f{Symbol}\c/\C')

   #======================================================================

   r_matplot = []

   r_matplot.append('${\\Gamma}$');     r_matplot.append('${\\gamma}$');      r_matplot.append('${\\Delta}$')
   r_matplot.append('${\\delta}$');     r_matplot.append('${\\Lambda}$');     r_matplot.append('${\\lambda}$')
   r_matplot.append('${\\Sigma}$');     r_matplot.append('${\\sigma}$');      r_matplot.append('${\\Theta}$')
   r_matplot.append('${\\theta}$');     r_matplot.append('${\\Omega}$');      r_matplot.append('${\\omega}$') 
   r_matplot.append('${\\Psi}$');       r_matplot.append('${\\psi}$');        r_matplot.append('${\\Phi}$')
   r_matplot.append('${\\phi}$');       r_matplot.append('${\\varphi}$');     r_matplot.append('${\\alpha}$')
   r_matplot.append('${\\beta}$');      r_matplot.append('${\\pi}$');         r_matplot.append('${\\rho}$') 
   r_matplot.append('${\\tau}$');       r_matplot.append('${\\upsilon}$');    r_matplot.append('${\\mu}$')
   r_matplot.append('${\\nu}$');        r_matplot.append('${\\epsilon}$');    r_matplot.append('${\\eta}$')
   r_matplot.append('${\\kappa}$');     r_matplot.append('${\\xi}$');         r_matplot.append('${\\zeta}$')
   r_matplot.append('${\\leftarrow}$'); r_matplot.append('${\\rightarrow}$'); r_matplot.append('${\\uparrow}$');  r_matplot.append('${\\downarrow}$')

   #======================================================================
