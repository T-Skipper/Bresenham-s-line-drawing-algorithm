def bresen(x, y, j, k): 
    """
    X and Y are the Origin's Pixel Co-ordinates
    J and k are the Destination's Pixel Co-ordinates
    """
    count = 0
    axes = [[x, y]]

    #   Obtain change in x and change in y respectively
    dx = j - x
    dy = k - y

    #   Derive the Decision Parameter
    p = 2*dy - dx

    # Print the origin
    print(f'Pixel {count} ({x}, {y}) P{count} is {p}')

    #   Store the co-ordinates in a list - Axes
    while x != j and y != k:
        if p < 0:
            count += 1
            x += 1
            p = p + 2*dy
            axes.append([x, y])
            # print(f'Pixel {count} ({x}, {y}) P{count} is {p}')

        else:
            count += 1
            x += 1
            y += 1
            p = p + 2*(dy - dx)
            axes.append([x, y])
            # print(f'Pixel {count} ({x}, {y}) P{count} is {p}')

    print(f'Co-ordinates:{axes[:4]}...')

    # Flatten the co-ordinates
    x, y = [], []

    for pixel in axes:
        x.append(pixel[0])
        y.append(pixel[1])

    # Plot the Graph
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))
    plt.plot(
        x, y,
        color='blue',
        marker='o',
        markerfacecolor='white',
        markersize=8
    )
    plt.title(f'Bresenham\'s Algorithm --> {axes[0]} - {axes[-1]}')
    plt.xlabel("X Co-ordinates")
    plt.ylabel("Y Co-ordinates")
    plt.show()
    plt.savefig(f'Images/Image_{axes[0][0]}_{axes[0][1]}_{axes[-1][0]}_{axes[-1][1]}')


bresen(12, 24, 18, 30)
bresen(4, 22, 43, 61)
bresen(5, 45, 45, 5)