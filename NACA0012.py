#imports
import numpy as np
import matplotlib.pyplot as plt

#constants: chordlength, number of points
c=1 #m
n=100

#generate x locations (cosine clustered)
beta= np.linspace(0, np.pi, n)
x= 0.5 * (1- np.cos(beta))
# print(x)
#compute y from thickness equation
y=0.6 * (0.2969* np.sqrt(x)- 0.1260*x -0.3516*x**2 + 0.2843*x**3  - 0.1036* x**4)
# print(y)

x_rev= x[::-1]
y_rev= y[::-1]
y_mir= -y

y_cat= np.concatenate((y_rev, y_mir))
y_cat=np.delete(y_cat, n)


x_cat= np.concatenate((x_rev,x))
x_cat=np.delete(x_cat, n)
z= np.zeros(2*n-1)

group_no= np.ones(2*n-1)
point_no= np.arange(1, 2*n)

#assemble upper+lower surface into one ordered loop; group, point number, x, y, z
col_stack= np.column_stack((group_no,point_no, x_cat,y_cat,z))
col_stack=np.delete(col_stack, -1, axis=0)

#plot to verify
X= col_stack[:,2]
Y=col_stack[:,3]
plt.plot(X,Y)
plt.axis('equal')
plt.show()


#write coordinate file in ansys format
np.savetxt('airfoil.txt', col_stack, fmt=['%d', '%d', '%.6f', '%.6f', '%.6f'], delimiter=' ', newline='\n', footer='1 0', comments='#')
print(col_stack[0])
print(col_stack[-1])
