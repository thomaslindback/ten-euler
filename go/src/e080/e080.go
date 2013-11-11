/**
 * Created with IntelliJ IDEA.
 * User: thomas
 * Date: 2013-11-10
 * Time: 19:04
 * To change this template use File | Settings | File Templates.
 */
package main

import (
	"fmt"
	"strconv"
	"math/big"
)

type pair struct {
	a,  b *big.Int
}

func sumOfDigitsD(n int64) int {
	return sumOfDigitsS(strconv.FormatInt(n, 10))
}

func sumOfDigitsS(str string) (sum int) {
	sum = 0
	for _, c := range str {
		sum += (int(c) - 48)
	}
	return
}

func setup(n *big.Int) pair {
	return pair{big.NewInt(0).Mul(big.NewInt(5), n), big.NewInt(5)}
}

//http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf
func step(p pair) pair {
	if p.a.Cmp(p.b) == 1 {
		return pair{big.NewInt(0).Sub(p.a, p.b), big.NewInt(0).Add(p.b, big.NewInt(10))}
	} else {
		five := big.NewInt(5)
		hundred := big.NewInt(100)
		ten := big.NewInt(10)

		t1 := big.NewInt(0).Div(p.b,ten)
		t2 := big.NewInt(0).Mul(t1, hundred)
		return  pair{big.NewInt(0).Mul(p.a, big.NewInt(100)),
			big.NewInt(0).Add(t2, five)}
	}
}

func main() {
	fmt.Printf("Hello world!\n")

	var pp pair = setup(big.NewInt(2))
	fmt.Printf("%v, %v\n", pp.a.String(), pp.b.String())
	pp = step(pp)
	fmt.Printf("%v, %v\n", pp.a.String(), pp.b.String())
	pp = step(pp)
	fmt.Printf("%v, %v\n", pp.a.String(), pp.b.String())

	for i := 0; i < 2000; i++ {
		pp = step(pp)
		//fmt.Printf("%v, %v\n", pp.a.String(), pp.b.String())
		if len(pp.b.String()) == 110 {
			break
		}
	}
	fmt.Printf("%v\n", pp.b.String())
	s := pp.b.String()

	decimals := s[0:100]
	fmt.Printf("decimals %v\n", decimals)
	fmt.Printf("sum digits %v\n", sumOfDigitsS(decimals))

}
