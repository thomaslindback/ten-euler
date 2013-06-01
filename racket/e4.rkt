#lang racket

(require racket/format)

;; Project Euler 4

(define (palindrome? s)
  (string=? s (list->string (reverse (string->list s)))))

(palindrome? (~a 123321))

(define (e4 low high)
  (define (inner pal-list low high cnt)
    (+ low high))
  (inner null low high low))
    
; (begin (display (string-append (~a low) "\n")) low))

(e4 10 15)