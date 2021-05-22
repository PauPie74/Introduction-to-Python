import matplotlib.pyplot as plt

y_cords = [1,5,10,18,20]
x_cords = [2,3,5,6,8]

yr_cords = [2,6,11,20,22]
xr_cords = [3,4,6,7,9]
plt.plot(x_cords, y_cords, 'b*')
plt.plot(xr_cords, yr_cords, 'ro')
plt.title("Paulina Pieper")

plt.xticks([1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

plt.grid(True)

plt.show()