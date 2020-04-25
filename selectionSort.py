# Selection Sort from: https://stackabuse.com/selection-sort-in-python/
# Selection sort algorithm time complexity is: O(n^2). But faster(twice as fast) than Bubble Sort

def selection_sort(list):

    for i in range(len(list)-1):    # Start the list itireration.

        min_index = i   # We assume the min value is the first element of the list

        for current_element in range(i+1, len(list)-1):   # We then use current_element to loop through the remaining elements

            if list[current_element] < list[min_index]:   # Update the min_index if the current_element is lower
                min_index = current_element

        list[i], list[min_index] = list[min_index], list[i]     # After finding the lowest item of the unsorted regions, swap with the first unsorted item

    return list


#
list = [3, 1, 41, 59, 26, 53, 59]

string = "Before Sorting: {} \nAfter Sorting: {}"
print(string.format(str(list), selection_sort(list)))
