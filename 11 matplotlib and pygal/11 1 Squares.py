import matplotlib.pyplot as plt
input_values = range(1,6)
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5)
plt.title("Kwadraty liczb", fontsize = 24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Kwadraty wielkości", fontsize = 14)
plt.tick_params(axis='both',labelsize = 14)
plt.show()