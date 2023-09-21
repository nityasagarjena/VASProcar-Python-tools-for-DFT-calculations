# VASProcar Copyright (C) 2023
# GNU GPL-3.0 license

print("===========================")
print("Analisando os pontos-k ====")
print("===========================")
print(" ")
  
#######################################################################
########################## Loop dos Pontos_k ##########################
#######################################################################

# nb = 38
# nk = 501

#============================================

print('Analisando o arquivo {filband}')
print("------------------------------")

#-------------------------------------------
bands = open(dir_files + '/' + filband, "r")
#-------------------------------------------
       
temp = 1.0; number = 0

VTemp = bands.readline()

for point_k in range(1, (nk+1)):                                  

    #--------------------------------------------------------------
    # Calculando a porcentagem de leitura do filband_file ---------
    #--------------------------------------------------------------

    porc = (point_k/nk)*100        

    if (porc >= temp):
       print(f'Processado {porc:>3,.0f}%')                 
       number += 1
       if (number == 1):
          temp = 10.0
       if (number == 2):
          temp = 25.0
       if (number >= 3):
          temp = temp + 25.0
          
    VTemp = bands.readline().split()
    kx = float(VTemp[0])
    ky = float(VTemp[1])
    kz = float(VTemp[2])

    #----------------------------------------------------------------
    # Teste para verificar a variacao das coordenadas kx, ky e kz ---
    #----------------------------------------------------------------

    if (point_k == 1):
       kx_i = kx; ky_i = ky; kz_i = kz         
       dk = [0]*6

    if (point_k != 1):
       #---------------------------------
       if (kx != kx_i): dk[3] = 1
       if (ky != ky_i): dk[4] = 1
       if (kz != kz_i): dk[5] = 1

    #----------------------------------------
    passo1 = (nb/10)
    resto = passo1 - int(passo1)
    if (resto == 0): passo1 = int(passo1)
    if (resto != 0): passo1 = int(passo1) + 1

    for i in range (passo1):
        VTemp = bands.readline()
    #----------------------------------------
         
#-------------
bands.close()
#-------------

print(dk)

#######################################################################
###################### Fim do Loop dos pontos-k #######################
#######################################################################

print(" ")
