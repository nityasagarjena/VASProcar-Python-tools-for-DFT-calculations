
#----------------------------------------------------------------------
# Cores utilizadas no plot das Projeções: (GRACE) ---------------------
#----------------------------------------------------------------------

# Obs.: Codigo das cores
# Branco  = 0,  Preto = 1, Vermelho = 2,  Verde   = 3,  Azul   = 4,  Amarelo = 5,  Marrom   = 6, Cinza = 7
# Violeta = 8,  Cyan  = 9, Magenta  = 10, Laranja = 11, Indigo = 12, Marron  = 13, Turquesa = 14
                                                                        
cor_spin = [1]*4   # Inicialização do vetor cor_spin
cor_orb  = [1]*12  # Inicialização do vetor cor_orb

                   # Valores padrão:
                   #------------------------------------------
cor_spin[1] = 1    # Cor da componente Nula do Spin (Preto)            
cor_spin[2] = 2    # Cor da componente Up do Spin   (Vermelho)         
cor_spin[3] = 4    # Cor da componente Down do Spin (Azul)
                   #------------------------------------------
cor_orb[1]  = 4    # Cor do Orbital S   (Azul)
cor_orb[2]  = 2    # Cor do Orbital P   (Vermelho)
cor_orb[3]  = 3    # Cor do Orbital D   (Verde)
cor_orb[4]  = 4    # Cor do Orbital Px  (Azul)
cor_orb[5]  = 2    # Cor do Orbital Py  (Vermelho)
cor_orb[6]  = 3    # Cor do Orbital Pz  (Verde)
cor_orb[7]  = 4    # Cor do Orbital Dxy (Azul)
cor_orb[8]  = 2    # Cor do Orbital Dyz (Vermelho)
cor_orb[9]  = 3    # Cor do Orbital Dz2 (Verde)
cor_orb[10] = 6    # Cor do Orbital Dxz (Marrom)
cor_orb[11] = 10   # Cor do Orbital Dx2 (Magenta)
                   #------------------------------------------
cor_A  = 4         # Cor da Região A (Azul)
cor_B  = 2         # Cor da Região B (Vermelho)
cor_C  = 3         # Cor da Região C (Verde)
cor_D  = 6         # Cor da Região D (Marrom)
cor_E  = 10        # Cor da Região E (Magenta)

#----------------------------------------------------------------------
# Dimensoes que definem as proporcões dos gráficos 2D: (GRACE) --------
#----------------------------------------------------------------------
                   # Valores padrão:
fig_xmin = 0.12    # 0.12
fig_xmax = 0.82    # 0.82
fig_ymin = 0.075   # 0.075
fig_ymax = 0.95    # 0.95
