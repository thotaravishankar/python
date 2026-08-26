a = [9,1,5,2,8,4,6,3,7,0]
#[7,6,4,3,0,9,8,5,2,1]
b = len(a)//2
first = sorted(a[:b], reverse=True)  
second = sorted(a[b:], reverse=True) 
output = second+first
print(output)



