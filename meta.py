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