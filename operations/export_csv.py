import csv
import os

def export(members, records):
    csv_content = [['price', 'buyer', *members]]
    for record in records:
        row = [*record[:2]]
        row += record[2][:len(members)]
        csv_content.append(row)
    
    if not os.path.isdir('./result'):
        os.mkdir('result')
    try:
        with open(os.path.join(os.getcwd(), 'result', 'records.csv'), 'w') as output:
            csv_writer = csv.writer(output, delimiter=',', lineterminator='\n')
            csv_writer.writerows(csv_content)
        print(f'\n{len(records)} record exported successfully!\n')
    except PermissionError:
        print(f'\nError: please close your csv file!\n')