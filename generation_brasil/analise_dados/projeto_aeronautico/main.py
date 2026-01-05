import pandas as pd
# ler arquivos 
df_aviao = pd.read_csv("datasets/airplane.csv")
df_modelo = pd.read_csv("datasets/modelos.csv", sep=';') 

# ver a estrutura do modelos.csv
print("=== ESTRUTURA DO MODELOS.CSV ===")
print(df_modelo.head())
print("\nColunas:", df_modelo.columns.tolist())

print(df_aviao)

# coletar dados
id = input('Informe o ID:')
modelo = input('Informe o modelo:')
companhia = input('Informe a companhia:')
capacidade = input('Informe a capacidade:')
ano_fabricacao = input('Informe o ano de fabricação:')

novo_modelo = {
    'id': id, 
    'modelo': modelo,
    'companhia': companhia,
    'capacidade': capacidade, 
    'ano_fabricacao': ano_fabricacao
}

# adicionar o dado e salvar
df_modelo = pd.concat([df_modelo, pd.DataFrame([novo_modelo])], ignore_index=True)
df_modelo.to_csv("datasets/modelos.csv", sep=';', index=False)

print('Dados adicionados com sucesso!')

