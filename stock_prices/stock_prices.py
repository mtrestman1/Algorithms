#!/usr/bin/python

import argparse

'''
iterate through prices and compare i[0] to price of +1 and check which is bigger
if i is less than +1 calculate difference (profit) and append to new array
then iterate through new array comparing to find largest number
I HAVE NO IDEA WHAT IM DOING
'''


def find_max_profit(prices):
    new_arr = []
    largest = prices[1] - prices[0]
    for i in range(0, len(prices)):
        for j in range(0, len(prices)):
            if i < j:
                profit = prices[j] - prices[i]
                new_arr.append(profit)
    for i in range(0, len(new_arr)):
        
        if largest < new_arr[i]:
            largest = new_arr[i]
    return largest
           
            
            
prices = [100, 90, 80, 50, 20, 10]   
        
print(find_max_profit(prices))
   


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

# print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))