# euler 17

dic = {}

dic[1] = 'one'
dic[2] = 'two'
dic[3] = 'three'
dic[4] = 'four'
dic[5] = 'five'
dic[6] = 'six'
dic[7] = 'seven'
dic[8] = 'eight'
dic[9] = 'nine'
dic[10] = 'ten'
dic[11] = 'eleven'
dic[12] = 'twelve'
dic[13] = 'thirteen'
dic[14] = 'fourteen'
dic[15] = 'fifteen'
dic[16] = 'sixteen'
dic[17] = 'seventeen'
dic[18] = 'eighteen'
dic[19] = 'nineteen'
dic[20] = 'twenty'
dic[30] = 'thirty'
dic[40] = 'forty'
dic[50] = 'fifty'
dic[60] = 'sixty'
dic[70] = 'seventy'
dic[80] = 'eighty'
dic[90] = 'ninety'
dic[100] = 'hundred'
dic[1000] = 'onethousand'

def num2str(num):
	sr = ''
	if len(str(num)) == 3:
		li = map(int, list(str(num)))
		sr = dic[li[0]] + 'hundred'
		if li[1] > 0 or li[2] > 0:
			sr += 'and'
		# the tens
		tens = li[1]*10+li[2]
		if tens >= 10 and tens < 20:
			sr += dic[tens]
		else:
			if li[1] > 0:
				sr += dic[li[1]*10] 
			if li[2] > 0:
				sr += '' + dic[li[2]]
	if len(str(num)) == 2:
		li = map(int, list(str(num)))
		if li[0] >=2:
			sr = dic[li[0]*10]
		if li[1] > 0:
			sr += '' + dic[li[1]]
	return sr

total_len = 0
for i in range(1,1001):
	if i < 20:
		s = dic[i]
	elif i >=20 and i < 1000:
		s = num2str(i)
	elif i == 1000:
		s = dic[i]
	total_len += len(s)
	print(i, s)

print(total_len)
if total_len != 21124:
	print('------------------ERROR')

print(100,  len(num2str(100)), num2str(100))
print(110,  len(num2str(110)), num2str(110))
print(111,  len(num2str(111)), num2str(111))
print(112,  len(num2str(112)), num2str(112))
print(113,  len(num2str(113)), num2str(113))
print(342,  len(num2str(342)), num2str(342))
print(115,  len(num2str(115)), num2str(115))