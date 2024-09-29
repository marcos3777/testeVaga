import json
import xml.etree.ElementTree as ET

# Caminhos dos arquivos
caminho_json = r'C:\Users\Thanatos\Documents\testeVaga\data\dados.json'
caminho_xml = r'C:\Users\Thanatos\Documents\testeVaga\data\dados2.xml'

# DEF para ler JSON
def ler_valor_json(caminho_arquivo_json):
    with open(caminho_arquivo_json, 'r') as file:
        return json.load(file)

# DEF para ler XML
def ler_valores_xml(caminho_arquivo_xml):
    tree = ET.parse(caminho_arquivo_xml)
    root = tree.getroot()
    
    valores = []
    for row in root.findall('row'):
        dia = int(row.find('dia').text)
        valor = float(row.find('valor').text)
        valores.append({'dia': dia, 'valor': valor})
    return valores

# Função para processar o faturamento e calcular os resultados
def processar_faturamento(fonte='json'):
    if fonte == 'json':
        dados = ler_valor_json(caminho_json)
    elif fonte == 'xml':
        dados = ler_valores_xml(caminho_xml)
    else:
        print("Fonte desconhecida!")
        return
    
    # Filtrando os dias com faturamento > 0
    faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

    # Verificando se há dias válidos para calcular
    if not faturamento_diario:
        print("Não há dados de faturamento para processar.")
        return

    # Calculando o menor e o maior faturamento
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)

    # Média mensal
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    # Dias com faturamento superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    # Resultados
    print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

# Chamada Função JSON e XML
print("Resultados para JSON:")
processar_faturamento('json')

print("\nResultados para XML:")
processar_faturamento('xml')
