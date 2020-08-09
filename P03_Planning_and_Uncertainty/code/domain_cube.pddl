(define (domain cube)
  (:requirements :strips :typing:equality
                 :universal-preconditions
                 :conditional-effects)
  (:types colour block) ; 
  (:constants white yellow green blue orange red - colour b1 b2 b3 b4 b5 b6 b7 b8 - block)
  (:predicates   
        (on ?b - block ?x - colour ?y - colour ?z - colour)
        ;(finish ?a ?b ?c ?d - colour ?x - surface) ;the surface only has one colour
        ;finish(surface) :- any colour on the surface are the same
        )
    ; R 右面 L 左面 F 前面 B 后面 U 上面 D 下面 
    ; R顺时针 R'逆时针
    ; x:F,B y:R,L z:U,D
  (:action move_F
      :effect (and
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b1 ?x ?y ?z) (and (on b2 ?x ?z ?y) (not (on b1 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b2 ?x ?y ?z) (and (on b4 ?x ?z ?y) (not (on b2 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b3 ?x ?y ?z) (and (on b1 ?x ?z ?y) (not (on b3 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b4 ?x ?y ?z) (and (on b3 ?x ?z ?y) (not (on b4 ?x ?y ?z)))))          
      )
    )
  (:action move_F2
      :effect (and
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b1 ?x ?y ?z) (and (on b3 ?x ?z ?y) (not (on b1 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b2 ?x ?y ?z) (and (on b1 ?x ?z ?y) (not (on b2 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b3 ?x ?y ?z) (and (on b4 ?x ?z ?y) (not (on b3 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b4 ?x ?y ?z) (and (on b2 ?x ?z ?y) (not (on b4 ?x ?y ?z)))))          
      )
    )
  (:action move_R
      :effect (and
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b2 ?x ?y ?z) (and (on b6 ?z ?y ?x) (not (on b2 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b4 ?x ?y ?z) (and (on b2 ?z ?y ?x) (not (on b4 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b6 ?x ?y ?z) (and (on b8 ?z ?y ?x) (not (on b6 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b8 ?x ?y ?z) (and (on b4 ?z ?y ?x) (not (on b8 ?x ?y ?z)))))          
      )
    )
  (:action move_R2
      :effect (and
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b2 ?x ?y ?z) (and (on b4 ?z ?y ?x) (not (on b2 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b4 ?x ?y ?z) (and (on b8 ?z ?y ?x) (not (on b4 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b6 ?x ?y ?z) (and (on b2 ?z ?y ?x) (not (on b6 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b8 ?x ?y ?z) (and (on b6 ?z ?y ?x) (not (on b8 ?x ?y ?z)))))          
      )
    )
  (:action move_U
      :effect (and
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b1 ?x ?y ?z) (and (on b5 ?y ?x ?z) (not (on b1 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b2 ?x ?y ?z) (and (on b1 ?y ?x ?z) (not (on b2 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b5 ?x ?y ?z) (and (on b6 ?y ?x ?z) (not (on b5 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b6 ?x ?y ?z) (and (on b2 ?y ?x ?z) (not (on b6 ?x ?y ?z)))))          
      )
    )
  (:action move_U2
      :effect (and
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b1 ?x ?y ?z) (and (on b2 ?y ?x ?z) (not (on b1 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b2 ?x ?y ?z) (and (on b6 ?y ?x ?z) (not (on b2 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b5 ?x ?y ?z) (and (on b1 ?y ?x ?z) (not (on b5 ?x ?y ?z)))))
      (forall(?x - colour ?y - colour ?z - colour) 
        (when (on b6 ?x ?y ?z) (and (on b5 ?y ?x ?z) (not (on b6 ?x ?y ?z)))))          
      )
    )
  
)