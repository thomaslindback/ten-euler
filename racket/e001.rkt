#lang racket

;; Project Euler 1

(define (e1)
   (define (inner1 x acc) 
     (let ([is-div (or (eq? (remainder x 5) 0) (eq? (remainder x 3) 0))])
       (if (> x 0) 
           (inner1 (- x 1) (if is-div 
                               (+ acc x) 
                               acc))
           acc)))
  (inner1 999 0)
 )
(e1)
