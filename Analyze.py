

import numpy as np
import matplotlib.pyplot as plt
reaches = np.genfromtxt("reaches2",delimiter=',')
reachstart = np.genfromtxt("reachstart2",delimiter=',')
ampvel = np.genfromtxt("ampVel2",delimiter=',')
tss = np.genfromtxt("tss2",delimiter=',')
rewtime = np.genfromtxt("rewTime2",delimiter=',')
temp = np.zeros((int(max(reachstart))+1500))
pos = np.genfromtxt("jspos2",delimiter=',')
depth = np.genfromtxt("depth2",delimiter=',')
border = np.genfromtxt("Mborder2",delimiter=',')
time_shallow_moving=[]
fire_moving=[]
counter = np.zeros(int(tss.shape[0]))
for i in range(0,20):
    print(i)
    for j in range(int(tss.shape[0])-67,int(tss.shape[0])):     
        for k in range(int(counter[j]),int(len(tss[i]))):
            if(tss[j][k]>reachstart[i]+1000):
                break
            if(tss[j][k]<reachstart[i]+1000 and tss[j][k]>reachstart[i]-500):
                time_shallow_moving.append(tss[j][k])
                fire_moving.append(j)
                counter[j]=counter[j]+1
time_shallow_thinking=[]
fire_thinking=[]
counter = np.zeros(int(tss.shape[0]))
for i in range(0,19):
    print(i)
    for j in range(int(tss.shape[0])-67,int(tss.shape[0])):     
        for k in range(int(counter[j]),int(len(tss[i]))):
            if(tss[j][k]>reachstart[i+1]-500):
                break
            if(tss[j][k]>reachstart[i]+1000 and tss[j][k]<reachstart[i+1]-500):
                time_shallow_thinking.append(tss[j][k])
                fire_thinking.append(j)
                counter[j]=counter[j]+1
plt.figure(num=None, figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(time_shallow_moving,fire_moving,'*')
plt.plot(time_shallow_thinking,fire_thinking,'r.')
plt.xlabel("Time (milliseconds)",fontsize=16)
plt.ylabel("Neuron",fontsize=16)
plt.title("")
plt.show()

time_deep_moving=[]
fire_deep_moving=[]
counter = np.zeros(int(tss.shape[0]))
for i in range(0,20):
    print(i)
    for j in range(int(tss.shape[0])-67):     
        for k in range(int(counter[j]),int(len(tss[i]))):
            if(tss[j][k]>reachstart[i]+1000):
                break
            if(tss[j][k]<reachstart[i]+1000 and tss[j][k]>reachstart[i]-500):
                time_deep_moving.append(tss[j][k])
                fire_deep_moving.append(j)
                counter[j]=counter[j]+1
                
time_deep_thinking=[]
fire_deep_thinking=[]
counter = np.zeros(int(tss.shape[0]))
for i in range(0,19):
    print(i)
    for j in range(int(tss.shape[0])-67):     
        for k in range(int(counter[j]),int(len(tss[i]))):

            if(tss[j][k]>reachstart[i+1]-500):
                break
            if(tss[j][k]>reachstart[i]+1000 and tss[j][k]<reachstart[i+1]-500):
                time_deep_thinking.append(tss[j][k])
                fire_deep_thinking.append(j)
                counter[j]=counter[j]+1
plt.figure(num=None, figsize=(14, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(time_deep_moving,fire_deep_moving,'*')
plt.plot(time_deep_thinking,fire_deep_thinking,'r.')
plt.xlabel("Time (milliseconds)",fontsize=16)
plt.ylabel("Neuron",fontsize=16)
plt.title("")
plt.show()


