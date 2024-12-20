# quantos preciso vender por mês para alcançar a meta
# somaProdutos * quantidadeQueFalta = meta

# minha meta é ter o ticket medio de 20 reais por pessoa, com no minimo 50 pessoas por dia
# ticketMedio * clientes = saldoDiario
# saldoDiario * 25 = saldoMensal

# config empresa

# nome empresa
# media clientes diario
# meta
# cadastrar produtos
# ticketMedio??? não sei se isso eu botaria
# gastos  


def config():

    empresa = "None"
    mediaDiaria = 0
    meta = 0

    print("Configurações......")
    print("")
    print("Nome Atual: ", empresa)
    print("Media diaria de clientes: ", mediaDiaria)
    print("Meta mensal :", meta)
    print("")



    print("1 - Definir nome da empresa")
    print("1 - Definir Media de clientes")


    empresa = input("Qual o nome da empresa? ")
    mediaDiaria = int(input("Qual a media de clientes diarios? "))
    meta = int(input("Qual a meta mensal? "))
    
    metaDiaria = (meta / 25)

    resp = input("Cadastro de prdutos")