def remove_duplicates(input_list):
    seen = set()
    result = []

    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result
my_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(my_list)
print(f"The list with duplicates removed: {result_list}")
