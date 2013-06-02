#lang racket

;; Project Euler 3

(define (e3 n)
  (define (inner prim-factors n counter)
    (if (> counter n)
        prim-factors
        (if (= (remainder n counter) 0)
            (inner (cons counter prim-factors) (/ n counter) counter)
            (inner prim-factors n (+ counter 1)))))
  (inner null n 2))

(car (e3 600851475143))

