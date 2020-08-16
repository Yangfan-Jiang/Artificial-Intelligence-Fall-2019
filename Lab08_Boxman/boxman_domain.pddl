(define (domain boxman)
  (:requirements :strips :typing:equality
                 :universal-preconditions
                 :conditional-effects)
  (:types pos man pearl)
  (:predicates   
        (wall ?x - pos)
  	    (move ?x ?y - pos)
  	    (push ?x ?y - pos)
  	    (near ?x ?y - pos)
        (clear ?x - pos)
        (manpos ?x - pos)
        (boxpos ?y - pos)
        (atline ?m ?x ?y - pos)
        (pearlpos ?p - pos)
    )
        
  (:action move
             :parameters (?x ?y - pos)
             :precondition (and (manpos ?x) (or (near ?x ?y) (near ?y ?x)) (clear ?y) )
             :effect (and (not(manpos ?x)) (manpos ?y) )
    )

  (:action push
             :parameters (?m ?x ?y - pos)
             :precondition (and (boxpos ?x) (or (near ?x ?y) (near ?y ?x)) (clear ?y) 
                            (or (atline ?m ?x ?y) (atline ?y ?x ?m)) (manpos ?m)
                           )
             :effect ( and (not(boxpos ?x)) (boxpos ?y) (clear ?x) (not (clear ?y)) 
                       (not (manpos ?m)) (manpos ?x) 
                     )
  )
)