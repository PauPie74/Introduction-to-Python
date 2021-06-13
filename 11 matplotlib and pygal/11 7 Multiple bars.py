import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men = [22, 30, 34, 30, 27]
women = [25, 32, 30, 35, 29]

x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men, width, label='Men', color='green')
rects2 = ax.bar(x + width/2, women, width, label='Women', color='red')

ax.set_ylabel('Wyniki')
ax.set_xlabel('Ludzie')
ax.set_title('Title')
ax.set_xticks([0,1,2,3,4])
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.minorticks_on()

plt.show()
