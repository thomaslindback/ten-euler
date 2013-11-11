/**
 * Created with IntelliJ IDEA.
 * User: thomas
 * Date: 2013-11-10
 * Time: 19:02
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

func main() {
	fmt.Printf("Hello world!\n")

	fmt.Printf("%v\n", 123)
	fmt.Printf("%v\n", 123 % 10)
	fmt.Printf("%v\n", 123 / 10)
	fmt.Printf("%v\n", strconv.Itoa(123 % 10))

	var i uint64 = 11929663269433863309
	fmt.Printf("%v\n", strconv.FormatUint(i, 10))
	fmt.Printf("%v\n", strconv.FormatUint(i*10, 10))

}
