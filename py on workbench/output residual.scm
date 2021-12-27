(define port)
(set! port (open-output-file "residuals.dat"))
(do
((i 0 (+ i 1)))
((= i (length (solver-residuals))))
(format port "~a ~2t" (car (list-ref (solver-residuals) i)))
)
(newline port)