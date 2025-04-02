import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adm123",
        database="sistema_gestao"
    )
    return connection

def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    connection.commit()
    cursor.close()
    connection.close()

def get_all_clients():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Cliente")
    clients = cursor.fetchall()
    cursor.close()
    connection.close()
    return clients

def add_client(nome, telefone, email, endereco):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Cliente (nome, telefone, email, endereco)
        VALUES (%s, %s, %s, %s)
    """, (nome, telefone, email, endereco))
    connection.commit()
    cursor.close()
    connection.close()

def get_all_services():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Servico")
    services = cursor.fetchall()
    cursor.close()
    connection.close()
    return services

def add_service(descricao, valor):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Servico (descricao, valor)
        VALUES (%s, %s)
    """, (descricao, valor))
    connection.commit()
    cursor.close()
    connection.close()

def get_all_agendas():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""
        SELECT A.id_agenda, C.nome AS cliente, S.descricao AS servico, A.data, A.hora, A.observacoes
        FROM Agenda A
        JOIN Cliente C ON A.id_cliente = C.id_cliente
        JOIN Servico S ON A.id_servico = S.id_servico
    """)
    agendas = cursor.fetchall()
    cursor.close()
    connection.close()
    return agendas

def add_agenda(id_cliente, id_servico, data, hora, observacoes):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO Agenda (id_cliente, id_servico, data, hora, observacoes)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_cliente, id_servico, data, hora, observacoes))
    connection.commit()
    cursor.close()
    connection.close()


def delete_client(id_cliente):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id_cliente,))
    connection.commit()
    cursor.close()
    connection.close()


def delete_service(id_servico):
    connection = connect_db()
    cursor = connection.cursor()

    # Exclui todos os agendamentos associados ao serviço
    cursor.execute("DELETE FROM Agenda WHERE id_servico = %s", (id_servico,))

    # Agora exclui o serviço
    cursor.execute("DELETE FROM Servico WHERE id_servico = %s", (id_servico,))

    connection.commit()
    cursor.close()
    connection.close()


def delete_agenda(id_agenda):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Agenda WHERE id_agenda = %s", (id_agenda,))
    connection.commit()
    cursor.close()
    connection.close()

def update_client(id_cliente, nome, telefone, email, endereco):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE Cliente 
        SET nome = %s, telefone = %s, email = %s, endereco = %s 
        WHERE id_cliente = %s
    """, (nome, telefone, email, endereco, id_cliente))
    connection.commit()
    cursor.close()
    connection.close()

def update_service(id_servico, descricao, valor):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE Servico 
        SET descricao = %s, valor = %s 
        WHERE id_servico = %s
    """, (descricao, valor, id_servico))
    connection.commit()
    cursor.close()
    connection.close()

def update_agenda(id_agenda, id_cliente, id_servico, data, hora, observacoes):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE Agenda 
        SET id_cliente = %s, id_servico = %s, data = %s, hora = %s, observacoes = %s 
        WHERE id_agenda = %s
    """, (id_cliente, id_servico, data, hora, observacoes, id_agenda))
    connection.commit()
    cursor.close()
    connection.close()

