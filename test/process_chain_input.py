'''
This source code takes an arithmetic chain and output a formatted
both in arithmetic and binary encoding.

For example, if the chain is "301231", the output of the program
will be

3
0
1
2
3
1

and

1 1
0 0
0 1
1 0
1 1
0 1
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