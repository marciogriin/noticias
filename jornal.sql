create database jornal;

create table categorias(
id int primary key auto_increment,
nome varchar(65)
);

drop table categorias;

create table noticias(
id int primary key auto_increment,
nome varchar (65),
texto text,
id_categoria int,
Foreign key (id_categoria) REFERENCES `categorias` (`id`)
);

select * from categorias;

insert into categorias (id, nome) VALUES (1, 'esportes');

select * from noticias;
insert into noticias (nome, texto, id_categoria) VALUES ( 'ganha', ' time ganha de 1 a 0', 1);


delete from categorias where id = 5;

SELECT noticias.id, noticias.nome, noticias.texto, noticias.id_categoria, categorias.nome FROM noticias join categorias on noticias.id_categoria = categorias.id;

