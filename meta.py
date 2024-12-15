
# github.com/docesarin

meta = int(input("Digite sua meta mensal: "))

metaDiaria = meta/25

qp = int(input("Quantos produtos você vende?"))

produtos = []
valores = []
qpi = []
metaIndividual = metaDiaria / qp

for i in range(qp):
    p = str(input("Digite o nome do produto: "))
    v = float(input("Digite o valor do produto: "))

    produtos.append(p)
    valores.append(v)

    mi = metaIndividual/v
    qpi.append(mi)

    print("Você precisa vender ", qpi[i], " o ", p[i], " por dia. em 25 dias para fazer ", metaIndividual, " por dia, somando ", metaDiaria, " por dia, assim fazendo ", meta, " em 25 dias (media do mês tirando os domingos).")




