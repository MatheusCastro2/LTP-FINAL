CREATE DATABASE ltp_projeto;

use ltp_projeto;

CREATE TABLE usuario(
	id_usuario int auto_increment primary key,
    nome varchar(100) not null,
    email varchar(100) not null unique,
    senha varchar(228) not null,
    tipo_usuario ENUM('usuario_padrao', 'fiscal_seguranca', 'administrador') not null,
    data_registro timestamp default current_timestamp);
    
create table delito (
	id_delito int auto_increment PRIMARY KEY,
    tipo_crime varchar(100) not null,
    localizacao varchar(255) not null,
    datas date not null,
    hora time not null,
    detalhes TEXT,
    id_usuario_registro int not null,
    FOREIGN KEY (id_usuario_registro) references usuario(id_usuario) on update cascade);
    
    
create table filtro (
	id_filtro int auto_increment primary key,
    tipo_crime varchar(100),
    localizacao varchar(255),
    data_inicio date,
    data_final date,
    id_usuario int not null,
    foreign key (id_usuario) references usuario(id_usuario) ON UPDATE CASCADE ON DELETE CASCADE,
    data_aplicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
    
    CREATE TABLE relatorio (
    id_relatorio INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) ON UPDATE CASCADE ON DELETE CASCADE
);

    
    
    
    
    
    
    
    
