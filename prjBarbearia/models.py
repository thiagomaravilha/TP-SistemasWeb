import database

# Funções relacionadas à entidade Cliente
def listar_clientes():
    return database.get_all_clients()

def adicionar_cliente(nome, telefone, email, endereco):
    database.add_client(nome, telefone, email, endereco)


# Funções relacionadas à entidade Serviço
def listar_servicos():
    return database.get_all_services()

def adicionar_servico(descricao, valor):
    database.add_service(descricao, valor)

# Funções relacionadas à entidade Agenda
def listar_agendas(order_by='data'):
    connection = database.connect_db()
    cursor = connection.cursor(dictionary=True)

    if order_by == 'nome':
        cursor.execute("""
            SELECT Agenda.id_agenda, Cliente.nome AS cliente, Servico.descricao AS servico, Agenda.data, Agenda.hora, Agenda.observacoes
            FROM Agenda
            JOIN Cliente ON Agenda.id_cliente = Cliente.id_cliente
            JOIN Servico ON Agenda.id_servico = Servico.id_servico
            ORDER BY Cliente.nome ASC
        """)
    else:
        cursor.execute("""
            SELECT Agenda.id_agenda, Cliente.nome AS cliente, Servico.descricao AS servico, Agenda.data, Agenda.hora, Agenda.observacoes
            FROM Agenda
            JOIN Cliente ON Agenda.id_cliente = Cliente.id_cliente
            JOIN Servico ON Agenda.id_servico = Servico.id_servico
            ORDER BY Agenda.data ASC
        """)

    agendas = cursor.fetchall()
    cursor.close()
    connection.close()
    return agendas

def obter_agenda_por_id(id_agenda):
    connection = database.connect_db()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT Agenda.id_agenda, Cliente.id_cliente, Cliente.nome AS cliente, 
               Servico.id_servico, Servico.descricao AS servico, Agenda.data, 
               Agenda.hora, Agenda.observacoes
        FROM Agenda
        JOIN Cliente ON Agenda.id_cliente = Cliente.id_cliente
        JOIN Servico ON Agenda.id_servico = Servico.id_servico
        WHERE Agenda.id_agenda = %s
    """, (id_agenda,))

    agenda = cursor.fetchone()  # Obtenha uma única agenda
    cursor.close()
    connection.close()

    return agenda


def adicionar_agenda(id_cliente, id_servico, data, hora, observacoes):
    database.add_agenda(id_cliente, id_servico, data, hora, observacoes)

def excluir_cliente(id_cliente):
    connection = database.connect_db()
    cursor = connection.cursor()

    # Verifica se há agendamentos associados ao cliente
    cursor.execute("SELECT COUNT(*) FROM Agenda WHERE id_cliente = %s", (id_cliente,))
    if cursor.fetchone()[0] > 0:
        cursor.close()
        connection.close()
        raise ValueError("Não é possível excluir o cliente porque há agendamentos associados.")

    # Se não houver agendamentos, exclui o cliente
    cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id_cliente,))
    connection.commit()
    cursor.close()
    connection.close()


def excluir_servico(id_servico):
    database.delete_service(id_servico)

def excluir_agenda(id_agenda):
    database.delete_agenda(id_agenda)

def atualizar_cliente(id_cliente, nome, telefone, email, endereco):
    database.update_client(id_cliente, nome, telefone, email, endereco)

def atualizar_servico(id_servico, descricao, valor):
    database.update_service(id_servico, descricao, valor)

def atualizar_agenda(id_agenda, id_cliente, id_servico, data, hora, observacoes):
    database.update_agenda(id_agenda, id_cliente, id_servico, data, hora, observacoes)


