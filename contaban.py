print ("--Seja bem vindo a sua conta bancária!-- \n") 
#definindo o primeiro menu para cadastro: 
print('MACK BANK - ESCOLHA UMA OPÇÃO:') 
print('(1) Cadastrar conta corrente') 
print('(2) Depositar') 
print('(3) Sacar') 
print('(4) Consultar saldo') 
print('(5) Consultar extrato') 
print('(6) Finalizar')
primeiraopcao = int(input('Sua opção: '))
bloqueio = 0
#definindo o menu para as demais opções:
def menu(): 
    print('MACK BANK - ESCOLHA UMA OPÇÃO:') 
    print('(1) Cadastrar conta corrente') 
    print('(2) Depositar') 
    print('(3) Sacar') 
    print('(4) Consultar saldo') 
    print('(5) Consultar extrato') 
    print('(6) Finalizar') 
    global opcao 
    opcao = int(input('Sua opção: ')) 
    while opcao < 1 or opcao > 6: 
        print('Opção Inválida! Digite um número entre 1 e 6.') 
        opcao = int(input('Sua opção: '))
    while opcao == 1:
            print ("Conta já cadastrada! Escolha uma opção entre 2 e 6.")
            opcao =  int(input('Sua opção: '))
while bloqueio > 0 and 3 <= opcao <= 5:
        print('Você pode acessar apenas as opções 2 e 6, pois sua conta foi bloqueada.\n')
        opcao = int(input('Sua opção: '))

     
#Parte 1 - Cadastro da conta (separado para que seja executada apenas uma vez)
while primeiraopcao != 1:
    print ('Opção Inválida! Você deve cadastrar sua conta primeiro, escolha opção 1 para cadastrar.')
    primeiraopcao = int(input('Sua opção: ')) 
if primeiraopcao == 1:
    print ("\nCADASTRO DE CONTA")
    import random
    n_conta = random.randint(1000,9999)
    print(f'O número da sua conta é {n_conta}')
    nome = input("Digite seu nome completo: ")
    while len(nome) == 0:
        print('Você não pode deixar este campo vazio!')
        nome = input("Digite seu nome completo: ")
    telefone = input('Digite seu telefone: ')
    while len(telefone) == 0:
        print('Você não pode deixar este campo vazio!')
        telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    while len(email) == 0:
        print('Você não pode deixar este campo vazio!')
        email = input('Digite seu email: ')
    #função extra: verificação de email válido
    while "@" not in email or '.com' not in email: 
        print('Digite um email válido!') 
        email = input('Digite seu email: ')
    saldo = float (input("Seu saldo inicial: R$")) 
    while saldo < 1000: 
        print('Saldo inválido! Seu saldo deve ser maior ou igual a R$1000.') 
        saldo = float (input("Digite seu saldo inicial: R$")) 
    limite = float (input("Seu limite de crédito: R$")) 
    while limite < 0: 
        print('Limite inválido! Seu limite deve ser maior ou igual a 0.') 
        limite = float (input("Digite seu limite de crédito: R$")) 
    senha = input("Digite sua senha(Lembre-se: Sua senha deve conter 6 caracteres): ") 
    while len (senha) != 6: 
        print ("Senha não permitida! Sua senha deve conter 6 caracteres.") 
        senha = input("Digite sua senha: ")
    conf_senha = input('Confirme sua senha: ') 
    while conf_senha != senha: 
         print("Senhas não correspondem!") 
         senha = input("Digite sua senha: ")
         while len (senha) != 6:
             print ("Senha não permitida! Sua senha deve conter 6 caracteres.") 
             senha = input("Digite sua senha: ")
         conf_senha = input('Confirme sua senha: ') 
    print('Cadastro realizado com sucesso! \n')
    menu()

 
  
 
listhistorico = [] 
#def pra adicionar a operação no historico 
def historico (): 
    item = nomeopcao+(str(operação)) 
    listhistorico.append (item)

