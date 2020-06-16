create table Sucursal (
	ID_Sucursal marchar (4),
	direccion VARCHAR(50),
	max_capacidad numeric (3,0),
	ciudad VARCHAR(50),
	primary key (ID_Sucursal)
);

insert into Sucursal (ID_Sucursal, direccion, max_capacidad, ciudad) values (1000, '866 Laurel Terrace', 69, 'Caracas');
insert into Sucursal (ID_Sucursal, direccion, max_capacidad, ciudad) values (1001, '17257 Burrows Road', 223, 'Caracas');
insert into Sucursal (ID_Sucursal, direccion, max_capacidad, ciudad) values (1002, '7629 Talisman Court', 31, 'Caracas');
insert into Sucursal (ID_Sucursal, direccion, max_capacidad, ciudad) values (1003, '350 Sugar Park', 112, 'Caracas');
insert into Sucursal (ID_Sucursal, direccion, max_capacidad, ciudad) values (1004, '805 Grover Road', 88, 'Caracas');


create table Categoria (
	ID_Categoria varchar (4),
	nombre VARCHAR(50),
    primary key (ID_Categoria)
);

insert into Categoria (ID_Categoria, nombre) values (9000, 'Bebidas');
insert into Categoria (ID_Categoria, nombre) values (9001, 'Charcuteria');
insert into Categoria (ID_Categoria, nombre) values (9002, 'Frutas y vegetales');
insert into Categoria (ID_Categoria, nombre) values (9003, 'Snacks');
insert into Categoria (ID_Categoria, nombre) values (9004, 'Higiene');


create table Banco (
	ID_Banco varchar (4),
	nombre VARCHAR(50),
    nro_cuenta varchar (23),
    primary key (ID_Banco)
);

insert into Banco (ID_Banco, nombre, nro_cuenta) values (0001, 'Mercantil', '0105-0077-09-1077235054');
insert into Banco (ID_Banco, nombre, nro_cuenta) values (0002, 'Banesco', '0134-1099-21-0001001610');
insert into Banco (ID_Banco, nombre, nro_cuenta) values (0003, 'Provincial', '0108-0085-41-0100134687');


create table Cliente (
	ID_Cliente varchar (8),
	nombre VARCHAR(50),
    apellido varchar(50),
    cumpleaños date,
    primary key (ID_Cliente)
);

insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (25021709, 'Hestia', 'Boggish', '1/20/1983');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (25399720, 'Edward', 'Odby', '12/22/1984');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (26044929, 'Angelina', 'Nairy', '11/26/1982');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (26118740, 'Mickie', 'Dunning', '2/26/1977');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (24997875, 'Sibyl', 'Pieper', '2/6/1986');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (25619359, 'Ferd', 'Boshere', '4/25/1997');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (24776966, 'Vail', 'Cathenod', '8/4/1994');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (27205181, 'Benni', 'MacCracken', '3/9/1979');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (27651832, 'Annamaria', 'Leach', '1/7/1991');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (25300265, 'Cos', 'Flicker', '8/4/1979');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (27408935, 'Matelda', 'Goddert.sf', '11/26/1997');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (24846813, 'Moreen', 'Nelthrop', '6/19/1997');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (24714462, 'Bellanca', 'Mowett', '4/30/1990');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (27669949, 'Melanie', 'Cathro', '6/21/1976');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (25259010, 'Loella', 'MacWhirter', '5/14/1987');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (24807501, 'Joyous', 'Orrick', '3/12/1976');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (24077324, 'Petra', 'Royse', '10/13/1992');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (26066636, 'Shellie', 'Sweetsur', '6/26/1985');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (26566783, 'Rafferty', 'De Michetti', '4/15/1986');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (25515100, 'Zoe', 'Meakes', '12/4/1978');
insert into Cliente (ID_Cliente, nombre, apellido, cumpleaños) values (27937999, 'Jyoti', 'Paolo', '3/6/1990');


create table Afiliado (
	ID_Cliente varchar (8),
	puntos numeric (15,0),
    fecha date,
    primary key (ID_Cliente),
	foreign key (ID_Cliente) references Cliente
		on delete cascade
);

