import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.Blues, s=1)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
