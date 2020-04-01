import numpy as np


def binary_split_array(array: np.ndarray, labels: list = None) -> np.ndarray:
    """Similar to separate segmentation. Splits array by unique values decoded in binary.
    """
    if labels.size != 0:
        unique_values = labels
    else:
        unique_values = np.unique(array)
    result = np.zeros((len(unique_values), ) + array.shape)
    for i, value in enumerate(unique_values):
        temp = np.array(array)
        temp[temp != value] = 0
        temp[temp == value] = 1
        result[i] = temp
    return result


def calculate_separate_dice(x: np.ndarray, y: np.ndarray, labels: np.ndarray = None) -> np.ndarray:
    """Calculate the Sørensen–Dice coefficient for two numpy arrays x and y
     where each label is calculated separately. The inputs should match in size/ dimensions."""
    x = binary_split_array(x + 1, labels + 1)
    y = binary_split_array(y + 1, labels + 1)
    axis = tuple(np.arange(1, x.ndim))
    return 2 * np.sum(x * y, axis=axis) / (np.sum(x, axis=axis) + np.sum(y, axis=axis))


def calculate_overall_dice(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Calculate the Sørensen–Dice coefficient for two numpy arrays x and y.
    The inputs should match in size/ dimensions."""
    return 2.0 * np.sum(y[y == x]) / (np.sum(x) + np.sum(y))
