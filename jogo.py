import random


# AQUI COMEÇA A BATALHA.PY
def batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):
    vidaInimigo = random.randint(100, 220) #vida inimigo
   
    while vidaInimigo > 0 and vidaJogador > 0:
        escolha = input("Deseja lutar (1) ou fugir (2)? ")
        print("")
       
        if escolha == '1':
            danoJogador = random.randint(10, 200)
            danoInimigo = random.randint(10, 100)
           
            if danoEspada > 0:
                danoJogador += danoEspada
                print("Sua espada causou dano extra!")
                print("")
            elif porcaoSono > 0:
                danoJogador += porcaoSono
                print("Você usou a poção do sono e derrou o guarda instantaneamente!")
                print("")
           
           
            vidaInimigo -= danoJogador
            vidaJogador -= max(danoInimigo - protecaoEscudo, 0)
           
            print(f"Você causou {danoJogador} de dano ao inimigo e recebeu {max(danoInimigo - protecaoEscudo, 0)} de dano.")
        elif escolha == '2':
            print("Você fugiu da batalha.")
            print("")
            break
        else:
            print("Escolha inválida.")
            print("")
           
    if vidaJogador <= 0:
        print("Você foi derrotado na batalha.")
        print("")
        return False
    else:
        print("Você venceu a batalha!")
        print("")
        moedas += random.randint(30, 50)
        print(f"Total de moedas: {moedas}")
        print("")
        return True


# AQUI COMEÇA A LOJA.PY
def loja(moedas):
    print("Bem-vindo à loja! Os itens disponíveis são:")
    print("-------------------------------------------")
    print("1. Espada - 50 moedas")
    print("2. Machado - 80 moedas")
    print("3. Escudo - 30 moedas")
    print("")
   
    danoEspada = 0
    pocaoSono = 0
    protecaoEscudo = 0
   
    while True:
        escolha = input("Digite o que quer comprar (ou '0' para sair): ")
        print("")
       # PREÇO DOS ITENS
        if escolha == '1':
            if moedas >= 50:
                moedas -= 50
                danoEspada = random.choice([30, 40])  # dano da espada
                print("Você comprou uma espada!")
                print("")
            else:
                print("Moedas insuficientes.")
                print("")
        elif escolha == '2':
            if moedas >= 80:
                moedas -= 80
                pocaoSono = 1000  # dano poçao
                print("Você comprou uma porção do sono!")
                print("")
            else:
                print("Moedas insuficientes.")
                print("")
        elif escolha == '3':
            if moedas >= 30:
                moedas -= 30
                protecaoEscudo = random.choice([50, 100])  
                print("Você comprou um escudo!")
                print("")
            else:
                print("Moedas insuficientes.")
                print("")
        elif escolha == '0':
            break
        else:
            print("Escolha inválida.")
            print("")
   
    return danoEspada, pocaoSono, protecaoEscudo


# AQUI COMEÇAA JOGABILIDADE.PY
def jogabilidade():
    moedas = random.randint(80, 100)
    vidaJogador = random.randint(200, 300)  # Defina a vida do jogador aqui
   
    guardasDerrotados = 0
    while True:
        print("O que você deseja fazer?")
        print("1. Entrar na loja")
        print("2. Lutar contra o guarda")
        escolha = input("Digite o número da opção desejada: ")
        print("")
       
        if escolha == '1':
            danoEspada, porcaoSono, protecaoEscudo = loja(moedas)  
        elif escolha == '2':
            if guardasDerrotados == 0:
                if batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):  
                    moedas += 30
                   
                    guardasDerrotados += 1
                    vidaJogador += random.randint(50, 80)  # Aumentar a vida depois da batalha
                    guarda1()
                else:
                    print("Jogo encerrado.")
                    break
            elif guardasDerrotados == 1:
                if batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):  
                    moedas += 30
                   
                    guardasDerrotados += 1
                    vidaJogador += random.randint(50, 80)
                    guarda2()
                else:
                    print("Jogo encerrado.")
                    break
            elif guardasDerrotados == 2:
                if batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):  
                    moedas += 30
                   
                    print("")
                    guardasDerrotados += 1
                    vidaJogador += random.randint(50, 80)  
                    guarda3()
                    print("Parabéns! Você derrotou todos os guardas e chegou ao seu destino final.")
                    print("")
                    break
                else:
                    print("Jogo encerrado.")
                    break
        else:
            print("Escolha inválida. Digite '1' para entrar na loja ou '2' para lutar.")
            print("")




