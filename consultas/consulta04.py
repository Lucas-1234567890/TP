import sqlite3

conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()

cursor.execute(
    '''
  SELECT data, localizacao, tipo
    FROM Eventos D 
    LEFT JOIN Dados_Eventos DE ON D.id = DE.id_evento
   where tipo LIKE '%ar livre%'
    '''
)

eventos = cursor.fetchall()

conn.close()

if eventos:
    print("\nEventos ao ar livre:")
    for evento in eventos:
        data, localizacao, tipo = evento
        print(f"Data: {data}, Localização: {localizacao}, Tipo: {tipo}")
else:
    print("Nenhum evento ao ar livre encontrado.")
