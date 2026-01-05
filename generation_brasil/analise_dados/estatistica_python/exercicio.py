import numpy as np
alturas = np.array([1.55,1.70,1.80])
media = np.mean(alturas)
# calcula a média de um conjunto de dados

desvio = np.std(alturas)
print(media)
print(desvio)

dias_semana1 = np.array([15,22,18,25,17,21])
media = np.mean(dias_semana1)
desvio = np.std(dias_semana1)

print(media)
print(desvio)

dias_semana2 = np.array([20,25,19,28,23,30])
media = np.mean(dias_semana2)
desvio = np.std(dias_semana2)

print(media)
print(desvio)