list = ['AA', 'DFG', 'Ok', 'Cool', 'qwerty']

filename=input()

with open(filename, "w") as f:
    for x in list:
        f.write(x + "\n")

print("List was written to", filename)