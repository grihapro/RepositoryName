import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file_read:
        data = csv.DictReader(file_read)
        py_obj = [row for row in data]
        with open(OUTPUT_FILENAME, 'w') as file_write:
            json.dump(py_obj, file_write, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
