#Notice: Password only works with integers
#Documentation: This program firs encodes the string you input to integer first, then 
# it gets the remainder of the (length of your string) and your password,
#then add it to the encoded result. Decrypt it with your password on (Decry) Level 1 Remainder Decryptor. https://replit.com/@yscmatthew/Decry-Level-1-Remainder-Decryptor#main.py

#With longer the password and longer the string, it will enhance the encoded result strength and complexity.
import math
constants = [3.141592561739,2.492828282828,1.0838171034,0.7896201647]
dish = 0
dishrecls = []
all_encry_keys = ''
temp1 = 0
temp2 = 0
temp3 = 0
temp4 = 0
temp5 = ''
key = 555
allecroad = 0
drivearr2 = 0
all_enc_keys_length = 0
#function zone (py X like js where u hv to define the fun first) 
def encrypt2():
  global all_encry_keys,temp1, temp2, temp3, temp4, all_enc_keys_length
  temp1 = (key/constants[0])
  temp2 = key/constants[1]
  temp3 = key/constants[2]
  temp4 = key/constants[3]
  temp1 = str(temp1)
  temp2 = str(temp2)
  temp3 = str(temp3)
  temp4 = str(temp4)
  #SOMETIME WORKS as the position of '.' in temp1 isn't always same as others, anyway the longer pw, less likely to happen this
  all_encry_keys = (temp1 + temp2 + temp3 + temp4)
  #all_encry_keys = str(all_encry_keys)
  all_encry_keys = all_encry_keys.replace('.','1')
  all_enc_keys_length = len(all_encry_keys)
  all_encry_keys = int(all_encry_keys)
  '''
  try:
    global all_enc_keys_length, all_encry_keys
    for i in range(len(temp1)):
      if (temp1[i] != '.') :
        all_encry_keys += temp1[i]
        all_encry_keys += temp2[i]
        all_encry_keys += temp3[i]
        all_encry_keys += temp4[i]
        all_enc_keys_length += 1
    
  except IndexError:
    print("Index error occured(based on password error)")
  for i in range(len(all_encry_keys)):
    all_encry_keys = str(all_encry_keys)
    if all_encry_keys[i] == ".":
      all_encry_keys = int(all_encry_keys)
      all_encry_keys[i] = "1"

def UNUSED():
  global dish, all_encry_keys, gostr, allecroad, key
  all_encry_keys = [int(c) for c in all_encry_keys]
  if (key / 2) > 0:
    dish += all_encry_keys[allecroad]
    allecroad += 1
    if allecroad > len(all_encry_keys):
      allecroad = 0
  else:
    dish -= all_encry_keys[allecroad]
    allecroad += 1
    if allecroad > len(all_encry_keys):
      allecroad = 0
'''


#use key's value to define add or minus
def erika():
  global drivearr2, dish, all_encry_keys, key, all_enc_keys_length, temp5
  all_encry_keys = int(all_encry_keys)
  
  if drivearr2 >= all_enc_keys_length:
    drivearr2 = 0
  else:
    all_encry_keys = str(all_encry_keys)
    temp5 = str(temp5)
    temp5 = all_encry_keys[drivearr2]
    temp5 = int(temp5)
    if key / 2 > 0:
      
      dish -= temp5
    else:
      dish += temp5
    all_encry_keys = int(all_encry_keys)
    drivearr2 += 1
    
   
      
 
  





result = ''
base = "0abcdefghijklmnopqrstuvwxyz !:)(&^%$#@*1234567890,.'ABCDEFGHIJKLMNOPQRSTUVWXYZ~`|?><;}{+_-=" #the first index (0) will never go checking #the length is 91
gostr = input("Input da words u want to encode: ")
key = int(input("input integer password key to encrypt the texts: "))
encrypt2()
print("all_encry_keys:",all_encry_keys)




for i in range(len(gostr)):
    driveArr = 1
    for driveArr in range (len(base) + 1): #starts from 1
            if gostr[i] == base[driveArr]:
                dish = driveArr
                dish += (key % len(gostr)) #Encrypt w/ caesar ciphar's method first
                dish = int(dish) #only serves 1 char
                erika()
              ###
              
                if dish > 91:
                  dish -= 91
                if dish < 0:
                  dish += 91
                  #Insert another encrypting function here

                break
    dish = str(dish)
    if len(dish) == 1:
        dish = '0' + dish
    result += dish
print("result: ",result)
