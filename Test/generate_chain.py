import random
import sys

if __name__ == "__main__":
    n = int(sys.argv[1])
    nucleotids = []
    for i in range(n):
        nuc = str(random.randint(0, 3))
        nucleotids.append(nuc)

    chain = "".join(nucleotids)

    with open("Test/chain_raw.txt", "w") as file_chain:
        file_chain.write(chain)
