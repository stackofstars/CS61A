
(define-macro (def func args body)
    `(define ,(append (cons func nil) args) ,body)
    )


(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define all-three-multiples
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) all-three-multiples))
)


(define (compose-all funcs)
  'YOUR-CODE-HERE
)


(define (partial-sums stream)
  'YOUR-CODE-HERE
  (helper 0 stream)
)