#def para verificar conta e senha    
def verificação ():
    n_conta1 = int(input('Informe o número da conta: '))
    while n_conta1 != n_conta:
        print('Conta inválida! O número da conta deve ser o mesmo cadastrado anteriormente.')
        n_conta1 = int(input('Informe o número da conta: '))
    print('Nome do cliente:', nome)
    senha1 = input("Digite sua senha: ")
    contadora = 0
    while senha1 != senha and contadora < 2:
        print ("O valor digitado não corresponde a sua senha!")
        senha1 = input("Digite sua senha: ")
        contadora += 1
        if senha1 != senha:
            print('Por digitar a senha incorreta 3 vezes, sua conta foi bloqueada.')
            bloqueio += 1
            menu()


#Parte 2 - Depósito
while 2 <= opcao <= 6: 
    if opcao == 2: 
        print('\nDEPÓSITO NA CONTA')
        n_conta1 = int(input('Informe o número da conta: '))
        while n_conta1 != n_conta:
            print('Conta inválida! O número da conta deve ser o mesmo cadastrado anteriormente.')
            n_conta1 = int(input('Informe o número da conta: '))
        print('Nome do cliente:', nome)
        operação = float (input("Digite a quantia a ser depositada: R$"))
        while operação <= 0:
            print('Valor inválido! A quantia deve ser maior que zero.')
            operação = float (input("Digite a quantia a ser depositada: R$"))
        saldo = saldo + operação 
        nomeopcao = "Depósito de: R$" 
        historico () 
        print ("OPERAÇÃO REALIZADA COM SUCESSO! \n") 
        menu () 
 
#Parte 3 - Saque 
    if opcao == 3:
        print ('\nSAQUE DA CONTA')
        verificação() 
        quantia = float (input("Digite o valor que deseja sacar: R$"))
        while quantia <= 0:
            print('Valor inválido! A quantia deve ser maior que zero.')
            quantia = float (input("Digite o valor que deseja sacar: R$"))
        nomeopcao = "Saque de: R$" 
        #verifica se tem o valor no saldo da conta ou tem limite 
        if quantia <= saldo: 
            saldo = saldo - quantia 
            operação = quantia 
            historico () 
            print ("OPERAÇÃO REALIZADA COM SUCESSO! \n") 
        elif saldo == 0: 
            limite = limite - quantia 
            operação = quantia 
            historico ()
            print('VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
            print ("OPERAÇÃO REALIZADA COM SUCESSO! \n") 
        #quantia saindo uma parte do saldo e uma do limite 
        elif quantia > saldo and (quantia-saldo) <= limite: 
            saldo = saldo - quantia 
            limite = limite + saldo 
            operação = quantia 
            historico ()
            print('VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
            print ("OPERAÇÃO REALIZADA COM SUCESSO! \n") 
        else: 
            print ("Transação negada: saldo ou limite insuficiente \n") 
        menu () 
#Parte 4 - Consulta de saldo 
    if opcao == 4:
        print ('\nCONSULTA DE SALDO')
        verificação ()
        print (f'Seu saldo atual é: R${saldo: .2f}')
        print (f'Seu limite de crédito atual é: R${limite: .2f} \n')
        menu()

#Parte 5 - Consulta do extrato
    if opcao == 5:
        print ('\nCONSULTA DE EXTRATO')
        verificação ()
        print (f'LIMITE DE CRÉDITO: R${limite: .2f}')
        print ("ÚLTIMAS OPERAÇÕES:")
        print (*listhistorico, sep = "\n")
        print (f'SALDO EM CONTA: R${saldo: .2f}\n')
        if saldo < 0:
            print('Atenção ao seu saldo!')
            print('\n')
        menu ()
 
    if opcao == 6: 
        print ("MACK BANK – SOBRE \nEste programa foi desenvolvido por \nLívia Novais \nAdrielle Moreira"
) 
        break