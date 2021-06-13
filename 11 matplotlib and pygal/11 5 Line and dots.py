import matplotlib.pyplot as plt

x_cords = [1,2,3,4,5]
y_cords = [772,776,777,778,775]
plt.plot(x_cords, y_cords,"co-")
plt.title("Title")

plt.xticks([1,2,3,4,5],['2019-10-03','2019-10-04','2019-10-05','2019-10-06','2019-10-07'])
plt.yticks([772,773,774,775,776,777,778])


plt.show()