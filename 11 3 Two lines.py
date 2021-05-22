import matplotlib.pyplot as plt

x_cords = [10,20,30]
y_cords = [20,40,10]
x2_cords = [10,20,30]
y2_cords = [40,10,30]
plt.plot(x_cords, y_cords)
plt.plot(x2_cords,y2_cords)
plt.title("Paulina Pieper")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.xticks([10,12.5,15,17.5,20,22.5,25,27.5,30])
plt.yticks([10,15,20,25,30,35,40])

plt.grid(True)
plt.legend(labels = ("linia 1", "linia 2"),loc="best")
plt.show()