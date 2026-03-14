import random
import tracemalloc
from time import perf_counter


def merge_lists(left_part, right_part):
    merged = []
    i = 0
    j = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            merged.append(left_part[i])
            i += 1
        else:
            merged.append(right_part[j])
            j += 1

    while i < len(left_part):
        merged.append(left_part[i])
        i += 1

    while j < len(right_part):
        merged.append(right_part[j])
        j += 1

    return merged


def merge_sort_method(values):
    if len(values) <= 1:
        return values

    middle = len(values) // 2 
    left_side = merge_sort_method(values[:middle])
    right_side = merge_sort_method(values[middle:])

    return merge_lists(left_side, right_side)


def quick_sort_method(values):
    if len(values) <= 1:
        return values

    pivot_value = random.choice(values)

    lower = []
    equal = []
    higher = []

    for number in values:
        if number < pivot_value:
            lower.append(number)
        elif number > pivot_value:
            higher.append(number)
        else:
            equal.append(number)

    return quick_sort_method(lower) + equal + quick_sort_method(higher)


def measure_performance(algorithm_name, algorithm_function, dataset):
    working_data = list(dataset)

    tracemalloc.start()
    start = perf_counter()
    algorithm_function(working_data)
    end = perf_counter()
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "algorithm": algorithm_name,
        "time": round(end - start, 6),
        "memory": peak_memory
    }


def main():
    data_size = 1000

    datasets = {
        "Sorted": list(range(data_size)),
        "Reverse": list(range(data_size, 0, -1)),
        "Random": [random.randint(1, data_size) for _ in range(data_size)]
    }

    final_results = []

    for dataset_name, dataset_values in datasets.items():
        merge_result = measure_performance("Merge Sort", merge_sort_method, dataset_values)
        quick_result = measure_performance("Quick Sort", quick_sort_method, dataset_values)

        final_results.append({
            "dataset": dataset_name,
            "merge_time": merge_result["time"],
            "merge_memory": merge_result["memory"],
            "quick_time": quick_result["time"],
            "quick_memory": quick_result["memory"]
        })

    print("\nSORTING ALGORITHM PERFORMANCE RESULTS\n")

    for result in final_results:
        print(f"Dataset: {result['dataset']}")
        print(f"Merge Sort -> Time: {result['merge_time']} seconds | Memory: {result['merge_memory']} bytes")
        print(f"Quick Sort -> Time: {result['quick_time']} seconds | Memory: {result['quick_memory']} bytes")
        print("-" * 60)

    print("\nSUMMARY TABLE")
    print("-" * 80)
    print(f"{'Dataset':<12}{'Merge Time':<15}{'Quick Time':<15}{'Merge Memory':<18}{'Quick Memory':<18}")

    for result in final_results:
        print(
            f"{result['dataset']:<12}"
            f"{result['merge_time']:<15}"
            f"{result['quick_time']:<15}"
            f"{result['merge_memory']:<18}"
            f"{result['quick_memory']:<18}"
        )


if __name__ == "__main__":
    main()