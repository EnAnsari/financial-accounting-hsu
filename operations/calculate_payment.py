import os

def calculate(payment, members):
    prices = [[i, 0] for i in range(len(members))]
    for i in range(len(members)): 
        for j in range(len(members)):
            prices[i][1] -= payment[i][j]
            prices[i][1] += payment[j][i]    
    
    prices = sorted(prices, key=lambda x: x[1])
    message = ''
    i = 0
    j = len(members) - 1
    while i < j:
        if prices[j][1] >= (prices[i][1] * -1):
            message += f"{members[prices[i][0]]} have to pay {prices[i][1] * -1} to {members[prices[j][0]]}\n"
            if prices[j][1] == (prices[i][1] * -1):
                j -= 1
            else:
                prices[j][1] += prices[i][1]
            i += 1
        else:
            prices[i][1] += prices[j][1]
            message += f"{members[prices[i][0]]} have to pay {prices[j][1]} to {members[prices[j][0]]}\n"
            j -= 1
    
    with open(os.path.join(os.getcwd(), 'result', 'payment.txt'), 'w') as file:
        file.write(message)
    print('\npayment receipt created successfully!\n')