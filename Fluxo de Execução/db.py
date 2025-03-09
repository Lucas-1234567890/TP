import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        tipo TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dados_Eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_evento INTEGER,
        data TEXT,
        localizacao TEXT,
        FOREIGN KEY (id_evento) REFERENCES Eventos(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Metadados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_evento INTEGER,
        metadado TEXT,
        FOREIGN KEY (id_evento) REFERENCES Eventos(id)
    )''')

    conn.commit()
    conn.close()

def inserir_evento(nome, tipo, data, localizacao, metadados):
    conn = sqlite3.connect('eventos.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Eventos (nome, tipo) VALUES (?, ?)''', (nome, tipo))
    evento_id = cursor.lastrowid  # Pega o id do último evento inserido

    cursor.execute('''
    INSERT INTO Dados_Eventos (id_evento, data, localizacao) VALUES (?, ?, ?)''', 
                   (evento_id, data, localizacao))

    # Inserir os metadados, se houver
    for metadado in metadados:
        cursor.execute('''
        INSERT INTO Metadados (id_evento, metadado) VALUES (?, ?)''', 
                       (evento_id, metadado))

    conn.commit()
    conn.close()
