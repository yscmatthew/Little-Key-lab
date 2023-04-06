
base = "0abcdefghijklmnopqrstuvwxyz !:)(&^%$#@*1234567890,.'ABCDEFGHIJKLMNOPQRSTUVWXYZ~`|?><;}{+_-=" #len = 91
gonum = input("type in da words u want to decode: ") #it will remain as str 
print(gonum)
dec_key = int(input("please input the password: "))
doublepick = ''
decode_result = ''
for x in range(0,len(gonum),2):
    #doublepick [
    doublepick = gonum[x]
    doublepick += gonum[x + 1]
    doublepick = int(doublepick)
    #]

    doublepick -= (dec_key % (len(gonum) / 2))
    if doublepick < 0:
        doublepick += 91
    decode_result = (decode_result + base[int(doublepick)])
    
print(decode_result)
print(doublepick)





        
