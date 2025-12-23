# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

ordered_dict = OrderedDict()
n = int(input())
for i in range(n):
    x = input()
    food_list = x.split()
    price = int(food_list[-1])
    n = len(food_list)
    food_name = " ".join(food_list[:n-1])
    if(food_name in ordered_dict.keys()):
        ordered_dict[food_name]+=price
    else:
        ordered_dict[food_name]=price

for i in ordered_dict:
    print(i, ordered_dict[i])