# Passo 1: Importar a base de dados

import pandas as pd;
import plotly.express as px;

# Passo 1: Importar a base de dados
tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
#-entender quais as informaçoes tao disponiveis
#-descobrir coisas erradas da base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)


# Passo 3: Tratamento de dados
#-valores que estao reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
#-valores vazios
tabela = tabela.dropna(how="all",axis=1)
tabela = tabela.dropna(how="any", axis=0)

# Passo 4: Análise Inicial
print(tabela.info())

# Como estão os nossos cancelamentos?
# Passo 5: Analise mais completa
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True))
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))


# comparar cada coluna da minha tabela com a coluna de cancelamento
# etapa : 6 criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela,x=coluna, color="Churn")
    # etapa 7 : exibir o gráfico
    grafico.show()