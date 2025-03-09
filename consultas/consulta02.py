import sqlite3
from datetime import datetime

conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()

data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

cursor.execute(
    '''
   select data,localizacao,tipo 
from Eventos D 
left join 
Dados_Eventos DE ON D.id = de.id_evento
WHERE data >= ?
LIMIT 2
    ''', (data_atual,)
)

eventos = cursor.fetchall()

conn.close()

if eventos:
    print("\nDois eventos mais próximos de iniciar:")
    for evento in eventos:
        data, localizacao, tipo = evento
        print(f"Data: {data}, Localização: {localizacao}, Tipo: {tipo}")
else:
    print("Nenhum evento encontrado ou todos os eventos já passaram.")
