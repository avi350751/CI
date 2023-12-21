import matplotlib.pyplot as plt 


fig, ax = plt.subplots()

fruits = ['apple','banana','blueberry','orange']
counts = [25,30,120,16]

bar_labels = ['red','yellow','blue','orange']
bar_colors = ['tab:red','tab:yellow','tab:blue','tab:orange']

ax.bar(fruits, counts, label = bar_labels, color= bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit Color')

plt.savefig('bars.png',bbox_inches='tight')

cat = ['bored','happy','happy','happy','bored','happy']
dog = ['happy','happy','happy','happy','bored','bored']
activity = ['playing','drinking','sleeping','cuddling','washing','combing']

fig, ax = plt.subplots()
ax.plot(activity,dog,label='dog')
ax.plot(activity,cat,label='cat')
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')