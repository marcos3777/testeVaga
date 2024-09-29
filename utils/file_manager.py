import json
import xml.etree.ElementTree as ET

#Caminhos dos arquivos
caminho_json = r'C:\Users\Thanatos\Documents\testeVaga\data\dados.json'
caminho_xml = r'C:\Users\Thanatos\Documents\testeVaga\data\dados2.xml'

#DEF para ler JSON
def ler_valor_json(caminho_arquivo_json, dia_alvo):
    with open(caminho_arquivo_json, 'r') as file:
        dados = json.load(file)
    
    for item in dados:
        if item['dia'] == dia_alvo:
            return item['valor']
    
    return None

#DEF para ler XML
def ler_valor_xml(caminho_arquivo_xml, dia_alvo):
    tree = ET.parse(caminho_arquivo_xml)
    root = tree.getroot()
    
    for row in root.findall('row'):
        dia = row.find('dia').text
        if dia == str(dia_alvo):
            return float(row.find('valor').text)
    
    return None

#DEF para atualizar JSON
def atualizar_json(caminho_arquivo_json, dia_alvo, novo_valor):
    with open(caminho_arquivo_json, 'r') as file:
        dados = json.load(file)
    
    for item in dados:
        if item['dia'] == dia_alvo:
            item['valor'] = novo_valor
            break
    
    with open(caminho_arquivo_json, 'w') as file:
        json.dump(dados, file, indent=4)

#DEF para atualizar XML
def atualizar_xml(caminho_arquivo_xml, dia_alvo, novo_valor):
    tree = ET.parse(caminho_arquivo_xml)
    root = tree.getroot()
    
    for row in root.findall('row'):
        dia = row.find('dia').text
        if dia == str(dia_alvo):
            row.find('valor').text = f"{novo_valor:.4f}"
            break
    
    tree.write(caminho_arquivo_xml)



#Teste de leitura
valor_json = ler_valor_json(caminho_json, 4)
valor_xml = ler_valor_xml(caminho_xml, 2)
print(f"Valor JSON dia 4: {valor_json}")
print(f"Valor XML dia 2: {valor_xml}")

#atualizar_json(caminho_json, 2, 30000.00)
#atualizar_xml(caminho_xml, 2, 30000.00)