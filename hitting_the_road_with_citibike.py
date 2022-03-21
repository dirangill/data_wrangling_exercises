import csv

source_file = open('chapter_2_data_files\\202009CitibikeTripdataExample.csv', 'r')

citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)
