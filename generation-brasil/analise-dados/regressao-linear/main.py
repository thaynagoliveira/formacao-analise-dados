# importar as bibliotecas para o sistema
# biblioteca de inteligência artificial 
from sklearn.linear_model import LinearRegression
# a inteligência artificial em geral não trabalha sozinha
# a IA depende de ferramentas para tratar os dados
import pandas as pd
# pandas para ler os dados
import matplotlib.pyplot as plt
# para mostrar os dados

# entrada de dados - ler os dados
# processamento de dados - interpretação dos dados
# saída de dados - exibição das informações

# 1 - LER
df_dados = pd.read_csv("dados.csv")
print(df_dados) # exibe tudo

# 2 - PROCESSAR OS DADOS
# var independente
x_independente = df_dados[["horas_estudo"]]
# var dependente 
y_dependente = df_dados[["nota"]]

# 2 - criar um modelo de regressão linear
modelo = LinearRegression()

# 2 - treinar o modelo 
modelo.fit(x_independente, y_dependente)

# 2 - exibir os dados
print("Coeficiente", modelo.coef_[0]) # inclinação
print("Interceptação", modelo.intercept_) # onde os pontos se encontram

# 3 - SAÍDA DOS DADOS
# 3 - o que eu quero prever? 
nova_hora = [[4]] # anota o que quer prever

# vou prever
prever = modelo.predict(nova_hora)
# mostrar a previsão
print("Estudando", nova_hora, "horas","sua nota será:", prever)

# SEMPRE A REGRESSÃO LINEAR, OU SEJA, A PREVISÃO DEVE TER DOIS GRÁFICOS EM UM 
# SENDO ELES O GRÁFICO DE DISPERSÃO COM O GRÁFICO DE LINHA
plt.plot(df_dados["horas_estudo"], modelo.predict(x_independente))
plt.scatter(df_dados["horas_estudo"], df_dados["nota"])

plt.show()
