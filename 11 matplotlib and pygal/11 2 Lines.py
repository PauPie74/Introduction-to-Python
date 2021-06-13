import matplotlib.pyplot as plt

x_cords = [1,2,3]
y_cords = [2,4,1]
plt.plot(x_cords, y_cords)
plt.title("Title")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")

plt.xticks([1,1.25,1.50,1.75,2,2.25,2.50,2.75,3])
plt.yticks([1,1.5,2,2.5,3,3.5,4])

plt.grid(True)

plt.show()