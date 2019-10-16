# LAB 2 PART 1

import sys

def main():
   codeword = int(sys.argv[1])
   print("Hamming Code:")
   if (sys.argv[2] == "encode"):
      new = hamEncode(codeword)
      print("input  {0:04b}".format(codeword) + " ")
      print("output {0:07b}".format(new))
   else:
      print("input  {0:07b}".format(codeword) + " ")
      hamDecode(codeword)

# codeword: P1 P2 X3 P4 X2 X1 X0
# P1 = X0 xor X2 xor X3
# P2 = X3 xor X0 xor X1
# P4 = X2 xor X0 xor X1
def hamEncode(data):
   p1 = getBit(data, 0) ^ getBit(data, 2) ^ getBit(data, 3)
   p2 = getBit(data, 0) ^ getBit(data, 1) ^ getBit(data, 3)
   p4 = getBit(data, 1) ^ getBit(data, 2) ^ getBit(data, 0)
   code = getBit(data, 0) | (getBit(data, 1) << 1) | (getBit(data, 2) << 2) | (p4 << 3) | (getBit(data, 3) << 4) | (p2 << 5) | (p1 << 6) 
   return code   

# syndrome: C2 C1 C0
# bit pos: 1(MSB) -> 7(LSB)
def hamDecode(data):
   p1 = getBit(data, 6)
   p2 = getBit(data, 5)
   x3 = getBit(data, 4)
   p4 = getBit(data, 3)
   x2 = getBit(data, 2)
   x1 = getBit(data, 1)
   x0 = getBit(data, 0)
   c0 = p1 ^ x3 ^ x2 ^ x0
   c1 = p2 ^ x3 ^ x1 ^ x0
   c2 = p4 ^ x2 ^ x1 ^ x0
   syndrome = (c2 << 2) | (c1 << 1) | c0
   if syndrome == 0:
      print("no error found");
      return True
   else:
      err = syndrome
      cor = data ^ (1 << (7-syndrome))
      #correct = (getBit(cor, 4) << 3) | (cor & 7)
      #orig = (getBit(data, 4) << 3) | (data & 7)
      print("error in bit %d" %err)
      print("corrected data: {0:07b}".format(cor))  
      return False

def getBit(num, bit_pos):
   mask = 1 << (bit_pos)
   bit = (num & mask) >> bit_pos
   return bit   

if __name__== "__main__":
  main()
