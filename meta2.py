def obter_input_float(prompt, limite_inf=0):
    """Função para obter entradas numéricas do usuário com verificação de valor."""
    while True:
        try:
            valor = float(input(prompt))
            if valor <= limite_inf:
                print(f"Erro: O valor deve ser maior que {limite_inf}. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Erro: Por favor, insira um número válido.")

def obter_input_int(prompt, limite_inf=0):
    """Função para obter entradas inteiras com verificação de valor."""
    while True:
        try:
            valor = int(input(prompt))
            if valor <= limite_inf:
                print(f"Erro: O valor deve ser maior que {limite_inf}. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")

def calcular_meta_personalizada():
    """Função principal para calcular a meta personalizada."""
    print("Bem-vindo ao cálculo da meta personalizada!")

    # Obter a meta e o tempo de forma segura
    meta = obter_input_float("Qual sua meta em reais? ", 0)
    tempo = obter_input_int("Em quantos meses deseja alcançar a meta? ", 0)

    # Validação de valores para meta e tempo
    if meta <= 0 or tempo <= 0:
        print("A meta e o tempo devem ser maiores que zero.")
        return

    # Variáveis para armazenar os produtos e os pesos
    produtos = []
    peso_total = 0

    # Cadastro de produtos
    while True:
        nome = input("Digite o nome do produto (ou pressione Enter para finalizar): ").strip()
        if not nome:
            break

        valor_unitario = obter_input_float(f"Digite o valor unitário de {nome}: ", 0)
        peso = obter_input_float(f"Digite o peso percentual de contribuição de {nome} (ex: 50 para 50%): ", 0)

        # Adicionando o produto e somando os pesos
        produtos.append({"nome": nome, "valor": valor_unitario, "peso": peso})
        peso_total += peso

    # Verificação se produtos foram cadastrados
    if not produtos:
        print("Nenhum produto foi adicionado. O programa será encerrado.")
        return

    # Verificar se a soma dos pesos é igual a 100
    if peso_total != 100:
        print(f"A soma dos pesos deve ser igual a 100%. A soma atual é {peso_total}%. Tente novamente.")
        return

    # Definir o número de dias por mês para cálculo
    dias_por_mes = 30
    total_necessario_diario = meta / (tempo * dias_por_mes)
    total_necessario_mensal = meta / tempo

    # Exibir o resumo do planejamento
    print("\nResumo do planejamento:")
    print(f"Meta total: R$ {meta:.2f}")
    print(f"Prazo: {tempo} meses ({tempo * dias_por_mes} dias)")
    print(f"Vendas mensais necessárias: R$ {total_necessario_mensal:.2f}")
    print(f"Vendas diárias necessárias: R$ {total_necessario_diario:.2f}\n")

    # Detalhamento por produto
    print("Detalhamento por produto:")
    for produto in produtos:
        proporcao = produto["peso"] / 100
        meta_por_produto = meta * proporcao
        vendas_mensais = meta_por_produto / tempo
        vendas_diarias = vendas_mensais / dias_por_mes
        unidades_por_mes = vendas_mensais / produto["valor"]
        unidades_por_dia = vendas_diarias / produto["valor"]

        # Exibir detalhes do produto
        print(f"- Produto: {produto['nome']} (R$ {produto['valor']:.2f} cada)")
        print(f"  Peso: {produto['peso']}% da meta total")
        print(f"  Meta por produto: R$ {meta_por_produto:.2f}")
        print(f"  Unidades por dia: {unidades_por_dia:.2f}")
        print(f"  Unidades por mês: {unidades_por_mes:.2f}\n")

# Executa a função
if __name__ == "__main__":
    calcular_meta_personalizada()
