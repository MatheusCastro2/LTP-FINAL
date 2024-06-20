from banco import SQL
import random
import string


class Action:
    def __init__(self):
        self.mysql = SQL()

    def login(self, usr, pwd):
        # Consulta um registro de usuário se usuário e senha criptografada for iguais a
        # algum registro no banco de dados
        cmd = "SELECT * FROM usuario WHERE nome = %s AND senha = SHA(%s);"
        obj = self.mysql.get_object(cmd, [usr, pwd])
        return obj

    def alterar_senha(self, idt_usr, senha_atual, senha, confirma):
        # Consultar se a senha atual é mesmo a senha que está no banco para o usuário logado
        cmd = "SELECT COUNT(id_usuario) as qtd FROM usuario WHERE id_usuario=%s AND senha=SHA(%s);"
        num = self.mysql.get_int(cmd, [idt_usr, senha_atual])
        # Validou que a senha atual informada é igual a atual no banco
        if num == 1:
            # Verifica se a senha nova e igual a confirmação
            if senha == confirma:
                cmd = "UPDATE usuario SET senha=SHA(%s) WHERE id_usuario=%s;"
                ret = self.mysql.upd_del(cmd, [senha, idt_usr])
                # Alterou a senha com sucesso
                if ret == 1:
                    return "Senha alterada com sucesso."
                else:
                    return "Erro ao tentar mudar a senha"
            else:
                return "Senha nova e confirmação não são iguais!"
        else:
            return "Senha atual está errada!"


    def resetar_senha(self, nme_usr):
        # Gerar 8 caracteres aleatorios
        caracteres = string.ascii_letters + string.digits

        senha = ""
        for i in range(8):
            senha += random.choice(caracteres)

        cmd = "UPDATE tb_usr SET pwd_usr=SHA(%s) WHERE nme_usr=%s;"
        ret = self.mysql.upd_del(cmd, [senha, nme_usr])
        # Alterou a senha com sucesso
        if ret == 1:
            return senha
        else:
            return "Erro ao tentar mudar a senha"

    def incluir(self, nme_usr, eml_usr, pwd_usr, pfl_usr):
        cmd = "INSERT INTO tb_usr (nme_usr, eml_usr, pwd_usr, pfl_usr) VALUES (%s, %s, SHA(%s), %s);"
        ret = self.mysql.insert(cmd, [nme_usr, eml_usr, pwd_usr, pfl_usr])
        # Inseriu usuário com sucesso
        if ret > 0:
            return (ret, pwd_usr)
        else:
            return "Erro ao tentar inserir usuário"

    def listar(self, nme_usr, pfl_usr):
        cmd = '''SELECT * FROM usuario
                WHERE nome LIKE CONCAT('%', %s, '%') AND (tipo_usuario = %s OR %s = 'T')
                ORDER BY nome ASC;'''

        lista = self.mysql.get_list(cmd, [nme_usr, pfl_usr, pfl_usr])
        return lista

    def get_usuario(self, idt_usr):
        cmd = 'SELECT * FROM usuario where id_usuario = %s;'

        obj = self.mysql.get_object(cmd, [idt_usr])
        return obj

    def alterar(self, idt_usr, nme_usr, eml_usr, pwd_usr, pfl_usr):
        cmd = "UPDATE usuario SET nome=%s, email=%s, senha=SHA(%s), tipo_usuario=%s WHERE id_usuario = %s;"
        ret = self.mysql.upd_del(cmd, [nme_usr, eml_usr, pwd_usr, pfl_usr, idt_usr])
        # Alterou usuário com sucesso
        if ret > 0:
            return "Usuário alterado com sucesso"
        else:
            return "Nada a alterar ou erro ao tentar alterar o usuário"

    def excluir(self, idt_usr):
        cmd = "DELETE FROM usuario WHERE id_usuario = %s;"
        ret = self.mysql.upd_del(cmd, [idt_usr])
        # Excluiu usuário com sucesso
        if ret > 0:
            return "Usuário excluido com sucesso"
        else:
            return "Nada a excluir ou erro ao tentar excluir o usuário"
