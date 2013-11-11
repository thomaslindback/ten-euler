package main

import (
	"fmt"
	"strconv"
	"math/big"
	"math"
)

type pair struct {
	a,  b *big.Int
}

func main() {
	fmt.Printf("Hello world!\n")

	fmt.Printf("%v\n", 123)
	fmt.Printf("%v\n", 123 % 10)
	fmt.Printf("%v\n", 123 / 10)
	fmt.Printf("%v\n", strconv.Itoa(123 % 10))

	var i uint64 = 11929663269433863309
	fmt.Printf("%v\n", strconv.FormatUint(i, 10))
	fmt.Printf("%v\n", strconv.FormatUint(i*10, 10))

	fmt.Printf("%v\n", math.Sqrt(4)*math.Sqrt(4) == 4)

}
