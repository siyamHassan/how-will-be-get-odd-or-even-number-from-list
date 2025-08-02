num = [2,4,5,20,43,44,78,54,237,23,34,234,2354,45,12,34,55,4,100,32]
odd = [a for a in num if a%2!=0]
even = [x for x in num if x%2==0]
print(odd)
print(even)