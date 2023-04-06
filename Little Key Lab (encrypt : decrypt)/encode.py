import math
#Notice: Password only works with integers
#Documentation: This program encodes the string you input first to integer, then 
# it gets the remainder of the (length of your string) and your password,
#then add it to the encoded result. Decrypt it with your password on (Decry) Level 1 Remainder Decryptor.
#With longer the password and longer the string, it will return stronger security.
constants = [3.14159265,2.71828283,1.414623562,1.13198824]
loop = []
addnum = []
temp = 0.0
     
dish = 0
result = ''
base = "0abcdefghijklmnopqrstuvwxyz !:)(&^%$#@*1234567890,.'ABCDEFGHIJKLMNOPQRSTUVWXYZ~`|?><;}{+_-=" #the first index (0) will never go checking #the length is 91
gostr = input("Input da words u want to encode: ")
key = int(input("input integer password key to encrypt the texts: "))
temp = key / constants[key % 2] #if remaindor is 1, pick constants[0], else pick constant[0]
temp = str(temp)
def toloopsum():
     i2 = 0
     for i in range(len(temp),2):
          i2 += 1
          if temp[i] != '.' :
               loop[i2] = temp[i]
               addnum[i2] = temp[i-1]
          else:
               print('hesistate at ',i,'.')



               
for i in range(len(gostr)):
    driveArr = 1
    for driveArr in range (len(base) + 1): #starts from 1
            if gostr[i] == base[driveArr]:
                dish = driveArr
                dish += (key % len(gostr))
                if dish > 91:
                     dish -= 91

                break            
    dish = str(dish)
    if len(dish) == 1:
        dish = '0' + dish
    result += dish
print(result)
print(key % len(gostr)) 
















