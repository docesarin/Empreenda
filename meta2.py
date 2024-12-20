def calcular_meta_personalizada():
    try:
        meta = float(input("Qual sua meta em reais? "))
        tempo = int(input("Em quantos meses deseja alcançar a meta? "))
        
        if tempo <= 0 or meta <= 0:
            print("A meta e o tempo devem ser maiores que zero.")
            return
        
        produtos = []
        pesos = []
        peso_total = 0

        while True:
            nome = input("Digite o nome do produto (ou pressione Enter para finalizar): ").strip()
            if not nome:
                break
            valor_unitario = float(input(f"Digite o valor unitário de {nome}: "))
            if valor_unitario <= 0:
                print("O valor do produto deve ser maior que zero. Tente novamente.")
                continue
            peso = float(input(f"Digite o peso percentual de contribuição de {nome} (ex: 50 para 50%): "))
            if peso <= 0:
                print("O peso deve ser maior que zero. Tente novamente.")
                continue
            
            produtos.append({"nome": nome, "valor": valor_unitario, "peso": peso})
            peso_total += peso
        
        if not produtos:
            print("Nenhum produto foi adicionado. O programa será encerrado.")
            return

        if peso_total != 100:
            print("A soma dos pesos deve ser igual a 100%. Tente novamente.")
            return
        
        dias_por_mes = 30
        total_necessario_diario = meta / (tempo * dias_por_mes)
        total_necessario_mensal = meta / tempo

        print("\nResumo do planejamento:")
        print(f"Meta total: R$ {meta:.2f}")
        print(f"Prazo: {tempo} meses ({tempo * dias_por_mes} dias)")
        print(f"Vendas mensais necessárias: R$ {total_necessario_mensal:.2f}")
        print(f"Vendas diárias necessárias: R$ {total_necessario_diario:.2f}\n")
        
        print("Detalhamento por produto:")
        for produto in produtos:
            proporcao = produto["peso"] / 100
            meta_por_produto = meta * proporcao
            vendas_mensais = meta_por_produto / tempo
            vendas_diarias = vendas_mensais / dias_por_mes
            unidades_por_mes = vendas_mensais / produto["valor"]
            unidades_por_dia = vendas_diarias / produto["valor"]
            
            print(f"- Produto: {produto['nome']} (R$ {produto['valor']:.2f} cada)")
            print(f"  Peso: {produto['peso']}% da meta total")
            print(f"  Meta por produto: R$ {meta_por_produto:.2f}")
            print(f"  Unidades por dia: {unidades_por_dia:.2f}")
            print(f"  Unidades por mês: {unidades_por_mes:.2f}\n")
        
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

# Executa a função
calcular_meta_personalizada()
