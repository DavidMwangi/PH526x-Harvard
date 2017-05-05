"""

Abraham Lincoln was a president during the American Civil War.
His famous 1863 Gettysburg Address has been stored as address,
and the counter function defined in part 1c has been loaded.
Use these to return a dictionary consisting of the count of each
letter in this address, and save this as address_count.
Print address_count.

"""

from func import counter

address_count = {}

with open("address.txt") as f:

    address = [line.rstrip('\n') for line in f]

count = 0

while count < len(address):

    taddress_count = counter(address[count])

    for key in taddress_count.keys():

        if key in address_count.keys():

            taddress_count[key] += address_count[key]
        
    count += 1
    address_count.update(taddress_count)

print(address_count)
