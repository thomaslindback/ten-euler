# Project Euler 7

require 'prime'

cnt, res = 0, 0

Prime.each { |prime|
	if cnt >= 10001
		break
	else
		cnt += 1
		res = prime
	end 
}

p res
