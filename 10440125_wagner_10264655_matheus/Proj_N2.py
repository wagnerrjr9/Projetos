#Wagner Araujo Marcelino Junior RA 10440125
#Matheus Carneiro Maciel RA 10264655
import csv
import os
from typing import List, Dict, Tuple

# Função para carregar os dados do arquivo CSV
def carregar_dados(arquivo_csv: str) -> List[Dict[str, str]]:
    if not os.path.isfile(arquivo_csv):
        raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_csv}")
    
    dados = []
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dados.append(row)
    return dados

# Função para contar produtos por categoria
def contar_produtos_por_categoria(dados: List[Dict[str, str]]) -> Dict[str, int]:
    contagem = {}
    for item in dados:
        categoria = item['categoryName']
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    return contagem

# Função para calcular o percentual de produtos por categoria
def percentual_produtos_por_categoria(dados: List[Dict[str, str]]) -> Dict[str, float]:
    contagem = contar_produtos_por_categoria(dados)
    total_produtos = len(dados)
    percentual = {cat: (count / total_produtos) * 100 for cat, count in contagem.items()}
    return percentual

# Função para calcular a proporção de produtos best-sellers por categoria
def proporcao_best_sellers_por_categoria(dados: List[Dict[str, str]]) -> Dict[str, float]:
    best_sellers = {}
    contagem = contar_produtos_por_categoria(dados)
    for item in dados:
        if item['isBestSeller'].lower() == 'true':
            categoria = item['categoryName']
            if categoria in best_sellers:
                best_sellers[categoria] += 1
            else:
                best_sellers[categoria] = 1
    proporcao = {cat: (best_sellers.get(cat, 0) / count) * 100 for cat, count in contagem.items()}
    return proporcao

# Função para identificar os 10 produtos mais caros e mais baratos
def top_10_produtos_caros_baratos(dados: List[Dict[str, str]]) -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    ordenado_por_preco = sorted(dados, key=lambda x: float(x['price']), reverse=True)
    top_caros = ordenado_por_preco[:10]
    top_baratos = ordenado_por_preco[-10:]
    return top_caros, top_baratos

# Função para listar produtos por categoria
def listar_produtos_por_categoria(dados: List[Dict[str, str]], categoria_escolhida: str) -> List[Dict[str, str]]:
    produtos_categoria = [item for item in dados if item['categoryName'].lower() == categoria_escolhida.lower()]
    return produtos_categoria

# Função para gerar relatório em HTML
def gerar_relatorio_html(dados: List[Dict[str, str]], caminho_html: str):
    categorias = set(item['categoryName'] for item in dados)
    html_content = "<html><head><title>Relatório de Best-Sellers</title></head><body>"
    html_content += "<h1>Top 10 Best-Sellers por Categoria</h1>"
    for categoria in categorias:
        best_sellers = sorted(
            [item for item in dados if item['categoryName'] == categoria and item['isBestSeller'].lower() == 'true'],
            key=lambda x: int(x['boughtInLastMonth']), 
            reverse=True
        )[:10]
        if best_sellers:
            html_content += f"<h2>{categoria}</h2><ul>"
            for produto in best_sellers:
                html_content += f"<li>{produto['title']} - Quantidade vendida: {produto['boughtInLastMonth']}</li>"
            html_content += "</ul>"
    html_content += "</body></html>"

    with open(caminho_html, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Relatório gerado com sucesso em: {caminho_html}")

# Função para exibir o menu e lidar com a interação do usuário
def menu_interativo(dados: List[Dict[str, str]]):
    while True:
        print("\nMenu de Opções:")
        print("1. Contar produtos por categoria")
        print("2. Calcular percentual de produtos por categoria")
        print("3. Proporção de best-sellers por categoria")
        print("4. Top 10 produtos mais caros e mais baratos")
        print("5. Listar produtos por categoria")
        print("6. Gerar relatório HTML dos top 10 best-sellers por categoria")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            contagem = contar_produtos_por_categoria(dados)
            for categoria, count in contagem.items():
                print(f"{categoria}: {count} produtos")
        elif opcao == '2':
            percentual = percentual_produtos_por_categoria(dados)
            for categoria, perc in percentual.items():
                print(f"{categoria}: {perc:.2f}%")
        elif opcao == '3':
            proporcao = proporcao_best_sellers_por_categoria(dados)
            for categoria, prop in proporcao.items():
                print(f"{categoria}: {prop:.2f}% de best-sellers")
        elif opcao == '4':
            top_caros, top_baratos = top_10_produtos_caros_baratos(dados)
            print("Top 10 Produtos Mais Caros:")
            for produto in top_caros:
                print(f"{produto['title']} - Preço: {produto['price']}")
            print("\nTop 10 Produtos Mais Baratos:")
            for produto in top_baratos:
                print(f"{produto['title']} - Preço: {produto['price']}")
        elif opcao == '5':
            categoria_escolhida = input("Digite a categoria: ")
            produtos_categoria = listar_produtos_por_categoria(dados, categoria_escolhida)
            if produtos_categoria:
                for produto in produtos_categoria:
                    print(f"{produto['title']} - Preço: {produto['price']}")
            else:
                print("Nenhum produto encontrado para essa categoria.")
        elif opcao == '6':
            caminho_html = os.path.join(os.getcwd(), 'relatorio_best_sellers.html')
            gerar_relatorio_html(dados, caminho_html)
        elif opcao == '7':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Programa principal
if __name__ == "__main__":
    caminho_csv = 'emack.csv'  # Ajuste o caminho para o seu arquivo CSV aqui
    dados = carregar_dados(caminho_csv)
    menu_interativo(dados)