def guarda1():
    print("COM AGILIDADE E FORÇA IMPECÁVEIS, VOCÊ TRIUNFOU SOBRE O GUARDA ")
    print("SOMBRIO, DEIXANDO UM RASTRO DE SUA BRAVURA EM SEU CAMINHO. SEU PODEROSO ")
    print("GOLPE E DETERMINAÇÃO SÃO ADMIRÁVEIS. AGORA, COM ESSA VITÓRIA FRESCA, ELE ")
    print("SEGUE EM FRENTE, OLHOS FIXOS NO PRÓXIMO DESAFIO. COM CADA INIMIGO ")
    print("DERROTADO, SUA CONFIANÇA CRESCENTE O GUIARÁ PARA A CONQUISTA DO ")
    print("SANTO BERÇO.")
    print("")
    print("-------------------------------------------------------")


def guarda2():
    print("COM UM GOLPE AUDACIOSO E PRECISO, VOCÊ DEIXOU O GUARDA SOMBRIO EM")
    print("BRILHO EM SEUS OLHOS MOSTRA SUA DETERMINAÇÃO INDOMÁVEL. COM PASSOS ")
    print("FIRMES, ELE SE PREPARA PARA O PRÓXIMO CONFRONTO, PROMETENDO QUE ")
    print("NENHUM OBSTÁCULO O DETENDRÁ. CADA ADVERSÁRIO CAÍDO É UM PASSO MAIS ")
    print("PRÓXIMO DE SUA CONQUISTA, E NADA IRÁ ABALAR A SUA RESOLUÇÃO DE TRIUNFAR.")
    print("")
    print("------------------------------------------------------------------------")


def guarda3():
    print(f"COM O ECO DE CADA GOLPE VITORIOSO AINDA NO AR, VOCÊ DEIXOU O ÚLTIMO ")
    print("GUARDA SOMBRIO PROSTRADO AO SEU PODER. UM MISTO DE EXAUSTÃO E TRIUNFO ")
    print("DANÇAVA EM SEU OLHAR, POIS ELE SABIA QUE A BATALHA FINAL ESTAVA PRÓXIMA.  ")
    print("AGORA, NO CORAÇÃO DO CASTELO, ELE ENTRA NA ARENA DE UM CONFLITO HÁ. ")
    print("MUITO ESPERADO, ONDE A DESTREZA SE ENCONTRA COM A MALDADE: O ")
    print("DERRADEIRO GUARDA QUE ANTECEDE O TEMÍVEL ANFITRIÃO.")
    print("")
   


# AQUI COMEÇA O ARQUIVO DO JOGO.PY


def jogo():
    print("Seja Bem-vindo!")
    print("---------------------------")
    nomePerso = input("Digite o nome do seu personagem: ")
    print("")
    print(f"Olá, {nomePerso}! Sua jornada começa agora.")
    print("")
    print(f"NAS TERRAS ANTIGAS DE ELDORIA, O AUDACIOSO GUERREIRO SIR {nomePerso} EMBARCOU EM UMA MISSÃO")
    print("ÉPICA: CHEGAR AO SINISTRO SANTO BERÇO E DERROTAR OS GUARDAS SOMBRIO PARA ACESSAR")
    print("SEU INTERIOR.")
    print("")
 
   









import random

