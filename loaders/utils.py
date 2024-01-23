import csv


def read_csv(csv_file):
    file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(file)
    for row in reader:
        yield row
