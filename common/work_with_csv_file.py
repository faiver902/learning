import csv

from work_with_text_file import open_file

file = open_file("users.csv", "a+", newline="")
file_dict = open_file("users_dict.csv", "a+", newline="")

users = [["Tom", 28, 4], ["Alice", 23, 5], ["Bob", 34, 7]]
users_dict = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34},
]
user = ["Sam", 31]


def write_csv(file, content):
    writer = csv.writer(file)
    writer.writerows(content)


def add_csv(file, content):
    writer = csv.writer(file)
    writer.writerow(content)


def read_csv(file):
    file.seek(0)

    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row[0], " - ", row[1])


def write_dict(file, content):
    column = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=column)
    writer.writeheader()
    writer.writerows(content)


def read_dict(file):
    file.seek(0)
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])


# write_csv(file, users)
# add_csv(file, user)
# read_csv(file)
# write_dict(file_dict, users_dict)
# read_dict(file_dict)
