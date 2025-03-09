from db import criar_tabelas, inserir_evento
from scraping import extrair_dados_evento

# Função principal que organiza o fluxo de execução
def main():
   
    criar_tabelas()

    eventos = extrair_dados_evento()

    if eventos:
        # Inserir dados extraídos no banco de dados
        for evento in eventos:
            nome = evento["nome"]
            tipo = evento["tipo"]
            data = evento["data"]
            localizacao = evento["localizacao"]
            metadados = evento.get("metadados", "Metadados não encontrados") 

            inserir_evento(nome, tipo, data, localizacao, metadados)
    else:
        print("Nenhum evento encontrado ou erro na extração.")

if __name__ == "__main__":
    main()

print('Código executado com sucesso!')
