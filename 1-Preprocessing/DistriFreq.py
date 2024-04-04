import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    names = ['Idade', 'Sexo', 'TipoDorPeito','PressaoArterialRepouso', 'Colesterol', 'Glicemia', 'ResEletroCardio', 'FreqCardioMax', 'AnginaInduzExerc', 'PicoAnterior', 'Declive', 'VasosPrincAfetados', 'TesteEstresse', 'Resultado']

    input_file = '0-Datasets/HeartAttackModa.csv'


    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas
                 
    #ShowInformationDataFrame(df,"Dataframe original")

    QntClasse = 3
    TipoAtrib = 'C'

    if TipoAtrib == 'C':

        SepClasses = pd.cut(df['PHRefluxoNasogastrico'], bins=QntClasse)
        print(SepClasses)

        FreqAbs = SepClasses.value_counts().sort_index()

        FreqAbs.sort_values()
        print(FreqAbs)

        TotalObs = FreqAbs.sum()

        FreqRel = (FreqAbs / TotalObs)*100

        FreqRel = FreqRel.sort_index()

        print(FreqRel)

        plt.bar(FreqRel.index.astype(str), FreqRel.values)
        plt.xlabel('Classes')
        plt.ylabel('Frequência Absoluta')
    
        plt.show()

    else:
        coluna_desejada = df['RefluxoNasogastrico']
        print(coluna_desejada)

        FreqAbs = coluna_desejada.value_counts().sort_index()
        FreqAbs.sort_values()
        print(FreqAbs)

        TotalObs = FreqAbs.sum()

        FreqRel = (FreqAbs / TotalObs)*100

        FreqRel = FreqRel.sort_index()
        print(FreqRel)

        plt.bar(FreqRel.index.astype(str), FreqRel.values)
        plt.xlabel('Classes')
        plt.ylabel('Frequência Absoluta')
    
        plt.show()



    
    
if __name__ == "__main__":
    main()