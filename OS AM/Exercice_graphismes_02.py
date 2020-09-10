import matplotlib.pyplot as plt

t = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
T1 = [20,18,16,14,12,10,10,11,12,13,14,16,18,20,22,24,26,28,28,26,24,22,21,20]
T2 = [5,3,3,2,1,0,-4,-2,-2,-1,0,2,4,6,8,7,10,8,7,7,6,6,5,4]

for i in range(len(t)):
    plt.plot([t[i]-0.2, t[i]-0.2], [0, T1[i]], "r-", linewidth = 5)
    plt.plot([t[i]+0.2, t[i]+0.2], [0, T2[i]], "b-", linewidth = 5)


plt.xlabel("temps")
plt.ylabel("température")
plt.xticks(range(23))
plt.yticks(range(-5, 32, 2))
