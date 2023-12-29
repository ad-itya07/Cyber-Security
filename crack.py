import hashlib

file_path = r'D:\CyberSecurity\Project 1\password list(INITIAL).txt' # here 'r' denotes a "RAW STRING" where '\' ae traeted as normal charecter insteead of special meaning like '\n , \t, etc'

# opening the file:
file = open(file_path,'r')

# NOW, APPEnding the words from the '1000 paswwords' into a list
password_list = []
for line in file:
    password_list.append(line.strip())

print("Len before variation:", len(password_list))
#closing the file
file.close()

# now going with the variations (Capitalising/lowercasing one charecter at a time):
initial_length = len(password_list)

for i in range(initial_length):
    element = password_list[i]
    variations = []
    for j in range(len(element)):
        modified_element = element[:j] + element[j].swapcase() + element[j + 1:]
        variations.append(modified_element)
    password_list.extend(variations)

# 2nd variation: swapping the case of all elements in the word at once:

for i in range(initial_length):
    element = password_list[i]
    variations = []
    variations.append(element.swapcase())
    password_list.extend(variations)

# converting the list into set:
password_set = set(password_list)
print("Length of my dictionary(with variation):",len(password_set))

# print(password_set)

#NOw declaring the target hash
target_hash = "0421ac277aa224d073284dca5f5aa8d536c7a02e6ecf195708cb3d7eca7f33bf"

#now using for loop to iterate over all the elements of the dictionary
for i in password_set:

    #we have to check which password's HASH CODE is matching with the target HASH code
            # first find the HASH CODE of iTH element
    hash_code = hashlib.sha256(i.encode()).hexdigest()

    # USING 'IF' to check:
    if hash_code == target_hash:
        print("Cracked! Password is:", i)
        break

else:
    print("Failed! Password Not Found.")
    

# ***NOTE: 1. hashlib: This is a Python library that PROVIDES VARIOUS HASHING ALGOs, including SHA-256.
    #      2. i.encode(): The .encode() method is used to convert the 'i' into bytes. 
    #                           HASH FUNC. WORK ON BYTES SO IT'S NECESSARY TO CONVERT THE STRING TO BYTES FOR HASHING
    #      3. hashlib.sha256(...): This part initializes a new SHA-256 hash object from the hashlib module using the bytes obtained from i.encode()
    #      4. .hexdigest(): This method is used to obtain the hexadecimal digest (the string representation) of the hash. 
    #                       The output of a hash function is a series of bytes, but .hexdigest() converts it into a human-readable hexadecimal string.