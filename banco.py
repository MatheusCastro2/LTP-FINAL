import mysql.connector

class SQL:
    def __init__(self, servidor='localhost', usr='root', pwd='matheus1234', esquema='ltp_projeto'):
        self.cnx = mysql.connector.connect(user=usr, password=pwd, host=servidor, database=esquema)
# a pessoa que for usar o banco de dados vai ter que passar o servidor, o usuário e a senha da propria maquina, esses ultilados sao da minha maquina pessoal



def insert(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    self.cnx.commit()
    idt = cs.lastrowid
    cs.close()
    return idt 

def upd_del(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    self.cnx.commit()
    num = cs.rowcount
    cs.close()
    return num

def get_cursor(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    return cs

def get_int(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando,params)
    ret = int(cs.fetchone()[0])
    cs.close()
    return ret


def get_float(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    ret = float(cs.fetchone()[0])
    cs.close()
    return ret

def get_date(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    data = cs.fetchone()[0]
    ret = str(data.day).zfill(2) + '/' + str(data.month).zfill(2) + '/' + str(data.year)
    cs.close()
    return ret


def get_time(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando,params)
    hora = cs.fetchone()[0]
    total_segundos = hora.total_seconds()
    horas = int(total_segundos // 3600)
    minutos = int((total_segundos % 3600) // 60)
    segundos = int(total_segundos % 60)
    ret = f"{horas:02}:{minutos:02}:{segundos:02}"
    return ret


def get_string(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    ret = cs.fetchone()[0]
    cs.close()
    return ret


def get_object(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    dados = cs.fetchone()
    if dados is None:
        dic = None
    else:
        md = cs.description
        dic = {col[0]: valor for col, valor in zip(md, dados)}
    cs.close()
    return dic


def get_list(self, comando, params=[]):
    cs = self.cnx.cursor()
    cs.execute(comando, params)
    md = cs.description
    list = []
    for reg in cs:
        dic = {col[0]: valor for col, valor in zip(md, reg)}
        list.append(dic)
    cs.close()
    return list


        