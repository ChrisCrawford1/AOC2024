def _read_values_from_file() -> list[str]:
    try:
        file = open("./day_one/values.txt", "r")
        return file.readlines()
    except:
        print("Error parsing text file, try again")
        quit()


def get_sorted_values() -> tuple[list[int], list[int]]:
    raw_values = _read_values_from_file()
    unsorted_left_values, unsorted_right_values = [], []

    for val in raw_values:
        left, right = val.split()
        unsorted_left_values.append(left)
        unsorted_right_values.append(right)

    unsorted_left_values.sort()
    unsorted_right_values.sort()

    return unsorted_left_values, unsorted_right_values


def calculate_distance() -> int:
    left_values, right_values = get_sorted_values()

    left_length, right_length = len(left_values), len(right_values)

    if left_length == 0 or right_length == 0:
        print("Empty list found, cannot complete calculation")
        return 0

    if left_length != right_length:
        print("Left and right lists length do not match, cannot complete calculation")
        return 0

    total_distance = 0

    # As we have already checked that the left and right are the same length,
    # we can use either or for the range value, in this case we decided on left.
    for i in range(0, left_length):
        left, right = left_values[i], right_values[i]

        distance = abs(int(left) - int(right))
        total_distance += distance

    return total_distance

calculated_distance = calculate_distance()
print("The total distance is {}".format(calculated_distance))
