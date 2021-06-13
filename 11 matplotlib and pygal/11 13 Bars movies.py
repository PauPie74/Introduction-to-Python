import matplotlib.pyplot as plt

labels = ['Avengers: Endgame', 'Avatar', 'Titanic', 'Star Wars VII', 'Avengers: Infinity War','Jurassic World','The Lion King','The Avengers','Furious 7','Frozen 2']
budget = [0.4, 0.237, 0.2, 0.3, 0.4, 0.15, 0.26, 0.22, 0.25, 0.15]
box = [2.8, 2.79, 2.19, 2.06, 2.04,1.67,1.65,1.518,1.516,1.45]
width = 0.5

fig, ax = plt.subplots()

ax.bar(labels, budget, width, label='Budget',color = 'red', edgecolor='black')
ax.bar(labels, box, width, bottom=budget,
       label='box_office', color = 'blue', edgecolor='black')


ax.tick_params(axis='x', rotation=90)
ax.set_title('Highest-grossin movies')
ax.legend(edgecolor='black')

ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])

fig.patch.set_facecolor('xkcd:silver')

plt.show()