insert into Afiliado (ID_Cliente, puntos, fecha) values (25021709, 73115422, '8/7/2019');
insert into Afiliado (ID_Cliente, puntos, fecha) values (25399720, 48326798, '7/1/2018');
insert into Afiliado (ID_Cliente, puntos, fecha) values (26044929, 29777845, '7/4/2018');
insert into Afiliado (ID_Cliente, puntos, fecha) values (26118740, 64145287, '2/21/2019');
insert into Afiliado (ID_Cliente, puntos, fecha) values (24997875, 16701050, '7/12/2018');
insert into Afiliado (ID_Cliente, puntos, fecha) values (25619359, 91948793, '1/19/2019');
insert into Afiliado (ID_Cliente, puntos, fecha) values (24776966, 61027902, '2/19/2020');
insert into Afiliado (ID_Cliente, puntos, fecha) values (27205181, 77602299, '5/22/2020');
insert into Afiliado (ID_Cliente, puntos, fecha) values (27651832, 97954860, '9/7/2018');
insert into Afiliado (ID_Cliente, puntos, fecha) values (25300265, 79125628, '12/31/2019');
insert into Afiliado (ID_Cliente, puntos, fecha) values (27408935, 3980860, '9/2/2018');
insert into Afiliado (ID_Cliente, puntos, fecha) values (24846813, 68522885, '11/13/2019');
insert into Afiliado (ID_Cliente, puntos, fecha) values (24714462, 31311721, '10/20/2018');
insert into Afiliado (ID_Cliente, puntos, fecha) values (27669949, 38812618, '5/15/2019');
insert into Afiliado (ID_Cliente, puntos, fecha) values (25259010, 2204526, '11/5/2018');

create table Estante (
	ID_Estante varchar (4),
	pasillo numeric (2,0),
    max_capacidad numeric (3,0),
    temp numeric (3,1),
    ID_Sucursal varchar(4),
    primary key (ID_Estante),
	foreign key (ID_Sucursal) references Sucursal
		on delete cascade
);

insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2064, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2065, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2066, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2067, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2068, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2069, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2070, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2071, 1, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2072, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2073, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2074, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2075, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2076, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2077, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2078, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2079, 2, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2080, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2081, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2082, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2083, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2084, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2085, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2086, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2087, 3, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2088, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2089, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2090, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2091, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2092, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2093, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2094, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2095, 4, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2096, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2097, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2098, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2099, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2100, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2101, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2102, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2103, 5, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2104, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2105, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2106, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2107, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2108, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2109, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2110, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2111, 6, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2112, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2113, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2114, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2115, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2116, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2117, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2118, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2119, 7, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2120, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2121, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2122, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2123, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2124, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2125, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2126, 8, 100, 1001);
insert into Estante (ID_Estante, pasillo, max_capacidad, ID_Sucursal) values (2127, 8, 100, 1001);

create table Producto (
	ID_Producto varchar (4),
	nombre varchar (50),
    ID_Categoria varchar(4),
    primary key (ID_Producto)
);

insert into Producto (ID_Producto, nombre, ID_Categoria) values (3001, 'Chocolate de leche Nestle', 9003);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3002, 'Lechuga', 9002);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3003, 'Coca cola 1.5', 9000);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3004, 'Jamon de pavo Movilla', 9001);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3005, 'Rikomalt 1', 9000);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3006, 'Colgate', 9004);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3007, 'Listerine Cool mint', 9004);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3008, 'Manzana verde', 9002);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3009, 'Chistorra La Monserratina', 9001);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3010, 'Doritos 200', 9003);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3011, 'Natuchip verdes 500', 9003);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3012, 'Jugo de naranja 1', 9000);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3013, 'Carne molina', 9001);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3014, 'Head & shoulders', 9004);
insert into Producto (ID_Producto, nombre, ID_Categoria) values (3015, 'Toallitas humedas Huggies', 9000);

create table Costo_Producto (
	ID_Producto varchar (4),
	precio numeric (12,2),
    fecha date,
    primary key (ID_Producto),
    foreign key (ID_Producto) references producto
        on delete cascade
);

insert into Costo_Producto (ID_Producto, precio, fecha) values (3001, 296704.36, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3002, 280285.61, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3003, 449715.77, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3004, 1057298.82, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3005, 823668.87, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3006, 392321.58, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3007, 545688.41, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3008, 1799784.92, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3009, 1402175.0, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3010, 448480.98, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3011, 431408.94, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3012, 372055.5, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3013, 1192078.52, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3014, 805312.1, '6/15/2020');
insert into Costo_Producto (ID_Producto, precio, fecha) values (3015, 312699.39, '6/15/2020');

create table Inventario (
	ID_Estante varchar (4),
	ID_Producto varchar (4),
    primary key (ID_Estante, ID_Producto),
    foreign key (ID_Estante) references estante
        on delete cascade
);

