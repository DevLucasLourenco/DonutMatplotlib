import matplotlib.pyplot as plt


fig, ax = plt.subplots()
circle = plt.Circle((0,0), 0.64, color='white')
lbls = ['A','B','C','D',]


ax.pie([8,10,8,1],
        labels=lbls,
        autopct='%1.1f%%',
        pctdistance=.82)

ax.add_artist(circle)
ax.set_title('Alguma Coisa', fontsize=20)


plt.show()
        
