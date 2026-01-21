import pandas as pd
import matplotlib.pyplot as plt


x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y)
# print(plt.show())

#if labeling
plt.xlabel('x axis')
plt.ylabel('y axis')
#title to that graph
plt.title("student Marks")
print(plt.show())



#for ml we mstly use scattre plot
import matplotlib.pyplot as plt

A = [1, 2, 3, 4, 5]
B= [5, 7, 4, 6, 8]

plt.scatter(A, B)
plt.xlabel("A")
plt.ylabel("B")
plt.title("Scatter Plot Example")
print(plt.show())

#using matplot with pandas

data={
    'day':['mon','tues','wed','thurs','fri','sat','sun'],
    'sales':[200,300,400,350,600,350,640] #here no. of values should be same in both x and y 
    }#its a dictionary as its in key : value pair
#if x={ 10,20} then its a set

df=pd.DataFrame(data)
plt.plot(df['day'],df['sales'])
plt.title(' daily sales')
plt.xlabel('Days')
plt.ylabel('Sales')
print(plt.show())