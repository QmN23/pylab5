import json
import csv
import sys

# Task 1

# with open('src/input.txt', 'r') as f:
#     numbers_str = f.readline().split()
#     numbers = []
#
#     for num_str in numbers_str:
#         numbers.append(int(num_str))
#
# product = 1
# for num in numbers:
#     product *= num
#
# with open('src/output.txt', 'w') as f:
#     f.write(str(product))


# Task 2
# with open('src/Task2.txt', 'r') as f:
#     numbers = [int(line.strip()) for line in f]
#
#     numbers = sorted(numbers)
#
# with open('src/Task2_output.txt', 'w') as f:
#     for num in numbers:
#         f.write(str(num) + '\n')

# Task 3
# with open('src/Task3_input.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#
# max_age = 0
# min_age = 99999
# oldest_child = ''
# youngest_child = ''
#
#
# for line in lines:
#     parts = line.split()
#     age = int(parts[-1])
#     if age > max_age:
#         max_age = age
#         oldest_child = line
#     if age < min_age:
#         min_age = age
#         youngest_child = line
#
#
# with open('src/Task3_oldest.txt', 'w') as file:
#     file.write(oldest_child)
#
# with open('src/Task3_youngest.txt', 'w') as file:
#     file.write(youngest_child)


# Task 4
def json_to_csv(json_file_path):
    with open(json_file_path) as json_file:
        data = json.load(json_file)

    root_name = json_file_path.split('.')[0]

    csv_file_path = f"{root_name}.csv"

    employees_data = data.get('Employees')

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(employees_data[0].keys())
        for emp in employees_data:
            csv_writer.writerow(emp.values())

json_file_path = sys.argv[1]
json_to_csv(json_file_path)


