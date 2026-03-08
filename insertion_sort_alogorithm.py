# Assignment 1
# Insertion Sort in decreasing order

def sort_descending(values):
    n = len(values)

    for index in range(1, n):
        current_value = values[index]
        position = index - 1

        while position >= 0 and values[position] < current_value:
            values[position + 1] = values[position]
            position -= 1

        values[position + 1] = current_value

    return values


sample_list = [9, 1, 7, 4, 3, 8, 2]

print("Input list:", sample_list)
sort_descending(sample_list)
print("List after insertion sort in decreasing order:", sample_list)