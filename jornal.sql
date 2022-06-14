create database jornal;

create table categorias(
id int primary key auto_increment,
nome varchar(65)
);

create table noticias(
id int primary key auto_increment,
nome varchar (65),
texto text,
id_categoria int,
Foreign key (id_categoria) REFERENCES `categorias` (`id`)
);

select * from categorias;

insert into categorias (id, nome) VALUES (1, 'esportes');

update;




