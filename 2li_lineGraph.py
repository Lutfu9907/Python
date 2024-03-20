import matplotlib.pyplot as plt

x1 = [1, 2, 3]
y1 = [2, 4, 1]

plt.plot(x1, y1, label="çizgi 1")

x2 = [1, 2, 3]
y2 = [4, 1, 3]

plt.plot(x2, y2, label="çizgi 2")

plt.xlabel('x-ekseni')
plt.ylabel('y-ekseni')
plt.title('2 çizgi aynı grafikte!')

plt.legend()
plt.show()