insert into Inventario (ID_Estante, ID_Producto) values (2001, 3001);
insert into Inventario (ID_Estante, ID_Producto) values (2124, 3001);
insert into Inventario (ID_Estante, ID_Producto) values (2005, 3002);
insert into Inventario (ID_Estante, ID_Producto) values (2104, 3002);
insert into Inventario (ID_Estante, ID_Producto) values (2004, 3003);
insert into Inventario (ID_Estante, ID_Producto) values (2090, 3003);
insert into Inventario (ID_Estante, ID_Producto) values (2009, 3004);
insert into Inventario (ID_Estante, ID_Producto) values (2069, 3004);
insert into Inventario (ID_Estante, ID_Producto) values (2020, 3005);
insert into Inventario (ID_Estante, ID_Producto) values (2109, 3005);
insert into Inventario (ID_Estante, ID_Producto) values (2045, 3006);
insert into Inventario (ID_Estante, ID_Producto) values (2027, 3007);
insert into Inventario (ID_Estante, ID_Producto) values (2080, 3008);
insert into Inventario (ID_Estante, ID_Producto) values (2002, 3008);
insert into Inventario (ID_Estante, ID_Producto) values (2083, 3009);
insert into Inventario (ID_Estante, ID_Producto) values (2100, 3010);
insert into Inventario (ID_Estante, ID_Producto) values (2073, 3011);
insert into Inventario (ID_Estante, ID_Producto) values (2112, 3012);
insert into Inventario (ID_Estante, ID_Producto) values (2004, 3012);
insert into Inventario (ID_Estante, ID_Producto) values (2064, 3013);
insert into Inventario (ID_Estante, ID_Producto) values (2022, 3013);
insert into Inventario (ID_Estante, ID_Producto) values (2120, 3014);
insert into Inventario (ID_Estante, ID_Producto) values (2127, 3015);

create table Compra (
	ID_Compra varchar (4),
    ID_Cliente varchar (8),
    fecha date,
    ID_Product varchar (4),
    cant numeric (3,0),
    ID_Factura varchar (4),
    ID_Sucursal varchar (4),
    primary key (ID_Compra, ID_Product),
    foreign key (ID_Sucursal) references sucursal
        on delete cascade
);

insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6001, 25021709, '10/24/2019', 3001, 3, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6001, 25021709, '10/24/2019', 3004, 2, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6001, 25021709, '10/24/2019', 3010, 3, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6001, 25021709, '10/24/2019', 3006, 1, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6001, 25021709, '10/24/2019', 3015, 4, 1000);

insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6002, 25399720, '8/30/2019', 3002, 2, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6002, 25399720, '8/30/2019', 3006, 2, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6002, 25399720, '8/30/2019', 3010, 1, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6002, 25399720, '8/30/2019', 3003, 1, 1000);
insert into Compra (ID_Compra, ID_Cliente, fecha, ID_Product, cant, ID_Sucursal) values (6002, 25399720, '8/30/2019', 3009, 2, 1000);

create table Factura (
	ID_Factura varchar (4),
    total numeric (12,0),
    fecha date,
    ID_Banco varchar (4),
    ID_Compra varchar (4),
    primary key (ID_Factura)
);

insert into Factura (ID_Factura, fecha, ID_Banco, ID_Compra) values (4001, '10/24/2019', 2, 6001);
insert into Factura (ID_Factura, fecha, ID_Banco, ID_Compra) values (4002, '8/30/2019', 1, 6001);

create table Visita (
	ID_Cliente varchar (4),
    fecha date,
    ID_Sucursal varchar (4),
    primary key (ID_Cliente, fecha, ID_Sucursal)
);

insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25021709, '10/24/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25399720, '9/16/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26044929, '9/24/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25399720, '8/30/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26118740, '3/16/2020', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25619359, '9/24/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24997875, '4/23/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25021709, '11/5/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26118740, '12/1/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24776966, '1/2/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26044929, '9/10/2018', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27205181, '5/9/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24776966, '3/17/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25619359, '4/8/2020', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27651832, '1/2/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24997875, '11/3/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27205181, '11/18/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27408935, '7/12/2018', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24846813, '11/23/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25300265, '7/7/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25259010, '5/29/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27408935, '5/24/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24846813, '7/23/2018', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27669949, '5/7/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27408935, '5/20/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26066636, '11/1/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27651832, '6/28/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24714462, '11/15/2018', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26566783, '3/18/2020', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24714462, '8/8/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26566783, '8/28/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24807501, '11/9/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25300265, '2/14/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25259010, '3/4/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27669949, '1/18/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27669949, '8/23/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24714462, '5/5/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24807501, '2/12/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25259010, '7/20/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (26566783, '9/28/2018', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25515100, '7/21/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24077324, '8/20/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24807501, '12/17/2018', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25515100, '1/3/2020', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (25515100, '12/2/2019', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24077324, '5/13/2020', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (24077324, '2/4/2019', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27937999, '7/27/2018', 0);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27937999, '8/18/2018', 1);
insert into Visita (ID_Cliente, fecha, ID_Sucursal) values (27937999, '3/23/2019', 1);

