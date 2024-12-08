import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def financiar_construcao(valor_do_imovel, prazo_anos):
    taxa_juros = 9.75
    percentual_entrada = 20
    valor_entrada = (percentual_entrada / 100) * valor_do_imovel
    valor_financiado = valor_do_imovel - valor_entrada
    prazo_meses = prazo_anos * 12
    taxa_mensal = taxa_juros / 12 / 100
    parcela = (valor_financiado * taxa_mensal) / (1 - (1 + taxa_mensal) ** -prazo_meses)
    total_pago = parcela * prazo_meses
    juros_totais = total_pago - valor_financiado
    return taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais

def financiar_casa(valor_do_imovel, prazo_anos):
    taxa_juros = 8.99
    percentual_entrada = 20
    valor_entrada = (percentual_entrada / 100) * valor_do_imovel
    valor_financiado = valor_do_imovel - valor_entrada
    prazo_meses = prazo_anos * 12
    taxa_mensal = taxa_juros / 12 / 100
    parcela = (valor_financiado * taxa_mensal) / (1 - (1 + taxa_mensal) ** -prazo_meses)
    total_pago = parcela * prazo_meses
    juros_totais = total_pago - valor_financiado
    return taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais

def financiar_mcmv(valor_do_imovel, prazo_anos):
    taxa_juros = 5.00
    percentual_entrada = 20
    valor_entrada = (percentual_entrada / 100) * valor_do_imovel
    valor_financiado = valor_do_imovel - valor_entrada
    prazo_meses = prazo_anos * 12
    taxa_mensal = taxa_juros / 12 / 100
    parcela = (valor_financiado * taxa_mensal) / (1 - (1 + taxa_mensal) ** -prazo_meses)
    total_pago = parcela * prazo_meses
    juros_totais = total_pago - valor_financiado
    return taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais

def financiar_veiculo(valor_veiculo, prazo_anos, tipo_veiculo):
    if tipo_veiculo == "moto":
        taxa_juros = 1.69
    elif tipo_veiculo == "carro":
        taxa_juros = 1.49
    else:
        print("Tipo de veículo inválido.")
        return None
    
    percentual_entrada = 20
    valor_entrada = (percentual_entrada / 100) * valor_veiculo
    valor_financiado = valor_veiculo - valor_entrada
    prazo_meses = prazo_anos * 12
    taxa_mensal = taxa_juros / 12 / 100
    parcela = (valor_financiado * taxa_mensal) / (1 - (1 + taxa_mensal) ** -prazo_meses)
    total_pago = parcela * prazo_meses
    juros_totais = total_pago - valor_financiado
    return taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais

def calcular_financiamento():
    limpar_tela()
    print("=== Simulador de Financiamento Habitacional e Veicular ===")
    print("Escolha uma opção:")
    print("1 - Financiar construção")
    print("2 - Financiar compra de casa")
    print("3 - Financiar pelo Minha Casa Minha Vida")
    print("4 - Financiar veículo")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        tipo = "construção"
        print("\nVocê escolheu financiar construção.")
        print("Limitação: Valor mínimo para construção é R$ 50.000,00.")
        func = financiar_construcao
        valor_minimo = 80000
    elif opcao == 2:
        tipo = "compra de casa"
        print("\nVocê escolheu financiar compra de casa.")
        print("Limitação: Valor mínimo para compra de casa é R$ 50.000,00.")
        func = financiar_casa
        valor_minimo = 50000
    elif opcao == 3:
        tipo = "Minha Casa Minha Vida"
        print("\nVocê escolheu financiar pelo Minha Casa Minha Vida.")
        print("Limitação: Valor mínimo para o Minha Casa Minha Vida é R$ 30.000,00.")
        func = financiar_mcmv
        valor_minimo = 30000
    elif opcao == 4:
        tipo = "veículo"
        print("\nVocê escolheu financiar veículo.")
        print("Limitação: Valor mínimo para financiamento de veículo é R$ 10.000,00.")
        tipo_veiculo = input("Digite o tipo de veículo (moto ou carro): ").lower()
        func = financiar_veiculo
        valor_minimo = 10000
    else:
        print("Opção inválida. O programa será encerrado.")
        return
    
    if opcao == 4:  # Para veículos, perguntamos o valor do veículo
        valor_veiculo = float(input("\nDigite o valor do veículo: R$ "))
        if valor_veiculo < valor_minimo:
            print(f"Valor mínimo para financiamento de veículo é R$ {valor_minimo:,.2f}.")
            return
        prazo_anos = int(input("Informe o prazo do financiamento (em anos): "))
        taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais = func(valor_veiculo, prazo_anos, tipo_veiculo)
    else:  # Para os outros tipos, usamos o valor do imóvel
        valor_do_imovel = float(input("\nDigite o valor do imóvel ou construção: R$ "))
        if valor_do_imovel < valor_minimo:
            print(f"Valor mínimo para esse tipo de financiamento é R$ {valor_minimo:,.2f}.")
            return
        prazo_anos = int(input("Informe o prazo do financiamento (em anos): "))
        taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais = func(valor_do_imovel, prazo_anos)
    
    print("\n=== Resumo do financiamento ===")
    print(f"Tipo de financiamento: {tipo.capitalize()}")
    print(f"Valor do bem: R$ {valor_veiculo if opcao == 4 else valor_do_imovel:,.2f}")
    print(f"Entrada mínima (20%): R$ {valor_entrada:,.2f}")
    print(f"Valor financiado: R$ {valor_financiado:,.2f}")
    print(f"Prazo: {prazo_anos} anos ({prazo_anos * 12} meses)")
    print(f"Taxa de juros mensal: {taxa_juros / 12:.2f}%")
    print(f"Valor da parcela: R$ {parcela:,.2f}")
    print(f"Juros totais pagos: R$ {juros_totais:,.2f}")
    print(f"Valor total pago (financiamento + juros): R$ {total_pago:,.2f}")

calcular_financiamento()
