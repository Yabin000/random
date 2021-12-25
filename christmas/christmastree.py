## =================================== Merry Chirstmas ========================================== ##
## This script is entirely for fun to celebrate 2021 Christmas
## Most code comes from the following blog
## https://medium.com/analytics-vidhya/how-to-draw-a-3d-christmas-tree-with-matplotlib-aabb9bc27864
## =================================== Merry Chirstmas ========================================== ##



import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

K = 800
FACECOLOR='black'


fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(top = 1, bottom = 0, 
                    right = 1, left = 0, 
                    hspace = 0, wspace = 0)
plt.margins(0,0,0)

def init_tree():
    """plot the initial tree"""
    ## tree
    Z = [i for i in range(K)]
    X = [np.cos(i/10)*(K-i) for i in range(K)]
    Y = [np.sin(i/10)*(K-i) for i in range(K)]
    ax.scatter(X,Y,Z, c="green", marker="D", s=18)

    ## head star
    ax.scatter(0, 0, 850, marker="1", color="white",s=400)
    ax.scatter(0, 0, 850, marker="2", color="white",s=400)
    ax.scatter(0, 0, 850, marker="3", color="white",s=400)
    ax.scatter(0, 0, 850, marker="4", color="white",s=400)
    ax.scatter(0, 0, 850, marker="o", color="gold",s=20)

    ## decleration
    step = 4
    Z = [i for i in range(1,K,step)]
    X = [np.cos(i/5+2)*(K-i+10) for i in range(1,K,step)]
    Y = [np.sin(i/5+2)*(K-i+10) for i in range(1,K,step)]
    ax.scatter(X,Y,Z, c="red", marker="*", s=25)

    Z = [i for i in range(1,K,step)]
    X = [np.sin(i/5+2)*(K-i+10) for i in range(1,K,step)]
    Y = [np.cos(i/5+2)*(K-i+10) for i in range(1,K,step)]
    ax.scatter(X,Y,Z, c="orange", marker="p", s=18)

    Z = [i for i in range(800, int(K/4), -(step+1))]
    X = [np.sin(i/5+2)*(K/4-i+10) for i in range(int(K/4), 800, (step+1))]
    Y = [np.cos(i/5+2)*(K/4-i+10) for i in range(int(K/4), 800, (step+1))]
    ax.scatter(X, Y, Z, c='white', marker="o", s=18)

    Z = [i for i in range(800, int(K/3), -(step+1))]
    X = [np.cos(i/5+2)*(K/3-i+10) for i in range(int(K/3), 800, (step+1))]
    Y = [np.sin(i/5+2)*(K/3-i+10) for i in range(int(K/3), 800, (step+1))]
    ax.scatter(X, Y, Z, c='purple', marker="X", s=25)

    ## remove tick
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    ## remove grid and set face color
    ax.grid(False)
    ax.set_facecolor(FACECOLOR)

    ## remove pane fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    ## change edge color to whatever the same as 
    ## the facecolor
    ax.xaxis.pane.set_edgecolor(FACECOLOR)
    ax.yaxis.pane.set_edgecolor(FACECOLOR)
    ax.zaxis.pane.set_edgecolor(FACECOLOR)

    return fig,



def animate(frame_number):
    """
    the same tree but to show in different frames
    """
    fig.clear()
    ax = fig.add_subplot(111, projection="3d")

    ## tree
    Z = [i for i in range(K)]
    X = [np.cos(i/10-frame_number/10)*(K-i) for i in range(K)]
    Y = [np.sin(i/10-frame_number/10)*(K-i) for i in range(K)]
    ax.scatter(X,Y,Z, c="green", marker="D", s=18)

    ## head star
    ax.scatter(0, 0, 850, marker="1", color="white",s=400)
    ax.scatter(0, 0, 850, marker="2", color="white",s=400)
    ax.scatter(0, 0, 850, marker="3", color="white",s=400)
    ax.scatter(0, 0, 850, marker="4", color="white",s=400)
    ax.scatter(0, 0, 850, marker="o", color="gold",s=20)

    ## decleration
    step = 4
    Z = [i for i in range(1,K,step)]
    X = [np.cos(i/5+2-frame_number/10)*(K-i+10) for i in range(1,K,step)]
    Y = [np.sin(i/5+2-frame_number/10)*(K-i+10) for i in range(1,K,step)]
    ax.scatter(X,Y,Z, c="red", marker="*", s=25)

    Z = [i for i in range(1,K,step)]
    X = [np.sin(i/5+2-frame_number/10)*(K-i+10) for i in range(1,K,step)]
    Y = [np.cos(i/5+2-frame_number/10)*(K-i+10) for i in range(1,K,step)]
    ax.scatter(X,Y,Z, c="orange", marker="p", s=18)

    Z = [i for i in range(800, int(K/4), -(step+1))]
    X = [np.sin(i/5+2-frame_number/10)*(K/4-i+10) for i in range(int(K/4), 800, (step+1))]
    Y = [np.cos(i/5+2-frame_number/10)*(K/4-i+10) for i in range(int(K/4), 800, (step+1))]
    ax.scatter(X, Y, Z, c='white', marker="o", s=18)

    Z = [i for i in range(800, int(K/3), -(step+1))]
    X = [np.cos(i/5+2-frame_number/10)*(K/3-i+10) for i in range(int(K/3), 800, (step+1))]
    Y = [np.sin(i/5+2-frame_number/10)*(K/3-i+10) for i in range(int(K/3), 800, (step+1))]
    ax.scatter(X, Y, Z, c='purple', marker="X", s=25)

    ## remove tick
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    ## remove grid and set face color
    ax.grid(False)
    ax.set_facecolor(FACECOLOR)

    ## remove pane fill
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    ## change edge color to whatever the same as 
    ## the facecolor
    ax.xaxis.pane.set_edgecolor(FACECOLOR)
    ax.yaxis.pane.set_edgecolor(FACECOLOR)
    ax.zaxis.pane.set_edgecolor(FACECOLOR)

    return fig,


if __name__ == "__main__":
    # fig = init_tree()
    # plt.show()

    anim = animation.FuncAnimation(fig, animate, init_func=init_tree,
                                   frames=100, interval=150, blit=True) 
    anim.save("christmastree.mp4")
