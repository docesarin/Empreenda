# não sei onde fiz esse codigo, então vou fazer de novo kkkk

meta = int(input("Qual sua meta? "))
tempo = int(input("Em quantos meses deseja? "))
produto = input("Qual o nome do seu produto? ")
valorProduto = int(input("Qual o valor do seu produto? "))


qntMes = meta / tempo 
qntProduto = qntMes / valorProduto

if tempo <= 1:
    qntMes = meta / 25 

    print(f"Você precisa vender {qntProduto} R$ em 25 dias, vendendo {qntMes} unidades de {produto} por dia.")
else: 

    print(f"Você precisa vender {qntProduto} R$ por mês em {tempo} meses, vendendo {qntMes} unidades de {produto} em um mês")