# AQUI COMEÇA A BATALHA.PY
def batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):
    vidaInimigo = random.randint(100, 220) #vida inimigo
   
    while vidaInimigo > 0 and vidaJogador > 0:
        escolha = input("Deseja lutar (1) ou fugir (2)? ")
        print("")
       
        if escolha == '1':
            danoJogador = random.randint(10, 200)
            danoInimigo = random.randint(10, 100)
           
            if danoEspada > 0:
                danoJogador += danoEspada
                print("Sua espada causou dano extra!")
                print("")
            elif porcaoSono > 0:
                danoJogador += porcaoSono
                print("Você usou a poção do sono e derrou o guarda instantaneamente!")
                print("")
           
           
            vidaInimigo -= danoJogador
            vidaJogador -= max(danoInimigo - protecaoEscudo, 0)
           
            print(f"Você causou {danoJogador} de dano ao inimigo e recebeu {max(danoInimigo - protecaoEscudo, 0)} de dano.")
        elif escolha == '2':
            print("Você fugiu da batalha.")
            print("")
            break
        else:
            print("Escolha inválida.")
            print("")
           
    if vidaJogador <= 0:
        print("Você foi derrotado na batalha.")
        print("")
        return False
    else:
        print("Você venceu a batalha!")
        print("")
        moedas += random.randint(30, 50)
        print(f"Total de moedas: {moedas}")
        print("")
        return True

# AQUI COMEÇA A LOJA.PY
def loja(moedas):
    print("Bem-vindo à loja! Os itens disponíveis são:")
    print("-------------------------------------------")
    print("1. Espada - 50 moedas")
    print("2. Machado - 80 moedas")
    print("3. Escudo - 30 moedas")
    print("")
   
    danoEspada = 0
    pocaoSono = 0
    protecaoEscudo = 0
   
    while True:
        escolha = input("Digite o que quer comprar (ou '0' para sair): ")
        print("")
       # PREÇO DOS ITENS
        if escolha == '1':
            if moedas >= 50:
                moedas -= 50
                danoEspada = random.choice([30, 40])  # dano da espada
                print("Você comprou uma espada!")
                print("")
            else:
                print("Moedas insuficientes.")
                print("")
        elif escolha == '2':
            if moedas >= 80:
                moedas -= 80
                pocaoSono = 1000  # dano poçao
                print("Você comprou uma porção do sono!")
                print("")
            else:
                print("Moedas insuficientes.")
                print("")
        elif escolha == '3':
            if moedas >= 30:
                moedas -= 30
                protecaoEscudo = random.choice([50, 100])  
                print("Você comprou um escudo!")
                print("")
            else:
                print("Moedas insuficientes.")
                print("")
        elif escolha == '0':
            break
        else:
            print("Escolha inválida.")
            print("")
   
    return danoEspada, pocaoSono, protecaoEscudo

# AQUI COMEÇAA JOGABILIDADE.PY
def jogabilidade():
    moedas = random.randint(80, 100)
    vidaJogador = random.randint(200, 300)  # Defina a vida do jogador aqui
   
    guardasDerrotados = 0
    while True:
        print("O que você deseja fazer?")
        print("1. Entrar na loja")
        print("2. Lutar contra o guarda")
        escolha = input("Digite o número da opção desejada: ")
        print("")
       
        if escolha == '1':
            danoEspada, porcaoSono, protecaoEscudo = loja(moedas)  
        elif escolha == '2':
            if guardasDerrotados == 0:
                if batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):  
                    moedas += 30
                   
                    guardasDerrotados += 1
                    vidaJogador += random.randint(50, 80)  # Aumentar a vida depois da batalha
                    guarda1()
                else:
                    print("Jogo encerrado.")
                    break
            elif guardasDerrotados == 1:
                if batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):  
                    moedas += 30
                   
                    guardasDerrotados += 1
                    vidaJogador += random.randint(50, 80) 
                    guarda2()
                else:
                    print("Jogo encerrado.")
                    break
            elif guardasDerrotados == 2:
                if batalha(vidaJogador, moedas, danoEspada, porcaoSono, protecaoEscudo):  
                    moedas += 30
                   
                    print("")
                    guardasDerrotados += 1
                    vidaJogador += random.randint(50, 80)  
                    guarda3()
                    print("Parabéns! Você derrotou todos os guardas e chegou ao seu destino final.")
                    print("")
                    break
                else:
                    print("Jogo encerrado.")
                    break
        else:
            print("Escolha inválida. Digite '1' para entrar na loja ou '2' para lutar.")
            print("")


