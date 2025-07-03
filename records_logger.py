"""Function for logging sorting resutls"""

import json


def records_log(sort_type, list_num, list_min, list_max, sorting_elapsed_time, sort_status):
    """JSON logging Function"""
    sort_type_name = "No Entry"
    sort_status_name = "No Entry"

    if sort_type == "A":
        sort_type_name = "Bubble Sort"
    elif sort_type == "B":
        sort_type_name = "Quick Sort"
    elif sort_type == "C":
        sort_type_name = "Monkey Sort"

    if sort_status == "A":
        sort_status_name = "Sorted"
    elif sort_type == "B":
        sort_status_name = "Reverse Sorted"
    elif sort_type == "C":
        sort_status_name = "Random"

    record_data = {
        "Type of Sort": sort_type_name,
        "Number of Items: ": list_num,
        "Min sorting item: ": list_min,
        "Max sorting item: ": list_max,
        "Sorting Time: ": sorting_elapsed_time,
        "Original status: ": sort_status_name}

    with open("Records.json", 'r', encoding="utf-8") as json_records:
        feeds = json.load(json_records)

    feeds.append(record_data)

    with open("Records.json", 'w', encoding="utf-8") as json_records:
        json.dump(feeds, json_records, indent=4)
