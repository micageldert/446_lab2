# LAB 2 PART 1

import sys

def main():
   codeword = int(sys.argv[1])
   if (sys.argv[2] == "encode"):
      new = parityEncode(codeword)
      print("input  {0:015b}".format(codeword) + " ")
      print("output {0:016b}".format(new))
   else:
      print("input  {0:015b}".format(codeword) + " ")
      parityDecode(codeword)

def parityEncode(codeword):   #even parity
   new = codeword
   cnt = countOnes(codeword)
   if (cnt % 2 == 0):   #if even append 0
      new = new << 1 
   else:                #if odd append 1
      new  = (new << 1) | 1 
   return new
  
def parityDecode(codeword):
   cnt = countOnes(codeword)
   if (cnt % 2 == 0):   #if even no error found
      print("no error found")
      return True
   else:                #if odd possible error
      print("possible error found")
      return False 
 
def countOnes(codeword):
   cnt = 0
   for i in range(0, 16, 1):  #count up number of ones in codeword
      test = codeword & 1
      if (test == 1):
         cnt+=1
      codeword = codeword >> 1    
   return cnt


if __name__== "__main__":
  main()
