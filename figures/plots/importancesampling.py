import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-(x - 2.2)**2)

def n(x, eta):
    return np.exp(-(x - 0)**2) - eta

def d(x, eta):
    return np.exp(-((x - 2.1) / 1.5)**2) - eta

def u(x):
    return 0.25 + x * 0.000000001

dispRatio = 1

t1 = np.arange(0.0, 2.5, 0.01)

a = plt.subplot2grid((1, 3), (0, 0))
a.plot(t1, f(t1), 'k')
a.plot(t1, n(t1, 0.0), 'b--')
a.set(aspect=1.0/a.get_data_ratio()*dispRatio, adjustable='box-forced')
plt.title('Bad')

frame = plt.gca()
frame.axes.get_xaxis().set_visible(False)
frame.axes.get_yaxis().set_visible(False)

b = plt.subplot2grid((1, 3), (0, 1))

b.plot(t1, f(t1), 'k')
b.plot(t1, u(t1), 'b--')
b.set(aspect=1.0/b.get_data_ratio()*dispRatio, adjustable='box-forced')
plt.title('Uniform')

frame = plt.gca()
frame.axes.get_xaxis().set_visible(False)
frame.axes.get_yaxis().set_visible(False)


c = plt.subplot2grid((1, 3), (0, 2))
c.plot(t1, f(t1), 'k')
c.plot(t1, d(t1, 0.1), 'b--')
c.set(aspect=1.0/c.get_data_ratio()*dispRatio, adjustable='box-forced')
frame = plt.gca()
frame.axes.get_xaxis().set_visible(False)
frame.axes.get_yaxis().set_visible(False)
plt.title('Good')

fig = plt.gcf()
fig.set_size_inches(15, 5)

#plt.show()
plt.savefig('importancesampling.pdf', bbox_inches='tight', dpi=1200)
