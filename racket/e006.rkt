#lang racket

;; Project Euler 6

(define N 100)
(- (sqr (/ (* N (+ N 1)) 2)) ; square of sum
   (/ (* N (+ N 1) (+ (* 2 N) 1)) 6)) ; sum of squares