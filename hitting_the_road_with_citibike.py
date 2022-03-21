import csv

source_file = open('chapter_2_data_files\\202009-citibike-tripdata.csv', 'r')

citibike_reader = csv.DictReader(source_file)

print(citibike_reader.fieldnames)

subscriber_count = 0
customer_count = 0
other_user_count = 0

for a_row in citibike_reader:
    if a_row['usertype'] == 'Subscriber':
        subscriber_count = subscriber_count + 1
    elif a_row['usertype'] == 'Customer':
        customer_count = customer_count + 1
    else:
        other_user_count = other_user_count + 1


    
