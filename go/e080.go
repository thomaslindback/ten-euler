package main

import (
	"fmt"
	"strconv"
	"math/big"
)

type pair struct {
	a,   b *big.Int
}

func sumOfDigitsD(n int64) int {
	return sumOfDigitsS(strconv.FormatInt(n, 10))
}

func sumOfDigitsS(str string) (sum int) {
	sum = 0
	for _, c := range str { sum += (int(c) - 48) }
	return
}

func setup(n *big.Int) pair {
	return pair{big.NewInt(0).Mul(big.NewInt(5), n), big.NewInt(5)}
}

//http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
func step(p pair) pair {
	if p.a.Cmp(p.b) == 1 || p.a.Cmp(p.b) == 0 {
		return pair{big.NewInt(0).Sub(p.a, p.b), big.NewInt(0).Add(p.b, big.NewInt(10))}
	} else {
		five := big.NewInt(5)
		hundred := big.NewInt(100)
		ten := big.NewInt(10)

		t1 := big.NewInt(0).Div(p.b, ten)
		t2 := big.NewInt(0).Mul(t1, hundred)
		return pair{big.NewInt(0).Mul(p.a, big.NewInt(100)),
			big.NewInt(0).Add(t2, five)}
	}
}

func calc_sqrt(n int64, max_len int) string {
	var pp pair = setup(big.NewInt(n))

	for len(pp.a.String()) < max_len + 5 {
		//fmt.Printf("%v, %v\n", pp.a.String(), pp.b.String())
		pp = step(pp)
		if pp.a.Cmp(big.NewInt(0)) == 0 {
			s := pp.b.String()
			return s[0:len(s)-1]
		}
	}
	s := pp.b.String()
    return s[0:max_len]
}

func main() {
	all_sum := 0
	for i := 1; i <= 100; i++ {
		s := calc_sqrt(int64(i), 100)
		if len(s) == 100 {
			all_sum = all_sum + sumOfDigitsS(s)
		}
	}
	fmt.Printf("Euler 80. Result %v\n", all_sum)
}
