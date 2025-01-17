from matplotlib import pyplot

x = list(range(-10, 11))
y = []
for i in x:
    y.append(i**2)

pyplot.plot(x, y, color='red')
pyplot.show()
