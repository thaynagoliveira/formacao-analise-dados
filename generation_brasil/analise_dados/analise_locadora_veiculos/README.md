# Análise Exploratória e Limpeza de Dados - Locadora

Este projeto contém a análise de dados de uma locadora de veículos, com foco em preparar bases de diferentes formatos para análise consolidada.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UrVuR81Xid6Uefv19VZl_OQu_dfmHigg?usp=sharing)

## Objetivo
O objetivo principal foi realizar o tratamento de dados (Data Cleaning) e a Engenharia de Atributos para calcular métricas de negócio, como receita total e emissão de CO2 por locação.

## Etapas Realizadas
* **Tratamento de Nulos**: Identificação e preenchimento de valores ausentes em idades e taxas diárias.
* **Padronização**: Conversão de tipos de dados (strings para numéricos e datas).
* **Consolidação**: Cruzamento de bases de clientes, veículos e locações (Merge).
* **Engenharia de Dados**: Cálculo de duração das locações e extração de informações temporais (mês/ano).

## Estrutura de Arquivos
* `exploracao_de_dados.ipynb`: Notebook com todo o código e visualizações.
* `datasets/`: Pasta contendo os arquivos originais em CSV e JSON.