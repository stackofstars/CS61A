(define email "staceyvu@berkeley.edu")

;; This question is in two parts, implementing `ladder-locator` and
;; `surgery-switch`. See the specifications above each definition
;; for details.
;;
;; NOTE: these parts are unrelated to each other, you can work on
;;    them in any order.

;; Part (a)
;; Implement `ladder-locator` which takes in a number `newspaper` and circles
;; all digits of value `8` in the number by returning a list of digits where all the
;; `8` digits are individually placed in a nested list.
;;
;; NOTE 1: Your function should be tail recursive
;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
;;    in a blank
;;
;; To run tests just for this part, run
;;      python3 ok -q a

(define (// numer denom) (floor (/ numer denom)))

;; scm> (ladder-locator 12)
;; (1 2)
;; scm> (ladder-locator 1881)
;; (1 (8) (8) 1)
;; scm> (ladder-locator 0) ; no digits
;; ()
;; scm> (ladder-locator 88888888)
;; ((8) (8) (8) (8) (8) (8) (8) (8))
;; scm> (ladder-locator 1128651)
;; (1 1 2 (8) 6 5 1)

(define (ladder-locator newspaper)
    (define (helper newspaper lstsofar)
        (define current-digit
            (modulo newspaper 10))
        (define value
            (if
                (= current-digit 8)
                (cons 8 nil)
                current-digit))
        (if
            (not(= newspaper 0))
            (helper
                (// newspaper 10)
                (cons value lstsofar))))
    (helper newspaper ()))

;; Part (b)
;; The `surgery-switch` operation takes in two infinite streams `zk` and `bt`
;; and returns a new stream containing the non-city elements of each stream,
;; alternating from one stream to the other when encountering the symbol
;; `city`.
;;
;; Note: the symbol `city` should not appear in the final stream.
;;
;;
;; To run tests just for this part, run
;;      python3 ok -q b

;; the following function is defined for testing, and takes the first
;; k elements of a stream `s`, returning them as a list.
(define (take k s)
    (if (zero? k)
        nil
        (cons
            (car s)
            (take (- k 1) (cdr-stream s)))))

;; scm> (define just-city (cons-stream 'city just-city))
;; just-city
;; scm> (define two (cons-stream 1 (cons-stream 'city two)))
;; two
;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'city three))))
;; three
;; scm> (take 10 two)
;; (1 city 1 city 1 city 1 city 1 city)
;; scm> (take 10 three)
;; (x y city x y city x y city x)
;; scm> (take 10 (surgery-switch two three))
;; (1 x y 1 x y 1 x y 1)
;; scm> (take 10 (surgery-switch two just-city))
;; (1 1 1 1 1 1 1 1 1 1)
;; scm> (take 10 (surgery-switch three three))
;; (x y x y x y x y x y)

(define (surgery-switch zk bt)
	(if ______
		______
		(cons-stream ______ ______)))


; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `ladder-locator` and
; ;; `surgery-switch`. See the specifications above each definition
; ;; for details.
; ;;
; ;; NOTE: these parts are unrelated to each other, you can work on
; ;;    them in any order.

; ;; Part (a)
; ;; Implement `ladder-locator` which takes in a number `newspaper` and circles
; ;; all digits of value `8` in the number by returning a list of digits where all the
; ;; `8` digits are individually placed in a nested list.
; ;;
; ;; NOTE 1: Your function should be tail recursive
; ;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
; ;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
; ;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a

; (define (// numer denom) (floor (/ numer denom)))

; ;; scm> (ladder-locator 12)
; ;; (1 2)
; ;; scm> (ladder-locator 1881)
; ;; (1 (8) (8) 1)
; ;; scm> (ladder-locator 0) ; no digits
; ;; ()
; ;; scm> (ladder-locator 88888888)
; ;; ((8) (8) (8) (8) (8) (8) (8) (8))
; ;; scm> (ladder-locator 1128651)
; ;; (1 1 2 (8) 6 5 1)

; (define (ladder-locator newspaper)
;     (define (helper newspaper ______)
;         (define current-digit
;             ______)
;         (define value
;             (if
;                 ______
;                 ______
;                 ______))
;         (if ______
;             ______
;             (helper
;                 ______
;                 (cons value ______))))
;     (helper ______ ______))

; ;; Part (b)
; ;; The `surgery-switch` operation takes in two infinite streams `zk` and `bt`
; ;; and returns a new stream containing the non-city elements of each stream,
; ;; alternating from one stream to the other when encountering the symbol
; ;; `city`.
; ;;
; ;; Note: the symbol `city` should not appear in the final stream.
; ;;
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q b

; ;; the following function is defined for testing, and takes the first
; ;; k elements of a stream `s`, returning them as a list.
; (define (take k s)
;     (if (zero? k)
;         nil
;         (cons
;             (car s)
;             (take (- k 1) (cdr-stream s)))))

; ;; scm> (define just-city (cons-stream 'city just-city))
; ;; just-city
; ;; scm> (define two (cons-stream 1 (cons-stream 'city two)))
; ;; two
; ;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'city three))))
; ;; three
; ;; scm> (take 10 two)
; ;; (1 city 1 city 1 city 1 city 1 city)
; ;; scm> (take 10 three)
; ;; (x y city x y city x y city x)
; ;; scm> (take 10 (surgery-switch two three))
; ;; (1 x y 1 x y 1 x y 1)
; ;; scm> (take 10 (surgery-switch two just-city))
; ;; (1 1 1 1 1 1 1 1 1 1)
; ;; scm> (take 10 (surgery-switch three three))
; ;; (x y x y x y x y x y)

; (define (surgery-switch zk bt)
; 	(if ______
; 		______
; 		(cons-stream ______ ______)))
