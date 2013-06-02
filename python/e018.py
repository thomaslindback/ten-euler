# euler 18
dic = {}

dic['r1'] = [75]
dic['r2'] = [95, 64]
dic['r3'] = [17, 47, 82]
dic['r4'] = [18, 35, 87, 10]
dic['r5'] = [20, 4, 82, 47, 65]
dic['r6'] = [19, 01, 23, 75, 3, 34]
dic['r7'] = [88, 02, 77, 73, 7, 63, 67]
dic['r8'] = [99, 65, 04, 28, 6, 16, 70, 92]
dic['r9'] = [41, 41, 26, 56, 83, 40, 80, 70, 33]
dic['r10'] = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
dic['r11'] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
dic['r12'] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
dic['r13'] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
dic['r14'] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
dic['r15'] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
print(dic)
n =len(dic)

for i in range(n-1,0,-1):
	row = dic['r'+ str(i)]
	next = dic['r'+ str(i+1)]
	for idx, val in enumerate(row):
		row[idx] += max(next[idx],next[idx+1])
	print(dic)
	
print(dic['r1'])