__author__ = 'Eddie'

import string

def input(filename):
    return [int(x) for x in open(filename,'r').read().split(',')]
def XOR(b,a):
    return int("".join(map(lambda x,y:str(int(((x)==1)==(int(y)==0))),  [int(x) for x in str(bin(a))[2:]] , [int(y) for y  in (len(str(bin(a)[2:]))-len(str(bin(b)[2:])))*'0' + str(bin(b))[2:]])),2)
def text(nums):
    return "".join([unichr(x) for x in nums])
def engrish(list):
    sum = 0
    for num in list:
        if (num<123 and num >96) or (num>64 and num<91) or (num==32):
            sum+=1
    return sum / float(len(list))
def split(list,int):
    return [[x for x in list[a::int]] for a in range(0,int)]
def get_letter(list):
    returnlist = []
    for letter in string.lowercase:
        maybel =  [XOR(x,ord(letter)) for x in list]
        returnlist.append(engrish(maybel))
    return returnlist

def decode( code_list, cipher_list):
    result = []
    x = 0
    while x<len(code_list):
        result.append(XOR(code_list[x],cipher_list[x%3]))
        x+=1
    return result

def main():
    maybel =  input('cipher1.txt')
    print maybel
    maybel1 = split(maybel,3)
    print maybel1
    maybel2 = [ get_letter(maybel1[x]) for x in range(3)]
    cipher = []
    for list in maybel2:
        cipher.append(ord(string.lowercase[list.index(max(list))]))
    print cipher
    print sum(decode( maybel , cipher))



main()



#print 107^42
#print XOR(107,42)

#have to be 65-90 or 97-122


