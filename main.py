import os
import platform
import mysql.connector
from mysql.connector import Error
#import pandas as pd
#import datetime
global z


def create_server_connectionprev(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        #print("Banco de Dados MySQL conectado com sucesso!")
    except Error as err:
        print(f"Erro: '{err}'")

    return connection

#Passa os parâmetros e cria uma conexão com o Banco de Dados
connectionprev = create_server_connectionprev("localhost", "root", "@Tech2022")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Banco de Dados MySQL Reconectado com sucesso!")
    except Error as err:
        print(f"Erro: '{err}'")
    
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Banco de Dados criado com sucesso!")
    except Error as err:
        print(f"Erro: '{err}'")

    return connection

#Criação do Banco de Dados
create_database_query = "CREATE DATABASE IF NOT EXISTS hotelnovo"
create_database(connectionprev, create_database_query)

#Passa os parâmetros e cria uma conexão com o Banco de Dados
connection = create_db_connection("localhost", "root", "@Tech2022", "hotelnovo")
mycursor=connection.cursor()

#Criação de consulta no bd
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        #print("Query executada com sucesso!")
    except Error as err:
        print(f"Erro: '{err}'")

#Criação de Tabelas: Hóspede
create_hospede_table = """
CREATE TABLE IF NOT EXISTS custdata (
  custname VARCHAR(20) NOT NULL,
  addr VARCHAR(30) NOT NULL,
  indate VARCHAR(10) NOT NULL,
  outdate VARCHAR(10) NOT NULL
  );
 """

#Criação de Tabelas: Quarto
create_quarto_table = """
CREATE TABLE IF NOT EXISTS roomtype (
  sno VARCHAR(5) NOT NULL,
  roomtype VARCHAR(20) NOT NULL,
  rent INTEGER(10)
  );
 """

#Criação de Tabelas: Itens Restaurante
create_restaurante_table = """
CREATE TABLE IF NOT EXISTS restaurent (
  sno INTEGER(10),
  itemname VARCHAR(30) NOT NULL,
  rent INTEGER(10)
  );
 """

#Criação de Tabelas: Itens Lavanderia
create_lavanderia_table = """
CREATE TABLE IF NOT EXISTS laundary (
  sno INTEGER(10),
  itemname VARCHAR(10) NOT NULL,
  rate INTEGER(10)
  );
 """

#Executa as Querys de criação de tabelas
execute_query(connection, create_hospede_table)
execute_query(connection, create_quarto_table)
execute_query(connection, create_restaurante_table)
execute_query(connection, create_lavanderia_table)

#Inserção de Dados Tabela Quartos
pop_room = """
INSERT INTO roomtype VALUES
('1','Tipo Simples',150),
('2','Tipo Duplo',200), 
('3','Tipo Casal',300),
('4','Tipo Luxo',500);
"""

#Inserção de Dados Tabela Restaurante
pop_restaurent = """
INSERT INTO restaurent VALUES
(1,"cha",4),
(2,"cafe",4), 
(3,"leite",4),
(4,"salgado",5),
(5,"sanduiche",6),
(6,"sorteve",10),
(7,"refrigerante",5),
(8,"pizza",20),
(9,"picacha",80),
(10,"peixe",60);
"""

#Inserção de Dados Tabela Lavanderia
pop_laundary = """
INSERT INTO laundary VALUES
(1,"calcas",15),
(2,"camisa",10), 
(3,"casaco",20),
(4,"terno",50);
"""


#Executa as Querys de inserção de dados
execute_query(connection, pop_room)
execute_query(connection, pop_laundary)
execute_query(connection, pop_restaurent)


def registercust():
    L=[]
    name=input("Digite o nome:")
    L.append(name)
    addr=input("Digite o Endereço:")
    L.append(addr)
    indate=input("Digite a data do Check-In:")
    L.append(indate)
    outdate=input("Digite a data do Check-Out:")
    L.append(outdate)
    cust=(L)
    sql="insert into custdata(custname,addr,indate,outdate)values(%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    connection.commit()
 
def roomtypeview():
    print("Deseja ver os tipos de Quarto Disponíveis? Digite 1 para Sim:")
    ch=int(input("Digite sua escolha:"))
    if ch==1:
        sql="select * from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)

def roomrent():
    print ("Nós possuímos os seguintes quartos:-")
    print ("1. Simples---->R$ 150,00")
    print ("2. Duplo---->R$ 200,00")
    print ("3. Casal---->R$ 300,00")
    print ("4. Luxo---->R$ 500,00")
    
    x=int(input("Digite sua escolha->"))
    n=int(input("Por quantas noites deseja ficar?:"))
    
    if(x==1):
        print ("Você escolheu o quarto Simples---->R$ 150,00")
        s=150*n
    elif (x==2):
        print ("Você escolheu o quarto Duplo---->R$ 200,00")
        s=200*n
    elif (x==3):
        print ("Você escolheu o quarto Casal---->R$ 300,00")
        s=300*n
    elif (x==4):
        print ("Você escolheu o quarto Luxo---->R$ 500,00")
        s=500*n
    else:
        print ("Por favor digite o número correspondente ao quarto.")
    print ("Sua estadia vai custar R${},00.".format(s))

def restaurentmenuview():
    print("Deseja ver o Menu do restaurante? Digite 1 para SIM:")
    ch=int(input("Digite sua escolha: "))
    if ch==1:
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)

