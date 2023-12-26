import matplotlib.pyplot as plt  # Importing matplotlib library for plotting

# Function to draw a line using DDA algorithm
def draw_line(x1, y1, x2, y2):
    dx = x2 - x1  # Calculate change in x
    dy = y2 - y1  # Calculate change in y

    # Determine the number of steps based on the larger difference
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    # Calculate the increment for x and y coordinates
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1  # Initialize x coordinate
    y = y1  # Initialize y coordinate

    points = [(round(x), round(y))]  # Store the starting point

    # Generate intermediate points along the line using incremental steps
    for _ in range(steps):
        x += x_increment
        y += y_increment
        points.append((round(x), round(y)))  # Store each rounded point

    return points  # Return the list of points on the line

# Function to plot a line using the draw_line function
def plot_line(x1, y1, x2, y2):
    points = draw_line(x1, y1, x2, y2)  # Get points on the line
    x_values = [point[0] for point in points]  # Extract x coordinates
    y_values = [point[1] for point in points]  # Extract y coordinates

    # Plot the line using matplotlib
    plt.plot(x_values, y_values, marker='o', color='black')

# Function to plot a circle using the midpoint circle algorithm
def plot_circle(radius):
    x = 0  # Initialize x coordinate of the circle's center
    y = radius  # Initialize y coordinate of the circle's center
    d = 1 - radius  # Initial decision parameter

    points = set()  # Initialize a set to store circle points

    # Generate points for the circle using the midpoint circle algorithm
    while x <= y:
        # Add symmetric points based on circle symmetry
        points.add((x, y))
        points.add((-x, y))
        points.add((x, -y))
        points.add((-x, -y))
        points.add((y, x))
        points.add((-y, x))
        points.add((y, -x))
        points.add((-y, -x))

        x += 1  # Increment x

        # Update decision parameter based on the circle algorithm
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1  # Decrement y for a new row
            d += 2 * (x - y) + 1

    # Plot the circle points on a graph using matplotlib
    for point in points:
        plt.scatter(point[0] + 15, point[1], color='black')

# Main function to provide a menu for drawing a line or a circle
def main():
    print("Choose option:")
    print("1. Draw a line")
    print("2. Draw a circle")

    choice = int(input("Enter choice (1 or 2): "))  # User input for choice

    if choice == 1:  # If choice is to draw a line
        x1, y1 = map(int, input("Enter starting point (x1 y1): ").split())
        x2, y2 = map(int, input("Enter ending point (x2 y2): ").split())
        plt.figure()  # Create a new figure for plotting
        plot_line(x1, y1, x2, y2)  # Plot the line
        plt.title("DDA Line Generation")  # Set plot title
        plt.show()  # Display the plot
    elif choice == 2:  # If choice is to draw a circle
        radius = int(input("Enter radius for the circle: "))  # Input radius
        plt.figure()  # Create a new figure for plotting
        plot_circle(radius)  # Plot the circle
        plt.title("Midpoint Circle Algorithm")  # Set plot title
        plt.show()  # Display the plot
    else:  # For an invalid choice
        print("Invalid choice!")  # Display error message

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
