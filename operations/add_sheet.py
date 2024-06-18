import os
import csv

def read_csv_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        header = next(csv_reader)[2:]
        content = list(csv_reader)
    return header, content

def read_data_from_csv(header, csv_reader, members):
    new_mem = []
    for name in header:
        if name not in members and name not in new_mem:
            new_mem.append(name)
    
    data = []
    for row in csv_reader:
        data_row = []
        data_row.append(int(row[0]))
        if row[1] in header:
            data_row.append(row[1])
        else:
            return None, None, None
        data_row.append([int(row[i]) if row[i] else 0 for i in range(2, len(row))])
        data.append(data_row)

    return header, data, new_mem


def add_data(members, records, history, MAXMEMBER):
    any_thing_find = False
    for filename in os.listdir(os.getcwd()):
        if not filename.endswith('.csv') or filename in history:
            continue
        any_thing_find = True
        header, csv_reader = read_csv_file(filename)
        header, data, new_mem = read_data_from_csv(header, csv_reader, members)
        if header and input(f"do you want add {filename} to db (new rec:{len(data)} mem:{len(new_mem)})? (yes/no) ").lower() in ['yes', 'y']:
            history.append(filename)
            members += new_mem

            index_array = [0] * len(header)
            for i in range(len(header)):
                index_array[i] = members.index(header[i])
            
            for record in data:
                row = [*record[:2]]
                status = [0] * MAXMEMBER
                
                for i in range(len(header)):
                    status[index_array[i]] = record[2][i]
                row.append(status)
                records.append(row)
            print('\nadded sucessfully!\n')
        else:
            print('\ncanceled!\n')
    
    if not any_thing_find:
        print('\nnew file not exist!\n')
    return members, records, history