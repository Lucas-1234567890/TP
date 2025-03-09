import sqlite3


conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()

cursor.execute(
    '''
    select data,localizacao,tipo from Eventos D 
    left join 
    Dados_Eventos DE ON D.id = de.id_evento
    '''
)

eventos = cursor.fetchall()

conn.close()

if eventos:
    print("\nEventos encontrados no banco de dados:")
    for evento in eventos:
        data, localizacao, tipo = evento
        print(f"Data: {data}, Localização: {localizacao}, Tipo: {tipo}")
else:
    print("Nenhum evento encontrado no banco de dados.")
