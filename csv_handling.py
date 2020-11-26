import csv

with open('students_data.csv', mode='w') as csv_file:
    fieldnames = ['id', 'student_name', 'birth_month', 'career']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'id': 1, 'student_name': 'Pablito Mix', 'birth_month': 'November', 'career': 'DJ'})
    writer.writerow({'id': 2, 'student_name': 'JBlavin', 'birth_month': 'January', 'career': 'musician'})

with open('students_data.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        print(f'\t{row["student_name"]} with id {row["id"]} is a {row["career"]}')
        line_count += 1
    print(f'Processed {line_count} lines.') 
