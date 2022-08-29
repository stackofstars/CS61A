(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond
      ((> num 0) 1)
      ((< num 0) -1)
      (else 0))
)


(define (square x) (* x x))

(define (pow x y)
  (if (= y 0)
    1
    (if (even? y)
      (square (pow x (/ y 2)))
      (* x (square (pow x (/ (- y 1) 2))))))
)


(define (unique s)
  (if (null? s)
      nil
      (cons (car s) (unique(filter (lambda (x) (not(equal? x (car s)))) s))))
)


(define (replicate x n)
  (define (replicate_help x n lst_so_far)
     (if (= n 0)
        lst_so_far
        (replicate_help x (- n 1) (append lst_so_far (cons x nil)))))
  (replicate_help x n '())
)


(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner (term n) (accumulate combiner start (- n 1) term)))
)


(define (accumulate-tail combiner start n term)
  (define (accumulate_help combiner start n term total)
    (if (= n 0)
      total
      (accumulate_help combiner start (- n 1) term (combiner total (term n)))))
  (accumulate_help combiner start n term start)
)

(define-macro (list-of map-expr for var in lst if filter-expr)
  `(map(lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
)
