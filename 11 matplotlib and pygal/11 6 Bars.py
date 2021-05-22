import matplotlib.pyplot as plt

left = [2,7,12,17,22,27]
heights = [22,17,8,9,7,6]

bar_width = 4

plt.bar(left,heights,bar_width,color=('r','black','g','b','yellow','xkcd:cyan'))

plt.title('Popularność języków programowania\n Paulina Pieper')
plt.xlabel('Język programowania')
plt.ylabel('Popularność')

plt.xticks([2,7,12,17,22,27],['Java','Python','PHP','JavaScript','C#','C++'])
plt.yticks([0,5,10,15,20])

plt.grid(True)
plt.grid(color='red' )
plt.minorticks_on()

plt.show()