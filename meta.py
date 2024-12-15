meta = int(input("Qual a sua meta mensal? "))
dds = int(input("Quantos dias de trabalho mensal você vai ter? (25: padrão sem os domingos) "))

metaDiaria = meta / dds

print(f"Sua meta diaria é {metaDiaria} que multiplicando por {dds} dias, ao final do mês você atinge {meta}!")