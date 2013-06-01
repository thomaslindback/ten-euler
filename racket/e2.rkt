#lang racket

;; Project Euler 2

(define (e2)
  (let ([v1 1]
        [v2 2]
        [max 4000000])
    (define (inner v1 v2 acc) 
      (if (>= (+ v1 v2) max)
          acc
          (inner v2 (+ v1 v2) 
                 (if (eq? (remainder (+ v1 v2) 2) 0) 
                     (+ v1 v2 acc)
                     acc))))
    (inner v1 v2 2)))

(e2)
    
