import numpy as np   
a = np.array([1, 2, 3])
a

type(a)

a.dtype

a.ndim

a.size

a.shape

b = np.array([[1.3, 2.4],[0.3, 4.1]])
b.dtype

b.ndim

b.size

b.shape

#ways to create array
c = np.array([[1, 2, 3],[4, 5, 6]])
c
d = np.array(((1, 2, 3),(4, 5, 6)))
d
e = np.array([(1, 2, 3), [4, 5, 6], (7, 8, 9)])
e
g = np.array([['a', 'b'],['c', 'd']])
g

#data type of array elements
g.dtype
g.dtype.name
f = np.array([[1, 2, 3],[4, 5, 6]], dtype=complex)
f

np.zeros((3, 3))

np.ones((3, 3))

np.arange(0, 10)   

np.arange(4, 10)

np.arange(0, 12, 3)

np.arange(0, 6, 0.6)

np.arange(0, 12).reshape(3, 4)

np.arange(0, 12).reshape(3, 4)

np.linspace(0,10,5)

np.random.random(3)

np.random.random((3,3))
