import csv
import os

def make_csv_content(payment, members):
    csv_content = [['pay to']]
    for name in members:
        csv_content[0].append(name)
    for i in range(len(members)):
        row = [members[i]]
        for j in range(len(members)):
            row.append(payment[i][j])
        csv_content.append(row)
    return csv_content

def export_csv(payment, members):
    if not os.path.isdir('./result'):
        os.mkdir('result')
    with open(os.path.join(os.getcwd(), 'result', 'output.csv'), 'w') as output:
        csv_writer = csv.writer(output, delimiter=',', lineterminator='\n')
        csv_writer.writerows(make_csv_content(payment, members))

def sync(payment):
    for i in range(len(payment) - 1):
        for j in range(i + 1, len(payment)):
            if payment[i][j] >= payment[j][i]:
                payment[i][j] = payment[i][j] - payment[j][i]
                payment[j][i] = 0
            else:
                payment[j][i] = payment[j][i] - payment[i][j]
                payment[i][j] = 0
    return payment
        

def calculate(members, records):
    payment = []
    for i in range(len(members)):
        payment.append([0] * len(members))
    
    
    for i in range(len(records)):
        price = records[i][0] // sum(records[i][2])
        buyer_idx = members.index(records[i][1])
        for j in range(len(members)):
            if records[i][2][j] == 1 and j != buyer_idx:
                payment[j][buyer_idx] += price
    
    # print(payment)

    payment = sync(payment)
    export_csv(payment, members)
    print("\nresult created successfully!\n")
    return payment