import matplotlib.pyplot as plt
import pandas as pd
df_p = pd.DataFrame({'pays': ['etats-unis','chine','inde','japon'], 'population': [331002651, 1439323776,1380004385,126476461], 'superficie': [9629091, 9640011,3287263,377972], 'Taux de croissance annuel': [0.6, 0.4,1.1,-0.2]})
# print (df_p)
dict_pays=dict(df_p)
# print(dict_pays)
sorted(dict_pays['population'].items(), key=lambda t: t[0])
print(dict_pays)

df_p.plot(x="pays", y="population", kind="bar")
plt.xlabel('pays')
plt.ylabel('population')
plt.title('graphique a barres')
plt.show()

x=df_p['superficie']
y=df_p['Taux de croissance annuel']
plt.scatter(x, y)
plt.xlabel('Superficie')
plt.ylabel(' Taux de croissance annuel ')
plt.title('Nuage de points')
plt.show()