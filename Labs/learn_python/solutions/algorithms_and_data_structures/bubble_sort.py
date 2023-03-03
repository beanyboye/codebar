"""
By:         Callum Clegg
Date:       14/01/2023

Desc:       bubble sort
"""

def bubble_sort(arr: list[int]) -> list[int]:
    """ This function uses the bubble sort algorithm to sort number in acending order. """
    
    num_of_elements = len(arr)

    for i in range(num_of_elements - 1):

        for j in range(num_of_elements - 1 - i):
            if (arr[j] > arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

    return arr



if __name__ == "__main__":
    unordered_numbers: list[int] = [4, 2, 10, 7, 8, 11, 51, 3, 22]

    ordered_numbers: list[int] = bubble_sort(unordered_numbers)
    print(*ordered_numbers)

