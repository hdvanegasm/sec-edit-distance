'''
This source code takes an arithmetic chain and output a formatted
both in arithmetic and binary encoding.
'''

getbinary = lambda x, n: format(x, 'b').zfill(n)

chain = input("Input chain:\n")

L = []
for element in chain:
    n = int(element)
    L.append(n)

print("===========[ BINARY ]===============")

for n in L:
    binary = getbinary(n, 2)
    print(binary[0], binary[1])
    
print("===========[ ARITHMETIC ]===============")

for n in L:
    print(n)