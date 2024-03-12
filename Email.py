# -*- coding: utf-8 -*-

import smtplib
import email.message
# from Autenticacao.credenciais import credenciais
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os


# Módulo para envio envio de e-mail com os documentos ao cliente
# Os documentos devem ser anexados dentro da pasta Email/Anexos
# Após o envio os documentos são apagados


class EmailAut:

    def __init__(self, destinatario, assunto, conteudo, anexos):
        self.destinatario = destinatario
        self.assunto = assunto
        self.conteudo = conteudo

        # Se anexos for igual a 1, o e-mail será enviado com os anexos
        self.anexos = anexos

        self.arquivos = []
        pasta = "anexos"
        if self.anexos == 1:
            for arquivo in os.listdir(pasta):
                caminho_completo = os.path.join(pasta, arquivo)
                self.arquivos.append(caminho_completo)

    def envio(self):
        msg = MIMEMultipart()
        msg.add_header('Content-Type', 'text/html')

        #depois preciso colocar essa senha em outro arquivo
        msg['From'] = "karython.unai@gmail.com"
        password = "xmyeaspfzxaeehyq"

        msg['Subject'] = self.assunto
        msg['To'] = self.destinatario
        msg.attach(MIMEText(self.conteudo, 'plain'))  # Adiciona o conteúdo do e-mail como parte da mensagem

        # Inclusão dos anexos
        if self.anexos == 1:
            for arquivo in self.arquivos:

                with open(arquivo, 'rb') as file:
                    nome_arquivo = os.path.basename(arquivo)

                    if 'github' in nome_arquivo:
                        continue

                    attachment = MIMEApplication(file.read(), 'octet-stream')
                    attachment.add_header('Content-Disposition', 'attachment', filename=nome_arquivo)
                    msg.attach(attachment)

        # Configura integração com Gmail
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print(f'Email enviado para {self.destinatario}')

# esse bloco vai ser copiado na main e alterado as informações
if __name__ == '__main__':
    enviando = EmailAut(destinatario="consultreds@gmail.com", # para enviar para mais de 1 email, mudar string para receber lista
                        assunto="Relatório de Imóveis",
                        conteudo="Email de teste para envio de relatorios do projeto 2",
                        anexos=1)
    enviando.envio()
