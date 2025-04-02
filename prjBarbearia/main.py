from flask import Flask, render_template, request, redirect, url_for
import models
import database

app = Flask(__name__)


# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')


# Rota para exibir todos os clientes com funcionalidade de pesquisa
@app.route('/clientes', endpoint='clientes')
def listar_clientes():
    search_query = request.args.get('search')
    if search_query:
        # Filtra os clientes pelo nome, insensível a maiúsculas/minúsculas
        clientes = [cliente for cliente in database.get_all_clients() if
                    search_query.lower() in cliente['nome'].lower()]
    else:
        clientes = database.get_all_clients()
    return render_template('clientes.html', clientes=clientes)


# Rota para adicionar um novo cliente
@app.route('/clientes/novo', methods=['GET', 'POST'], endpoint='novo_cliente')
def novo_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        database.add_client(nome, telefone, email, endereco)
        return redirect(url_for('clientes'))
    return render_template('novo_cliente.html')


# Rota para exibir todos os serviços com funcionalidade de pesquisa
@app.route('/servicos', endpoint='servicos')
def listar_servicos():
    search_query = request.args.get('search')
    if search_query:
        # Filtra os serviços pela descrição, insensível a maiúsculas/minúsculas
        servicos = [servico for servico in database.get_all_services() if
                    search_query.lower() in servico['descricao'].lower()]
    else:
        servicos = database.get_all_services()
    return render_template('servicos.html', servicos=servicos)


# Rota para adicionar um novo serviço
@app.route('/servicos/novo', methods=['GET', 'POST'], endpoint='novo_servico')
def novo_servico():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        database.add_service(descricao, valor)
        return redirect(url_for('servicos'))
    return render_template('novo_servico.html')


# Rota para exibir todas as agendas com funcionalidade de pesquisa
@app.route('/agendas', endpoint='agendas')
def listar_agendas():
    search_query = request.args.get('search')
    order_by = request.args.get('order_by', 'data')  # Ordenar por 'data' por padrão

    # Se houver uma consulta de pesquisa, filtramos as agendas pelo nome do cliente
    if search_query:
        agendas = [agenda for agenda in models.listar_agendas(order_by=order_by) if
                   search_query.lower() in agenda['cliente'].lower()]
    else:
        agendas = models.listar_agendas(order_by=order_by)

    return render_template('agendas.html', agendas=agendas)


# Rota para adicionar uma nova agenda
@app.route('/agendas/nova', methods=['GET', 'POST'], endpoint='nova_agenda')
def nova_agenda():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        id_servico = request.form['id_servico']
        data = request.form['data']
        hora = request.form['hora']
        observacoes = request.form['observacoes']
        models.adicionar_agenda(id_cliente, id_servico, data, hora, observacoes)
        return redirect(url_for('agendas'))

    clientes = models.listar_clientes()
    servicos = models.listar_servicos()
    return render_template('nova_agenda.html', clientes=clientes, servicos=servicos)


# Rota para excluir um cliente
@app.route('/clientes/excluir/<int:id_cliente>', methods=['POST'], endpoint='excluir_cliente')
def excluir_cliente(id_cliente):
    try:
        models.excluir_cliente(id_cliente)
    except ValueError:
        return render_template('erro_exclusao.html',
                               mensagem="Não é possível excluir o cliente porque há agendamentos associados.")
    return redirect(url_for('clientes'))


# Rota para excluir um serviço
@app.route('/servicos/excluir/<int:id_servico>', methods=['POST'], endpoint='excluir_servico')
def excluir_servico(id_servico):
    models.excluir_servico(id_servico)
    return redirect(url_for('servicos'))


# Rota para excluir uma agenda
@app.route('/agendas/excluir/<int:id_agenda>', methods=['POST'], endpoint='excluir_agenda')
def excluir_agenda(id_agenda):
    models.excluir_agenda(id_agenda)
    return redirect(url_for('agendas'))


# Rota para editar um cliente
@app.route('/clientes/editar/<int:id_cliente>', methods=['GET', 'POST'], endpoint='editar_cliente')
def editar_cliente(id_cliente):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        models.atualizar_cliente(id_cliente, nome, telefone, email, endereco)
        return redirect(url_for('clientes'))
    cliente = next((cliente for cliente in models.listar_clientes() if cliente['id_cliente'] == id_cliente), None)
    return render_template('editar_cliente.html', cliente=cliente)


# Rota para editar um serviço
@app.route('/servicos/editar/<int:id_servico>', methods=['GET', 'POST'], endpoint='editar_servico')
def editar_servico(id_servico):
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        models.atualizar_servico(id_servico, descricao, valor)
        return redirect(url_for('servicos'))
    servico = next((servico for servico in models.listar_servicos() if servico['id_servico'] == id_servico), None)
    return render_template('editar_servico.html', servico=servico)


# Rota para editar uma agenda
@app.route('/agendas/editar/<int:id_agenda>', methods=['GET', 'POST'], endpoint='editar_agenda')
def editar_agenda(id_agenda):
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        id_servico = request.form['id_servico']
        data = request.form['data']
        hora = request.form['hora']
        observacoes = request.form['observacoes']
        models.atualizar_agenda(id_agenda, id_cliente, id_servico, data, hora, observacoes)
        return redirect(url_for('agendas'))

    # Recupera a agenda específica a ser editada, e as listas de clientes e serviços
    agenda = models.obter_agenda_por_id(id_agenda)  # Nova função para buscar a agenda específica
    clientes = models.listar_clientes()  # Lista de todos os clientes
    servicos = models.listar_servicos()  # Lista de todos os serviços

    return render_template('editar_agenda.html', agenda=agenda, clientes=clientes, servicos=servicos)

if __name__ == '__main__':
    app.run(debug=True)
