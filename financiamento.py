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

def calcular_financiamento():
    limpar_tela()
    print("=== Simulador de Financiamento Habitacional ===")
    print("Escolha uma opção:")
    print("1 - Financiar construção")
    print("2 - Financiar compra de casa")
    print("3 - Financiar pelo Minha Casa Minha Vida")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        tipo = "construção"
        print("\nVocê escolheu financiar construção.")
        func = financiar_construcao
    elif opcao == 2:
        tipo = "compra de casa"
        print("\nVocê escolheu financiar compra de casa.")
        func = financiar_casa
    elif opcao == 3:
        tipo = "Minha Casa Minha Vida"
        print("\nVocê escolheu financiar pelo Minha Casa Minha Vida.")
        func = financiar_mcmv
    else:
        print("Opção inválida. O programa será encerrado.")
        return
    
    valor_do_imovel = float(input("\nDigite o valor do imóvel ou construção: R$ "))
    prazo_anos = int(input("Informe o prazo do financiamento (em anos): "))
    
    taxa_juros, valor_entrada, valor_financiado, parcela, total_pago, juros_totais = func(valor_do_imovel, prazo_anos)

    print("\n=== Resumo do financiamento ===")
    print(f"Tipo de financiamento: {tipo.capitalize()}")
    print(f"Valor do imóvel ou construção: R$ {valor_do_imovel:,.2f}")
    print(f"Entrada mínima (20%): R$ {valor_entrada:,.2f}")
    print(f"Valor financiado: R$ {valor_financiado:,.2f}")
    print(f"Prazo: {prazo_anos} anos ({prazo_anos * 12} meses)")
    print(f"Taxa de juros mensal: {taxa_juros / 12:.2f}%")
    print(f"Valor da parcela: R$ {parcela:,.2f}")
    print(f"Juros totais pagos: R$ {juros_totais:,.2f}")
    print(f"Valor total pago (financiamento + juros): R$ {total_pago:,.2f}")

calcular_financiamento()
