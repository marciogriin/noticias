create database jornal;

create table categorias(
id int primary key,
nome varchar(65)
);

create table noticias(
id int primary key,
nome varchar (65),
texto text,
id_categoria int,
Foreign key (id_categoria) REFERENCES `categorias` (`id`)
);
