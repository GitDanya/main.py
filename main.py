import random
simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input('length:'))

password = ''

for i in range(pass_length):
    password += random.choice(simvols)

print(password)    
