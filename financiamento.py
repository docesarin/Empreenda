import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_financiamento_base(valor_bem, prazo_anos, taxa_juros_anual, percentual_entrada, cet_anual=0, cesh_anual=0):
    prazo_meses = prazo_anos * 12
    taxa_mensal = taxa_juros_anual / 12 / 100
    cet_mensal = cet_anual / 12 / 100
    cesh_mensal = cesh_anual / 12 / 100

    valor_entrada = (percentual_entrada / 100) * valor_bem
    valor_financiado = valor_bem - valor_entrada

    parcela = (valor_financiado * (taxa_mensal + cet_mensal + cesh_mensal)) / (
        1 - (1 + taxa_mensal + cet_mensal + cesh_mensal) ** -prazo_meses
    )
    total_pago = parcela * prazo_meses
    juros_totais = total_pago - valor_financiado

    return {
        "valor_entrada": valor_entrada,
        "valor_financiado": valor_financiado,
        "parcela": parcela,
        "total_pago": total_pago,
        "juros_totais": juros_totais,
        "taxa_juros_anual": taxa_juros_anual,
        "prazo_meses": prazo_meses,
    }

def exibir_resumo(tipo, valor_bem, resultado, prazo_anos):
    print("\n=== Resumo do financiamento ===")
    print(f"Tipo de financiamento: {tipo}")
    print(f"Valor do bem: R$ {valor_bem:,.2f}")
    print(f"Entrada mínima: R$ {resultado['valor_entrada']:,.2f}")
    print(f"Valor financiado: R$ {resultado['valor_financiado']:,.2f}")
    print(f"Prazo: {prazo_anos} anos ({resultado['prazo_meses']} meses)")
    print(f"Valor da parcela: R$ {resultado['parcela']:,.2f}")
    print(f"Juros totais pagos: R$ {resultado['juros_totais']:,.2f}")
    print(f"Valor total pago: R$ {resultado['total_pago']:,.2f}")

def calcular_financiamento():
    limpar_tela()
    print("=== Simulador de Financiamento ===")
    print("1 - Construção")
    print("2 - Compra de Casa")
    print("3 - Minha Casa Minha Vida")
    print("4 - Veículo (Moto ou Carro)")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao not in [1, 2, 3, 4]:
        print("Opção inválida. O programa será encerrado.")
        return

    if opcao == 4:
        tipo_veiculo = input("Digite o tipo de veículo (moto ou carro): ").lower()
        if tipo_veiculo not in ["moto", "carro"]:
            print("Tipo de veículo inválido.")
            return
        valor_minimo = 10000
        taxa_juros_anual = 1.69 if tipo_veiculo == "moto" else 1.49
        tipo = f"Financiamento de {tipo_veiculo.capitalize()}"
    else:
        tipos = {
            1: ("Construção", 80000, 9.75),
            2: ("Compra de Casa", 50000, 8.99),
            3: ("Minha Casa Minha Vida", 30000, 4.5),
        }
        tipo, valor_minimo, taxa_juros_anual = tipos[opcao]

    valor_bem = float(input(f"Digite o valor do bem (mínimo R$ {valor_minimo:,.2f}): R$ "))
    if valor_bem < valor_minimo:
        print(f"O valor mínimo para este financiamento é R$ {valor_minimo:,.2f}.")
        return

    prazo_anos = int(input("Informe o prazo do financiamento (em anos): "))

    cet_anual = 0.66 if opcao == 3 else 0  # Aplicável apenas para MCMV
    cesh_anual = 3.8 if opcao == 3 else 0  # Seguro habitacional para MCMV
    percentual_entrada = 20  # Entrada padrão de 20%

    resultado = calcular_financiamento_base(
        valor_bem, prazo_anos, taxa_juros_anual, percentual_entrada, cet_anual, cesh_anual
    )

    exibir_resumo(tipo, valor_bem, resultado, prazo_anos)

calcular_financiamento()
