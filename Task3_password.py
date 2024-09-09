import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

pswd = input("Enter size of Password to generate : ")
while True: 
    try:
        pswd_size= int(pswd)
        if pswd_size < 5:
            print("Your number should be at least 5 ! ")
            pswd = input("Please, Enter your number again: ")
        else:
            break
    except:
        print("Please, Enter numbers only.")
        pswd = input("How many characters do you want in your password? ")
 
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
part1 = round(pswd_size * (30/100))
part2 = round(pswd_size * (20/100))
result = []
 
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2): 
    result.append(s3[x])
    result.append(s4[x])
    
random.shuffle(result)
password = "".join(result)
print("Strong Password: ", password)
 
