import matplotlib.pyplot as plt 


fig, ax = plt.subplots()

clubs = ['ManUtd','Liverpool','Chelsea','ShaktarFC']
counts = [65,30,12,6]

bar_labels = ['red','red','blue','orange']
bar_colors = ['tab:red','tab:red','tab:blue','tab:orange']

ax.bar(clubs, counts, label = bar_labels, color= bar_colors)

ax.set_ylabel('Club Trophies')
ax.set_title('Clubs by trophy count and color')
ax.legend(title='Football Clubs')

plt.savefig('bars.png',bbox_inches='tight')

cat = ['bored','happy','happy','happy','bored','happy']
dog = ['happy','happy','happy','happy','bored','bored']
activity = ['playing','drinking','sleeping','cuddling','washing','combing']

fig, ax = plt.subplots()
ax.plot(activity,dog,label='dog')
ax.plot(activity,cat,label='cat')
ax.legend()

plt.savefig('lines.png', bbox_inches='tight')