# -*- coding: utf-8 -*-
import os
import shutil


def leitura_dados(df):
    filtro_preco = (df['price'] > 5000000) & (df['price'] < 5999999) & (df['area'] > 10000) & (df['area'] < 10999) & (
                df['bedrooms'] > 2)
    df_filtrado = df[filtro_preco]
    imoveis = df_filtrado.to_dict(orient='records')

    return {'imoveis': imoveis}


def criar_texto_formatado(imovel):
    texto_formatado = f"Preço: R$ {imovel['price']:,.2f} \n"
    texto_formatado += f"Área: {imovel['area']} metros quadrados \n"
    texto_formatado += f"Quartos: {imovel['bedrooms']} quartos \n"
    texto_formatado += "-" * 30 + "\n"

    return texto_formatado
print(criar_te)

def criar_pasta_anexo():
    caminho_anexo = 'C:\\Users\\Gomes\\PycharmProjects\\Projeto2\\ProjetoPacotes\\anexos'

    # verificar se a pasta já existe
    if not os.path.exists(caminho_anexo):
        os.makedirs(caminho_anexo)

    return caminho_anexo

# mover os arquivos .txt da raiz do projeto para uma pasta
def mover_arquivos_txt_para_anexo(diretorio_origem, caminho_anexo):
    arquivos_origem = os.listdir(diretorio_origem)

    arquivos_txt = [arquivo for arquivo in arquivos_origem if arquivo.endswith('.txt')]

    for arquivo in arquivos_txt:
        caminho_origem = os.path.join(diretorio_origem, arquivo)
        caminho_destino = os.path.join(caminho_anexo, arquivo)
        shutil.move(caminho_origem, caminho_destino)
