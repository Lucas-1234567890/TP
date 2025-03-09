import sqlite3

conn = sqlite3.connect("eventos.db")
cursor = conn.cursor()

cursor.execute(
    '''
   select nome,tipo,metadado from Eventos e
left JOIN
Metadados m on e.id = m.id_evento
    '''
)

eventos = cursor.fetchall()

conn.close()

if eventos:
    print("\nEventos e seus metadados:")
    for evento in eventos:
        nome,tipo,metadado = evento
        print(f"Data: {nome}, Tipo: {tipo}, Metadados: {metadado}")
else:
    print("Nenhum evento encontrado.")
