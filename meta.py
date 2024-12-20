# github.com/docesarin

print("===========================================")
print("       CALCULADORA DE META MENSAL          ")
print("===========================================")

# Solicitar a meta mensal
meta = int(input("Digite sua meta mensal (em R$): "))
metaDiaria = meta / 25  # Supondo 25 dias úteis no mês

# Solicitar a quantidade de produtos
qp = int(input("Quantos produtos você vende? "))

produtos = []
valores = []
qpi = []
metaIndividual = metaDiaria / qp

# Loop para coletar dados dos produtos
print("\nAgora, vamos registrar os produtos e seus respectivos preços:")
for i in range(qp):
    p = input(f"\nDigite o nome do {i+1}º produto: ")  # Melhor mensagem para o usuário
    v = float(input(f"Digite o valor do {i+1}º produto (em R$): "))  # Melhor mensagem para o usuário

    produtos.append(p)
    valores.append(v)

    # Calcular a meta de unidades por produto para atingir a meta individual
    mi = metaIndividual / v
    qpi.append(mi)

# Exibir a necessidade de vendas por produto
print("\n===========================================")
print("      RESUMO DE VENDAS NECESSÁRIAS         ")
print("===========================================")
for i in range(qp):
    print(f"Para atingir sua meta diária de R${metaIndividual:.2f}, você precisa vender {qpi[i]:.2f} unidades do produto '{produtos[i]}' por dia.")

# Exibir resumo final
print("\n===========================================")
print(f"RESUMO FINAL:")
print("===========================================")
print(f"Meta Mensal: R${meta}")
print(f"Meta Diária: R${metaDiaria:.2f}")
print(f"Com base em {qp} produtos, sua meta diária de vendas é dividida entre os produtos, considerando o preço de cada um.")
print("\n===========================================")
print("   Obrigado por usar a calculadora de metas!")
print("===========================================")
