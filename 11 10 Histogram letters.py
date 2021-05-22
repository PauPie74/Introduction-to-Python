import matplotlib.pyplot as plt



w1 = len('jedzie')
w2 = len('Andrzej')
w3 = len('rowerem')
w4 = len('ledwie')
w5 = len('dajac')
w6 = len('rade')
w7 = len('nogami')
#Jedzie Andrzej rowerem ledwie dając radę nogami

left = [2,7,12,17,22,27,32]
heights = [w1,w2,w3,w4,w5,w6,w7]

bar_width = 4

plt.bar(left,heights,bar_width)

plt.title("Paulina Pieper")
plt.xticks([2,7,12,17,22,27,32],['Jedzie', 'Andrzej', 'rowerem', 'ledwie', 'dając', 'radę', 'nogami'])

plt.minorticks_on()
plt.show()