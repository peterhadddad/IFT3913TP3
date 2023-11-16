import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math

df = pd.read_csv('jfreechart-test-stats.csv')

# Création des dataframes nécessaires pour les 2 groupes recherchés
plus_assert = df[df[' TASSERT'] >= 20]
moins_assert = df[df[' TASSERT'] < 20 ]

# Moyenne de WMC et TLOC pour les classes avec plus de 20 assertions
plus_avg_WMC = (plus_assert[' WMC'].sum())/len(df)
plus_avg_TLOC = (plus_assert['TLOC'].sum())/len(df)

# Moyenne de WMC et TLOC pour les classes avec moins de 20 assertions
moins_avg_WMC = (moins_assert[' WMC'].sum())/len(df)
moins_avg_TLOC = (moins_assert['TLOC'].sum())/len(df)

# Résultats
print("\nLes classes avec plus de 20 assertions contiennent en moyenne:")
print("TLOC: " + str(plus_avg_TLOC))
print("WMC " + str(plus_avg_WMC))

print("\nLes classes avec plus de 20 assertions contiennent en moyenne:")
print("TLOC: " + str(moins_avg_TLOC))
print("WMC " + str(moins_avg_WMC))



## Calcul du test t des 2 groupes recherchés afin de déterminer si nous pouvons rejeter l'hypothèse nulle ##

# Statistique WMC
t_WMC = (plus_avg_WMC - moins_avg_WMC) / (math.sqrt(((plus_avg_WMC ** 2) / (len(plus_assert) ** 2)) + ((moins_avg_WMC ** 2) / (len(moins_assert) ** 2))))
print("\nLe résultat de la statistique du test t pour WMC est: " + str(t_WMC))

# Statistique TLOC
t_TLOC = (plus_avg_TLOC - moins_avg_TLOC) / (math.sqrt(((plus_avg_TLOC ** 2) / (len(plus_assert) ** 2)) + ((moins_avg_TLOC ** 2) / (len(moins_assert) ** 2))))
print("\nLe résultat de la statistique du test t pour TLOC est: " + str(t_TLOC))

## Calcul des degrés de libertés ##
# WMC
deg = len(plus_assert) + len(moins_assert) - 2
print("\nLe degré de liberté est: " + str(deg))
