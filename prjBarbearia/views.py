from flask import render_template, request, redirect, url_for
import models

# View para exibir a página inicial
def index():
    return render_template('index.html')

# View para listar todos os clientes
def listar_clientes():
    clientes = models.listar_clientes()
    return render_template('clientes.html', clientes=clientes)

# View para adicionar um novo cliente
def novo_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        endereco = request.form['endereco']
        models.adicionar_cliente(nome, telefone, email, endereco)
        return redirect(url_for('clientes'))
    return render_template('novo_cliente.html')


# View para listar todos os serviços
def listar_servicos():
    servicos = models.listar_servicos()
    return render_template('servicos.html', servicos=servicos)

# View para adicionar um novo serviço
def novo_servico():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        models.adicionar_servico(descricao, valor)
        return redirect(url_for('listar_servicos'))
    return render_template('novo_servico.html')

# View para listar todas as agendas
def listar_agendas():
    agendas = models.listar_agendas()
    return render_template('agendas.html', agendas=agendas)

# View para adicionar uma nova agenda
def nova_agenda():
    if request.method == 'POST':
        id_cliente = request.form['id_cliente']
        id_servico = request.form['id_servico']
        data = request.form['data']
        hora = request.form['hora']
        observacoes = request.form['observacoes']
        models.adicionar_agenda(id_cliente, id_servico, data, hora, observacoes)
        return redirect(url_for('listar_agendas'))
    return render_template('nova_agenda.html')
