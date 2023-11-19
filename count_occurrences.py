def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# Example usage:
my_string = input("Input a string: ")
character_to_count = "l"
result = count_occurrences(my_string, character_to_count)
print(f"The character '{character_to_count}' appears {result} times in the string.")
