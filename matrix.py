def main():
   A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
   B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
   mult(A, B)
   ABFT(A, B)

def mult(A, B):
   result = [[0 for x in range(len(B[0]))] for y in range(len(A))] 
   for i in range(len(A)):
      for j in range(len(B[0])):
         for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
   return result

def ABFT(A, B):
	#Adding checksums to A
	newlist = []
	total = 0
	for m in range(len(A[0])):
		for n in A:
			total += n[m]
		newlist.append(total)
		total = 0
	A.append(newlist)

	#Adding checksums to B
	total = 0
	for r in range(len(B)):
		for s in range(len(B[r])):
			total += B[r][s]
		B[r].append(total)
		total = 0

	testmatrix = mult(A, B)

	#Check columns
	testlist = []
	total = 0
	for m in range(len(testmatrix[0])):
		for n in testmatrix:
			total += n[m]
		if (total != 2 * n[m]):
			print("column checksum error")
			print("error in column %i" %(m + 1))
		total = 0

	#Check rows
	total = 0
	for r in range(len(testmatrix)):
		for s in range(len(testmatrix[r]) - 1):
			total += testmatrix[r][s]
		if (total != testmatrix[r][s + 1]):
			print("row checksum error")
			print("error in row %i" %(r + 1))
		total = 0

	print(testmatrix)
	return testmatrix


if __name__== "__main__":
  main()
