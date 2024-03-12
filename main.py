
# -*- coding: utf-8 -*-
import pandas as pd

from ProjetoPacotes.Email import EmailAut
from defProjeto import *
from email import *

df = pd.read_csv('housing.csv')

df.to_excel('housing.xlsx', index=False)

# precisa primeiro criar a pasta
caminho_anexo = criar_pasta_anexo()

dados_filtrados = leitura_dados(df)

# vou criar um arquivo txt para cada item filtrado
for indice, imovel in enumerate(dados_filtrados['imoveis'], start=1):
    texto_formatado = criar_texto_formatado(imovel)
    caminho_documento = f'C:\\Users\\Gomes\\PycharmProjects\\Projeto2\\ProjetoPacotes\\anexos\\imovel_{indice}.txt'

    with open(caminho_documento, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto_formatado)

# mover para a pasta anexo criada
mover_arquivos_txt_para_anexo(f'C:\\Users\\Gomes\\PycharmProjects\\Projeto2\\ProjetoPacotes', caminho_anexo)

#bloco alteravel
if __name__ == '__main__':
    enviando = EmailAut(destinatario="karython.unai@gmail.com",
                        assunto="Relatório de Imóveis",
                        conteudo="Segue anexado a este, o detalhamento de cada imóvel que atende aos filtros de buscas.\nEu criei um novo projeto "
                                 "em outro diretório para o teste ficar melhor e meu codigo ficar separado dos outros arquivos do seu repositório"
                                 "copiei os arquivos .csv e instalei o pacote openpyxl para executar.\nDepois me diz se é possível eu enviar para dois emails simultaneamente.\n\nAT.",
                        anexos=1)
    enviando.envio()