import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x_data = np.random.randint(80, size=(400, 4))
y_data = np.random.randint(80, size=(400, 4))

lists = [[],[]]
lists[0] = x_data
lists[1] = y_data 

fig, ax = plt.subplots(figsize = (8,6))
ax.set_xlim(0,80)
ax.set_ylim(0,80)

scatter = ax.scatter(lists[0][0], lists[1][0], zorder = 5) #Scatter plot

annotation = ax.annotate('  Subject 1', xy=(lists[0][0][2],lists[1][0][2]))

arrow = ax.annotate('', xy = (lists[0][0][0], lists[1][0][0]), xytext = (lists[0][0][1],lists[1][0][1]), arrowprops = {'arrowstyle': "<->"})

def animate(i) : 
    scatter.set_offsets([[[[[lists[0][0+i][0], lists[1][0+i][0]], [lists[0][0+i][1], lists[1][0+i][1]], [lists[0][0+i][2], lists[1][0+i][2]], [lists[0][0+i][3], lists[1][0+i][3]]]]]])
    Subject_x = lists[0][0+i][2]
    Subject_y = lists[1][0+i][2]
    annotation.set_position((Subject_x, Subject_y))
    annotation.xy = (Subject_x, Subject_y)
    Arrow1 = (lists[0][0+i][0], lists[1][0+i][0]) #Code for arrow animation doesn't work. Produces a blank screen after the 1st frame
    Arrow2 = (lists[0][0+i][1], lists[1][0+i][1])
    arrow.set_position((Arrow1, Arrow2))
    arrow.xy = (Arrow1, Arrow2)

ani = animation.FuncAnimation(fig, animate,
                          interval = 50, blit = False)

plt.show()