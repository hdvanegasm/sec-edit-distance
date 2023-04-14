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


def getbinary(x, n):
    return format(x, "b").zfill(n)


with open("Test/chain_raw.txt", "r") as file_chain:
    chain = file_chain.read()

L = []
for element in chain:
    n = int(element)
    L.append(n)

# Output binary
output_string = ""
for n in L:
    binary = getbinary(n, 2)
    output_string += str(binary[0]) + " " + str(binary[1]) + "\n"

output_string += "\n" + "========" + "\n\n"

for n in L:
    output_string += str(n) + "\n"

print("Writing in file")
with open("Test/chain_converted.txt", "w") as converted_file:
    converted_file.write(output_string)
