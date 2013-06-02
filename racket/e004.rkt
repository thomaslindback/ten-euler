#lang racket

(require racket/format)

;; Project Euler 4

(define (palindrome? s)
  (string=? s (list->string (reverse (string->list s)))))

(define (make-list from to)
  (build-list (+ 1 (- to from)) (lambda (x) (+ x from))))

(define (filter-palindromes from to)
  (let ([ll (map (lambda (x) (* from x)) (make-list from to))])
    (filter (lambda (x) (palindrome? (~a x))) ll)))

(define (e4 from to) 
  (if (> from to)
      null
      (cons (filter-palindromes from to) (e4 (+ 1 from) to))))

(car (sort (flatten(e4 100 999)) >))
