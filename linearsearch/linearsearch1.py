import time
import matplotlib.pyplot as plt
import random

def ls(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1



def gen():
    arr = []
    for i in range(1000):
        arr.append(random.randint(0,10000))
    return arr

axis = []
timetakes= []
z = int(input("how many array: "))
for i in range(z):
    arr = gen()
    print(arr)
    x = int(input("Enter the num to find: "))
    start = time.time()
    index = ls(arr,x)
    end = time.time()
    print("this is the index: ", index)
    timetakes.append(end - start)
    axis.append(i)

print(timetakes)
print(axis)