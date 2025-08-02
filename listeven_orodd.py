num = [2,4,5,20,43,44,78,54,237,23,34,234,2354,45,12,34,55,4,100,32]
odd_num = []
even_num = []
for a in num:
    if a%2!=0:
      odd_num.append(a)
    else:
      even_num.append(a)
print("odd number:",odd_num)
print("even number:",even_num)