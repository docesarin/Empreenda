# now on linux b1tch3s

meta = int(input("Qual a sua meta mensal em reais? "))
totalProdutos = int(input("No total, quantos produtos você vende? "))

produtos = []
valores = []

for i in range(totalProdutos):
    produto = input("Digite o nome do produto: ")
    valor = float(input("Qual o valor desse produto: "))

    produtos.append(produto)
    valores.append(valor)

somaProdutos = sum(valores)

print("Se você vender uma unidade de cada produto terá ", somaProdutos)
print("Tirando os domingos, seu mês terá em media 25 dias, e você fará ", somaProdutos * 25, " por mês.")


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