def guarda1():
    print("COM AGILIDADE E FORÇA IMPECÁVEIS, VOCÊ TRIUNFOU SOBRE O GUARDA ")
    print("SOMBRIO, DEIXANDO UM RASTRO DE SUA BRAVURA EM SEU CAMINHO. SEU PODEROSO ")
    print("GOLPE E DETERMINAÇÃO SÃO ADMIRÁVEIS. AGORA, COM ESSA VITÓRIA FRESCA, ELE ")
    print("SEGUE EM FRENTE, OLHOS FIXOS NO PRÓXIMO DESAFIO. COM CADA INIMIGO ")
    print("DERROTADO, SUA CONFIANÇA CRESCENTE O GUIARÁ PARA A CONQUISTA DO ")
    print("SANTO BERÇO.")
    print("")
    print("-------------------------------------------------------")

def guarda2():
    print("COM UM GOLPE AUDACIOSO E PRECISO, VOCÊ DEIXOU O GUARDA SOMBRIO EM")
    print("BRILHO EM SEUS OLHOS MOSTRA SUA DETERMINAÇÃO INDOMÁVEL. COM PASSOS ")
    print("FIRMES, ELE SE PREPARA PARA O PRÓXIMO CONFRONTO, PROMETENDO QUE ")
    print("NENHUM OBSTÁCULO O DETENDRÁ. CADA ADVERSÁRIO CAÍDO É UM PASSO MAIS ")
    print("PRÓXIMO DE SUA CONQUISTA, E NADA IRÁ ABALAR A SUA RESOLUÇÃO DE TRIUNFAR.")
    print("")
    print("------------------------------------------------------------------------")

def guarda3():
    print(f"COM O ECO DE CADA GOLPE VITORIOSO AINDA NO AR, VOCÊ DEIXOU O ÚLTIMO ")
    print("GUARDA SOMBRIO PROSTRADO AO SEU PODER. UM MISTO DE EXAUSTÃO E TRIUNFO ")
    print("DANÇAVA EM SEU OLHAR, POIS ELE SABIA QUE A BATALHA FINAL ESTAVA PRÓXIMA.  ")
    print("AGORA, NO CORAÇÃO DO CASTELO, ELE ENTRA NA ARENA DE UM CONFLITO HÁ. ")
    print("MUITO ESPERADO, ONDE A DESTREZA SE ENCONTRA COM A MALDADE: O ")
    print("DERRADEIRO GUARDA QUE ANTECEDE O TEMÍVEL ANFITRIÃO.")
    print("")
   

# AQUI COMEÇA O ARQUIVO DO JOGO.PY

def jogo():
    print("Seja Bem-vindo!")
    print("---------------------------")
    nomePerso = input("Digite o nome do seu personagem: ")
    print("")
    print(f"Olá, {nomePerso}! Sua jornada começa agora.")
    print("")
    print(f"NAS TERRAS ANTIGAS DE ELDORIA, O AUDACIOSO GUERREIRO SIR {nomePerso} EMBARCOU EM UMA MISSÃO")
    print("ÉPICA: CHEGAR AO SINISTRO SANTO BERÇO E DERROTAR OS GUARDAS SOMBRIO PARA ACESSAR")
    print("SEU INTERIOR.")
    print("")
  
    jogabilidade()







