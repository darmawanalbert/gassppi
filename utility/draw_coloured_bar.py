import matplotlib.pyplot as plt

def draw_coloured_bar(x_enum, data, colour, title, x_label, y_label):
    """
    Given x_enum, data, and some additional information, draw a bar chart using matplotlib

    Parameters:
    x_enum (list): List of x_enum values
    data (list): List of data values
    colour (list): List of colour
    title (str): Bar chart title
    x_label (str): Horizontal label
    y_label (str): Vertical label

    Returns:
    None

    """
    plt.bar(x_enum, data, width=0.9, color=colour)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(axis="y", alpha=0.75)
    plt.rcParams['figure.figsize'] = [12.8, 4.8]
    plt.show()
