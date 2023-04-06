#Notice: Use my another program ('Encry) Level 1 Remainder Encryptor to get the encrypted numbers first.
base = "0abcdefghijklmnopqrstuvwxyz !:)(&^%$#@*1234567890,.'ABCDEFGHIJKLMNOPQRSTUVWXYZ~`|?><;}{+_-="  #len = 91
gonum = input("type in da words u want to decode: ")  #it will remain as str
print(gonum)
dec_key = int(input("please input the password: "))
doublepick = ''
decode_result = ''
constants = [3.141592561739,2.492828282828,1.0838171034,0.7896201647]
all_dec_ref = ''
temp1 = 0
temp2 = 0
temp3 = 0
all_dec_ref_len = 0
dec_arr_driver = 0
#func zone{

def makekey():
  global constants, all_dec_ref, temp1, all_dec_ref_len, dec_key
  for i in range(0,4):
    temp1 = float(temp1)
    temp1 = dec_key / constants[i]
    temp1 = str(temp1)
    all_dec_ref = all_dec_ref + temp1
    all_dec_ref = all_dec_ref.replace(".","1")
  all_dec_ref_len = len(all_dec_ref)
  print("Decode Reference Key Values",all_dec_ref)

def decrypt2():
  global temp2, all_dec_ref, all_dec_ref_len, dec_arr_driver, dec_key, doublepick, gonum
  if dec_arr_driver >= all_dec_ref_len:
    dec_arr_driver = 0
  else:
    temp2 = str(temp2)
    temp2 = all_dec_ref[dec_arr_driver]
    temp2 = int(temp2)
    if (dec_key / 2) > 0:
      doublepick += temp2
    else:
      doublepick -= temp2
    dec_arr_driver += 1 
  

makekey()
for x in range(0, len(gonum), 2):
  #doublepick {
  doublepick = gonum[x]
  doublepick += gonum[x + 1]
  doublepick = int(doublepick)
  #}
  decrypt2()

  doublepick -= (dec_key % (len(gonum) / 2))
  if doublepick < 0:
    doublepick += 91
  if doublepick > 91:
    doublepick -= 91  
  decode_result = (decode_result + base[int(doublepick)])

print("Decode result: ", decode_result)
print('PW remainder: ',(dec_key % len(gonum)))