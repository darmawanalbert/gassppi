import matplotlib.pyplot as plt

def draw_scatter(x_axis, y_axis, title, x_label, y_label):
    """
    Given x_axis, y_axis data and some additional information, draw and plot a scatter plot using matplotlib

    Parameters:
    x_axis (list): List of x_axis values
    y_axis (list): List of y_axis values
    title (str): Scatter plot title
    x_label (str): Horizontal label
    y_label (str): Vertical label

    Returns:
    None

    """
    plt.scatter(x_axis, y_axis)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(axis="y", alpha=0.75)
    plt.show()
