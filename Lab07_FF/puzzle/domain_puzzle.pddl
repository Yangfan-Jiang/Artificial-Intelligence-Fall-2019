(define (domain puzzle)
  (:requirements :strips :equality:typing)
  (:types num loc) 
  (:predicates  (empty ?x - loc)
                (at ?x - num ?y - loc)
                (near ?x - loc ?y - loc))

(:action slide
             :parameters (?x - num ?z - loc ?y - loc)
             :precondition (and (empty ?y) (at ?x ?z) (near ?z ?y) )
             :effect (and (not (empty ?y)) (empty ?z) (not (at ?x ?z)) (at ?x ?y) ) 
)
)