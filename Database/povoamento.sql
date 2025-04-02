-- Inserir clientes na tabela Cliente
INSERT INTO Cliente (nome, telefone, email, endereco) VALUES
('João Silva', '111111111', 'joao@gmail.com', 'Rua A, 123'),
('Maria Oliveira', '222222222', 'maria@gmail.com', 'Rua B, 456'),
('Carlos Pereira', '333333333', 'carlos@gmail.com', 'Rua C, 789'),
('Ana Costa', '444444444', 'ana@gmail.com', 'Rua D, 101'),
('Lucas Mendes', '555555555', 'lucas@gmail.com', 'Rua E, 202'),
('Fernanda Souza', '666666666', 'fernanda@gmail.com', 'Rua F, 303'),
('Gabriel Santos', '777777777', 'gabriel@gmail.com', 'Rua G, 404'),
('Juliana Almeida', '888888888', 'juliana@gmail.com', 'Rua H, 505');

-- Inserir serviços na tabela Servico
INSERT INTO Servico (descricao, valor) VALUES
('Corte de Cabelo', 30.00),
('Barba', 15.00),
('Corte e Barba', 40.00),
('Pintura de Cabelo', 60.00),
('Hidratação Capilar', 50.00),
('Alisamento', 100.00);

-- Inserir agendamentos na tabela Agenda
INSERT INTO Agenda (id_cliente, id_servico, data, hora, observacoes) VALUES
(1, 1, '2024-09-01', '10:00:00', 'Prefere estilo moderno'),
(2, 3, '2024-09-02', '14:00:00', 'Cliente novo, primeira visita'),
(3, 2, '2024-09-03', '16:00:00', 'Gosta de barba desenhada'),
(4, 4, '2024-09-04', '11:00:00', 'Deseja uma cor mais clara'),
(5, 5, '2024-09-05', '13:00:00', 'Tratamento capilar intenso'),
(6, 6, '2024-09-06', '15:00:00', 'Alisamento completo'),
(7, 1, '2024-09-07', '09:00:00', 'Corte padrão, sem mudanças'),
(8, 2, '2024-09-08', '10:30:00', 'Barba curta e definida'),
(3, 3, '2024-09-09', '12:00:00', 'Corte e barba como sempre'),
(1, 6, '2024-09-10', '17:00:00', 'Alisamento parcial, foco nas pontas');
