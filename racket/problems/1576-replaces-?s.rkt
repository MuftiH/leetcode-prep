#lang racket

(define (unique a b)
    (define alph 
            (vector #\a #\b #\c #\d #\e #\f #\g #\h #\i #\j #\k #\l
                    #\m #\n #\o #\p #\q #\r #\s #\t #\u #\v #\w #\x 
                    #\y #\z))

    (define (unique? ch)
        (not (or (equal? ch a) (equal? ch b))))

    (define (go i)
        (if (unique? (vector-ref alph i))
            (vector-ref alph i) 
            (go (add1 i))))
    (go 0))

(define (modify-string s)
  
  (list->string
      (reverse
      (foldl (lambda (x i acc)
           (cons (match x
                   [#\? (unique (if (= i 0) x (car acc))
                                (string-ref s (min (add1 i) (sub1 (string-length s)))))]
                   [_ x])
                 acc))
         '()
         (string->list s)
         (range (string-length s))))))