// Project Euler 1

package org.teel

object E1 {

  def e1_match(n: Int, acc: Int): Int = n match {
    case 0 => acc
    case _ => e1_match(n - 1, if (n % 5 == 0 || n % 3 == 0) acc + n else acc)
  }

  def e1_r(n: Int): Int = n match {
    case 0 => 0
    case _ => (if (n % 5 == 0 || n % 3 == 0) n else 0) + e1_r(n-1)
  }

  def e1_explicit(n: Int): Int = {
    var sum = 0
    for (i <- 0 until n) {
      if (i % 5 == 0 || i % 3 == 0) {
        sum += i;
      }
    }
    sum
  }

  def e1_fold_1(n: Int): Int = {
    def list = for (i <- 0 until n) yield i
    list.foldLeft(0) { (sum, i) => if (i % 5 == 0 || i % 3 == 0) sum + i else sum }    
  }
  
  def e1_fold_2(n: Int): Int = {
    def list = for ( i <- 0 until n ; if (i % 5 == 0 || i % 3 == 0) ) yield i
    list.foldLeft(0) {_+_}
  }

  def main(args: Array[String]) {
    println(e1_explicit(1000))
    println(e1_match(999, 0))
    println(e1_fold_1(1000))
    println(e1_fold_2(1000))
  }
}
