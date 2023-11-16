import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

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