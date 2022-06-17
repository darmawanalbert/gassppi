import matplotlib.pyplot as plt

def draw_multiple_histogram(data_4a, data_5a, data_6a, title, x_label, y_label):
    """
    Given x_axis data of 4A templates, 5A templates, 6A templates, and some additional information, draw and show a histogram using matplotlib

    Parameters:
    data_4a (list): List of first x_axis values
    data_5a (list): List of second x_axis values
    data_6a (list): List of third x_axis values
    title (str): Histogram title
    x_label (str): Horizontal label
    y_label (str): Vertical label

    Returns:
    None

    """
    plt.hist(data_4a, alpha=0.5, bins="auto", label="4Ä distance threshold")
    plt.hist(data_5a, alpha=0.5, bins="auto", label="5Ä distance threshold")
    plt.hist(data_6a, alpha=0.5, bins="auto", label="6Ä distance threshold")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(axis="y", alpha=0.75)
    plt.legend(loc='upper right')
    plt.show()
