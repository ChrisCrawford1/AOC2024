def get_reports_from_file() -> list[list[str]]:
    try:
        file = open("./day_two/reports.txt", "r")
        raw_values = file.readlines()

        sanitized_reports = []

        for value in raw_values:
            report_list = value.split()
            sanitized_reports.append(report_list)

        return sanitized_reports
    except:
        print("Error parsing text file, try again")
        quit()


def values_change_in_same_direction(values: list[str]) -> bool:
    all_values_increasing = all(int(values[i]) < int(values[i + 1]) for i in range(len(values) - 1))
    if all_values_increasing:
        return True

    all_values_decreasing = all(int(values[i]) > int(values[i + 1]) for i in range(len(values) - 1))
    if all_values_decreasing:
        return True

    return False


def process_reports() -> None:
    reports = get_reports_from_file()
    safe_reports, unsafe_reports = 0, 0

    for report in reports:
        if not values_change_in_same_direction(report):
            unsafe_reports += 1
            continue

        prev_level = int(report[0])
        safe = True

        for i in range(1, len(report)):
            current_level = int(report[i])
            distance = abs(prev_level - current_level)

            if distance == 0 or distance > 3:
                unsafe_reports += 1
                safe = False
                break

            prev_level = current_level

        if safe:
            safe_reports += 1

    print("Safe Reports = {} | Unsafe Reports = {}".format(safe_reports, unsafe_reports))


process_reports()