def orderitem():
    global s
    print("Deseja ver os itens disponíveis? Digite 1 para SIM:")
    ch=int(input("Digite sua escolha:"))
    if ch==1:
        sql="select * from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)

    print("Deseja comprar algum item da lista?")
    d=int(input("Digite sua escolha:"))
    if(d==1):
        print("Você solicitou Chá")
        a=int(input("Digite a quantidade:"))
        s=4*a
        print("O valor do seu Chá é:",s,"\n")
    elif (d==2):
        print("Você solicitou Café")
        a=int(input("Digite a quantidade:"))
        s=4*a
        print("O valor do seu Café é::",s,"\n")
    elif(d==3):
        print("Você solicitou Leite")
        a=int(input("Digite a quantidade:"))
        s=4*a
        print("O valor do seu Leite é:",s,"\n")
    elif(d==4):
        print("Você solicitou Salgado")
        a=int(input("Digite a quantidade:"))
        s=5*a
        print("O valor do seu Salgado é:",s,"\n")
    elif(d==5):
        print("Você solicitou Sanduíche")
        a=int(input("Digite a quantidade:"))
        s=6*a
        print("O valor do seu Sanduíche é:",s,"\n")
    elif(d==6):
        print("Você solicitou Sorvete")
        a=int(input("Digite a quantidade:"))
        s=10*a
        print("O valor do seu Sorvete é:",s,"\n")
    elif(d==7):
        print("Você solicitou Refrigerante")
        a=int(input("Digite a quantidade:"))
        s=5*a
        print("O valor do seu Refrigerante é:",s,"\n")
    elif(d==8):
        print("Você solicitou Pizza")
        a=int(input("Digite a quantidade:"))
        s=20*a
        print("O valor da sua Pizza é:",s,"\n")
    elif(d==9):
        print("Você solicitou Picanha")
        a=int(input("Digite a quantidade:"))
        s=80*a
        print("O valor da sua Picanha é:",s,"\n")
    elif(d==10):
        print("Você solicitou Peixe")
        a=int(input("Digite a quantidade:"))
        s=60*a
        print("O valor do seu Peixe é:",s,"\n")
    else:
        print("Por favor digite uma ecolha do menu!")

def laundarybill():
    global z
    print("Deseja ver os serviços de Lavanteria? Digite 1 para sim :")
    ch=int(input("Digite sua escolha:"))
    if ch==1:
        sql="select * from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    y=int(input("Digite o número de peças->"))
    z=y*10
    print("O valor total dos serviços é:",z,"\n")
    return z

def lb():
    print(z)

def res():
    print(s)

def viewbill():
    a=input("Digite o nome do Cliente:")
    print("Cliente :",a,"\n")
    print("valor da Lavanderia:")
    print(lb)
    print("Valor do Restaurante:")
    print(res)

def Menuset():
    print("\nSISTEMA DE HOTELARIA")
    print("\n1: Para cadastro de Hóspede")
    print("2: Para visualizar os tipos de quarto")
    print("3: Para calcular o valor da reserva")
    print("4: Para visualizar o menu do Restaurante")
    print("5: Para realizar compra no restaurante")
    print("6: Para solcitar serviços de lavanderia")
    print("7: Para relatório completo de compras")
    print("8: Para finalizar o programa")
    try:
        userinput=int(input("Digite sua opção:"))
    except ValueError:
        exit("\n Isso não é uma opção correta!")
    
    if(userinput==1):
        registercust()
    elif(userinput==2):
        roomtypeview()
    elif(userinput==3):
        roomrent()
    elif(userinput==4):
        restaurentmenuview()
    elif(userinput==5):
        orderitem()
    elif(userinput==6):
        laundarybill()
    elif(userinput==7):
        viewbill()
    elif(userinput==8):
        quit()
    else:
        print("Digite uma escolha válida!")

Menuset()
def runagain():
    runagn=input("\n Retornar ao Menu Inicial? s/n:")
    while(runagn.lower()=='s'):
        if(platform.system()=="Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input("\n Retornar ao Menu Inicial? s/n:")

runagain()