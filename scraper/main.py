import requests
from bs4 import BeautifulSoup

def obter_preco_atual(url):
    headers = {
        "User-Agent": "Mozzila/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")

    preco_span = soup.find("span", class_="andes-money-amount__fraction")

    if not preco_span:
        print("Preço não encontrado!")
        return None
    
    preco = preco_span.text.strip().replace(".", "")
    return float(preco)