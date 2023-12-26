import matplotlib.pyplot as plt

def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    points = [(round(x), round(y))]

    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))

    return points

def plot_line(x1, y1, x2, y2):
    points = draw_line(x1, y1, x2, y2)
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    plt.plot(x_values, y_values, marker='o', color='black')

def plot_circle(radius):
    x = 0
    y = radius
    d = 1 - radius

    points = set()

    while x <= y:
        points.add((x, y))
        points.add((-x, y))
        points.add((x, -y))
        points.add((-x, -y))
        points.add((y, x))
        points.add((-y, x))
        points.add((y, -x))
        points.add((-y, -x))

        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1

    for point in points:
        plt.scatter(point[0] + 15, point[1], color='black')

def main():
    print("Choose option:")
    print("1. Draw a line")
    print("2. Draw a circle")

    choice = int(input("Enter choice (1 or 2): "))

    if choice == 1:
        x1, y1 = map(int, input("Enter starting point (x1 y1): ").split())
        x2, y2 = map(int, input("Enter ending point (x2 y2): ").split())
        plt.figure()
        plot_line(x1, y1, x2, y2)
        plt.title("DDA Line Generation")
        plt.show()
    elif choice == 2:
        radius = int(input("Enter radius for the circle: "))
        plt.figure()
        plot_circle(radius)
        plt.title("Midpoint Circle Algorithm")
        plt.show()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
