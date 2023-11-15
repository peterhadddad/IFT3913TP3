import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


#Creation du dataframe
df = pd.read_csv('jfreechart-test-stats.csv')

#Creation des pairs spéficiques de métriques afin de déterminer leur correlation
tloc_tassert = df[['TLOC', ' TASSERT']]
tloc_wmc = df[['TLOC', ' WMC']]
tassert_wmc = df[[' WMC', ' TASSERT']]

#Trouver les coéfficients de corrélation des pairs de métriques
tloc_tassert.corr()
tloc_wmc.corr()
tassert_wmc.corr()
print(tloc_tassert.corr())
print(tloc_wmc.corr())
print(tassert_wmc.corr())


##Déterminer les SCATTER PLOTS et les RÉGRESSIONS LINÉAIRES des pairs de métriques ##
#TLOC et TASSERT
regression_TT = np.polyfit(tloc_tassert['TLOC'], tloc_tassert[' TASSERT'], deg = 1)
trend_TT = np.polyval(regression_TT, tloc_tassert['TLOC'])
plt.scatter(tloc_tassert['TLOC'], tloc_tassert[' TASSERT'])
plt.plot(tloc_tassert['TLOC'], trend_TT)
plt.xlabel('TLOC')
plt.ylabel('TASSERT')
plt.title('Scatter Plot et Régression Linéaire de TLOC et TASSERT')
print("\nRégression linéaire de TLOC et TASSERT: Y = " + str(regression_TT[0]) + 'x + ' + str(regression_TT[1]) )
plt.show()

#TLOC et WMC
regression_TW = np.polyfit(tloc_wmc['TLOC'], tloc_wmc[' WMC'], deg = 1)
trend_TW = np.polyval(regression_TW, tloc_wmc['TLOC'])
plt.scatter(tloc_wmc['TLOC'], tloc_wmc[' WMC'])
plt.plot(tloc_wmc['TLOC'], trend_TW)
plt.xlabel('TLOC')
plt.ylabel('WMC')
plt.title('Scatter Plot et Régression Linéaire de TLOC et WMC')
print("\nRégression linéaire de TLOC et WMC: Y = " + str(regression_TW[0]) + 'x + ' + str(regression_TW[1]) )
plt.show()

#TASSERT et WMC
regression_TassW = np.polyfit(tassert_wmc[' TASSERT'], tassert_wmc[' WMC'], deg = 1)
trend_TassW = np.polyval(regression_TassW, tassert_wmc[' TASSERT'])
plt.scatter(tassert_wmc[' TASSERT'], tassert_wmc[' WMC'])
plt.plot(tassert_wmc[' TASSERT'], trend_TassW)
plt.xlabel('TASSERT')
plt.ylabel('WMC')
plt.title('Scatter Plot et Régression Linéaire de TASSERT et WMC')
print("\nRégression linéaire de TASSERT et WMC: Y = " + str(regression_TassW[0]) + 'x + ' + str(regression_TassW[1]) )
plt.show()








