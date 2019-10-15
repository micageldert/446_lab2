def main():
   A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
   B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
   print(mult(A, B));

def mult(A, B):
   result = [[0 for x in range(len(B[0]))] for y in range(len(A))] 
   print(result)
   for i in range(len(A)):
      for j in range(len(B[0])):
         for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
   return result

def AFBT(A, B):
   result = [[0 for x in range(len(B[0]))] for y in range(len(A))] 
   rowA = [0 for q in range(len(A[0]))]
   colB = [0 for r in range(len(B))]
   print(result)
   for i in range(len(A)):
      for j in range(len(B[0])):
         for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
   return result

if __name__== "__main__":
  main()
