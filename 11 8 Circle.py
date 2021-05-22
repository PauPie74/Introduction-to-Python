import matplotlib.pyplot as plt

labels = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
sizes = [31.3,24.8,12.4,11.3,10.8,9.4]
explode = (0.1,0, 0, 0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=140, colors = ('r','xkcd:yellow','xkcd:lime','b','xkcd:salmon','xkcd:light blue'))
ax1.axis('equal')


plt.title('Popularność języków programowania\n Paulina Pieper')

plt.show()