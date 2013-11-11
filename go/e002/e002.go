package main

import "fmt"

func fib () chan int {
	yield := make (chan int);
	a,b := 1,2;
	go func () {
		for {
			yield <- a+b
			tmp := a; a=b; b=tmp+b
		}
	} ();
	return yield
}

func main() {
	fibs := fib();
	sum := 2
	next_fib := 0
	for next_fib <= 4000000 {
		next_fib = <-fibs
		if next_fib%2 == 0 {
			sum += next_fib
		}
	}
	fmt.Printf("Euler 2. Result: %v\n", sum)
}
