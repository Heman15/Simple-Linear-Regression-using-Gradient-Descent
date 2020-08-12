import numpy as n
import matplotlib.pyplot as plt
x=n.array([10,1,2,3,4,5])
y=n.array([10,5,7,9,11,13])
slop=intercept=0
learning_rate=0.001
for i in range(1000):
    y_p=slop*x+intercept
    parital_der_wrt_slop=(-2/len(x))*sum((y-y_p)*x)
    parital_der_wrt_intercept=(-2/len(x))*sum((y-y_p))
    slop=slop-learning_rate*parital_der_wrt_slop
    intercept=intercept-learning_rate*parital_der_wrt_intercept
    print("slop= ",slop)
    print("  intercept= ",intercept)

y_points=[]
for i in range(20):
    c=slop*i + intercept
    y_points.append(c)

plt.text(9,10.5,"OUTLIER",fontsize=10)
plt.scatter(x,y, edgecolors= 'red')
plt.scatter\
    ([x for x in range(20)],y_points)
#plt.scatter(x,y, color = 'red')
plt.show()
