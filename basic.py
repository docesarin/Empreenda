import os
import time

# Script simples de cálculos empresariais 
#  /\_/\  
# ( o o ) 
#  >   < 

def calcular_preco_venda(custo_producao, margem_lucro, impostos, outros_custos):
    preco_venda = (custo_producao / (1 - margem_lucro / 100)) + impostos + outros_custos
    return round(preco_venda, 2)

def calcular_margem_lucro(preco_venda, custo_producao):
    margem_lucro = ((preco_venda - custo_producao) / preco_venda) * 100
    return round(margem_lucro, 2)

def calcular_ponto_equilibrio(custo_fixo, preco_venda, custo_variavel):
    ponto_equilibrio = custo_fixo / (preco_venda - custo_variavel)
    return round(ponto_equilibrio, 2)

def calcular_lucro_liquido(preco_venda, custo_producao, impostos, outros_custos):
    lucro_liquido = preco_venda - custo_producao - impostos - outros_custos
    return round(lucro_liquido, 2)

def estimar_lucro_anual(vendas_mensais, custo_mensal):
    lucro_anual = (vendas_mensais * 12) - (custo_mensal * 12)
    return round(lucro_anual, 2)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar_texto(texto, delay=0.05):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def exibir_resultado(opcao):
    limpar_tela()
    try:
        if opcao == "preco_venda":
            custo_producao = float(input("Digite o custo de produção (R$): "))
            margem_lucro = float(input("Digite a margem de lucro (%): "))
            impostos = float(input("Digite os impostos (%): "))
            outros_custos = float(input("Digite outros custos (R$): "))
            resultado = calcular_preco_venda(custo_producao, margem_lucro, impostos, outros_custos)
            print(f"\nPreço de Venda Ideal: R${resultado}")
        
        elif opcao == "margem_lucro":
            preco_venda = float(input("Digite o preço de venda (R$): "))
            custo_producao = float(input("Digite o custo de produção (R$): "))
            resultado = calcular_margem_lucro(preco_venda, custo_producao)
            print(f"\nMargem de Lucro: {resultado}%")
        
        elif opcao == "ponto_equilibrio":
            custo_fixo = float(input("Digite o custo fixo mensal (R$): "))
            custo_variavel = float(input("Digite o custo variável (R$): "))
            preco_venda = float(input("Digite o preço de venda (R$): "))
            resultado = calcular_ponto_equilibrio(custo_fixo, preco_venda, custo_variavel)
            print(f"\nPonto de Equilíbrio: {resultado} unidades")
        
        elif opcao == "lucro_liquido":
            preco_venda = float(input("Digite o preço de venda (R$): "))
            custo_producao = float(input("Digite o custo de produção (R$): "))
            impostos = float(input("Digite os impostos (R$): "))
            outros_custos = float(input("Digite outros custos (R$): "))
            resultado = calcular_lucro_liquido(preco_venda, custo_producao, impostos, outros_custos)
            print(f"\nLucro Líquido: R${resultado}")
        
        elif opcao == "lucro_anual":
            vendas_mensais = float(input("Digite as vendas mensais (R$): "))
            custo_mensal = float(input("Digite o custo mensal (R$): "))
            resultado = estimar_lucro_anual(vendas_mensais, custo_mensal)
            print(f"\nLucro Estimado Anual: R${resultado}")
    
    except ValueError:
        print("Erro: Por favor, insira valores válidos!")

def exibir_opcoes():
    limpar_tela()
    print("="*60)
    digitar_texto("Bem-vindo ao Empreenda - Calculadora de Preços!", delay=0.05)
    print("="*60)

    print("Escolha o cálculo que deseja realizar:")
    print("1 - Calcular Preço de Venda")
    print("2 - Calcular Margem de Lucro")
    print("3 - Calcular Ponto de Equilíbrio")
    print("4 - Calcular Lucro Líquido")
    print("5 - Estimar Lucro Anual")

    opcao = input("\nDigite o número da opção desejada: ")
    
    if opcao == "1":
        exibir_resultado("preco_venda")
    elif opcao == "2":
        exibir_resultado("margem_lucro")
    elif opcao == "3":
        exibir_resultado("ponto_equilibrio")
    elif opcao == "4":
        exibir_resultado("lucro_liquido")
    elif opcao == "5":
        exibir_resultado("lucro_anual")
    else:
        print("Opção inválida, tente novamente.")

def main():
    while True:
        exibir_opcoes()
        continuar = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
        if continuar != 's':
            for i in range(3):
                print("Saindo... " + "." * (i + 1), end="\r")
                time.sleep(0.5)
            print("Obrigado por usar o Empreenda! Até logo!")
            break

if __name__ == "__main__":
    main()
