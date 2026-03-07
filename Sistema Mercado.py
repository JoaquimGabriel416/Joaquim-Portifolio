# Dicionário para armazenar os produtos em memória
estoque = {}


# Função para cadastrar produtos
def cadastrar_produto():
    print("\n CADASTRO DE PRODUTOS")
    nome = input("Nome do produto: ").strip()
    if not nome:
        print(" O nome do produto não pode estar vazio.")
        return
    try:
        preco = float(input("Preço (R$): "))
        tipo = input("Tipo de venda (Unidade/Quilo): ").capitalize()
        quantidade = float(input(f"Quantidade em {tipo.lower()}: "))
    except ValueError:
        print(" Valor inválido! Digite números válidos para preço e quantidade.")
        return

    codigo = len(estoque) + 1
    estoque[codigo] = {
        "nome": nome,
        "preco": preco,
        "tipo": tipo,
        "quantidade": quantidade
    }
    print(f" Produto '{nome}' cadastrado com sucesso! Código: {codigo}")


# Função para consultar o estoque
def consultar_estoque():
    print("\n CONSULTA DE ESTOQUE")
    if estoque:
        for codigo, produto in estoque.items():
            print(f"Código: {codigo} | Nome: {produto['nome']} | "
                  f"Preço: R${produto['preco']:.2f} | "
                  f"Quantidade: {produto['quantidade']} {produto['tipo']}")
    else:
        print(" Nenhum produto cadastrado até o momento.")


# Função para realizar compras
def realizar_compra():
    print("\n REALIZAR COMPRA")
    try:
        codigo = int(input("Digite o código do produto: "))
    except ValueError:
        print(" Código inválido!")
        return

    if codigo in estoque:
        produto = estoque[codigo]
        print(f"Produto: {produto['nome']} - R${produto['preco']:.2f} por {produto['tipo'].lower()}")
        try:
            qtd = float(input(f"Quantidade ({produto['tipo']}): "))
        except ValueError:
            print(" Quantidade inválida!")
            return

        if qtd <= produto["quantidade"]:
            total = qtd * produto["preco"]
            produto["quantidade"] -= qtd
            print(f" Compra realizada com sucesso! Total: R${total:.2f}")
            print(f"Estoque atualizado: {produto['quantidade']} {produto['tipo']}(s) restantes.")
        else:
            print(" Estoque insuficiente para a quantidade solicitada.")
    else:
        print(" Produto não encontrado. Verifique o código e tente novamente.")


# Função principal com menu
def menu_principal():
    while True:
        print("\n========= SISTEMA DE ESTOQUE =========")
        print("1. Cadastrar Produto")
        print("2. Consultar Estoque")
        print("3. Realizar Compra")
        print("4. Sair")
        print("=====================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_estoque()
        elif opcao == "3":
            realizar_compra()
        elif opcao == "4":
            print(" Saindo do sistema...")
            break
        else:
            print(" Opção inválida. Tente novamente.")


# Execução do sistema
if __name__ == "__main__":
    menu_principal()

