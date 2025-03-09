import requests
from bs4 import BeautifulSoup

url = "https://www.sympla.com.br/eventos/carnaval"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontrar todos os nomes dos eventos (tags h3 com a classe 'pn67h18')
    eventos = soup.find_all("h3", class_="pn67h18")
    
    tipos_palavras_chave = {
        "musica": ["show", "musical", "concert", "rock", "pop"],
        "teatro": ["teatro", "drama", "peça", "performance"],
        "arte": ["exposição", "arte", "museu", "galeria"],
        "carnaval": ["carnaval", "bloco", "festa", "frevo"]
    }

    # Função para identificar o tipo do evento
    def identificar_tipo(nome_evento):
        nome_evento_lower = nome_evento.lower()
        for tipo, palavras in tipos_palavras_chave.items():
            if any(palavra in nome_evento_lower for palavra in palavras):
                return tipo
        return "Desconhecido"


    for evento in eventos:
        # Nome do evento
        nome = evento.text.strip()
        
        # Data
        data_tag = evento.find_next('div', class_='qtfy413 qtfy414') 
        data = data_tag.text.strip() if data_tag else "Data não encontrada"
        
        # Localização
        localizacao_tag = evento.find_next('p', class_='pn67h1a')  
        localizacao = localizacao_tag.text.strip() if localizacao_tag else "Localização não encontrada"
        
        # Tipo de evento
        tipo = identificar_tipo(nome)
        
        print(f"Nome: {nome}")
        print(f"Data: {data}")
        print(f"Localização: {localizacao}")
        print(f"Tipo de Evento: {tipo}")
        print("-" * 40)

else:
    print(f"Erro ao acessar a página: {response.status_code}")
