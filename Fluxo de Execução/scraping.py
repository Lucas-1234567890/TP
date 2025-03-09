import urllib.request
from bs4 import BeautifulSoup


def extrair_dados_evento():
    url = "https://www.sympla.com.br/eventos/carnaval"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }

    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, "html.parser")
        
    eventos = soup.find_all("h3", class_="pn67h18")
        
    # Armazenando as palavras-chave do tipo de evento
    tipos_palavras_chave = {
        "musica": ["show", "musical", "concert", "rock", "pop"],
        "teatro": ["teatro", "drama", "peça", "performance"],
        "arte": ["exposição", "arte", "museu", "galeria"],
        "ar livre": ["carnaval", "bloco", "festa", "frevo", "ar livre"]
    }

    def identificar_tipo(nome_evento):
        nome_evento_lower = nome_evento.lower()  
        for tipo, palavras in tipos_palavras_chave.items():
            if any(palavra in nome_evento_lower for palavra in palavras):  
                return tipo  
        return "Desconhecido"  

    dados_eventos = []

    for evento in eventos:
        nome = evento.text.strip()
        
        data_tag = evento.find_next('div', class_='qtfy413 qtfy414') 
        data = data_tag.text.strip() if data_tag else "Data não encontrada"
        
        localizacao_tag = evento.find_next('p', class_='pn67h1a')  
        localizacao = localizacao_tag.text.strip() if localizacao_tag else "Localização não encontrada"
        
        tipo = identificar_tipo(nome)
    
        dados_eventos.append({
            "nome": nome,
            "data": data,
            "localizacao": localizacao,
            "tipo": tipo
        })

    return dados_eventos
