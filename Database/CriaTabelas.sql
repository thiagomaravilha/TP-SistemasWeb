-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS sistema_gestao;
USE sistema_gestao;

-- Criação da tabela Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(255),
    endereco VARCHAR(255)
);

-- Criação da tabela Serviço
CREATE TABLE IF NOT EXISTS Servico (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);

-- Criação da tabela Agenda
CREATE TABLE IF NOT EXISTS Agenda (
    id_agenda INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_servico INT,
    data DATE NOT NULL,
    hora TIME NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_servico) REFERENCES Servico(id_servico)
);
