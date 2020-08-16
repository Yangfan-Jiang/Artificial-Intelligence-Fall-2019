% gender

male(george).
male(spencer).
male(philip).
male(charles).
male(mark).
male(andrew).
male(edward).
male(william).
male(harry).
male(peter).
male(james).

female(mum).
female(kydd).
female(elizabeth).
female(margaret).
female(diana).
female(anne).
female(sarah).
female(sophie).
female(zara).
female(beatrice).
female(eugenie).
female(louise).

% child
child(elizabeth,george).
child(elizabeth,mum).
child(margaret,george).
child(margaret,mum).

child(diana,spencer).
child(diana,kydd).

child(charles,elizabeth).
child(charles,philip).
child(anne,elizabeth).
child(anne,philip).
child(andrew,elizabeth).
child(andrew,philip).
child(edward,elizabeth).
child(edward,philip).

child(william,diana).
child(william,charles).
child(harry,diana).
child(harry,charles).

child(peter,anne).
child(peter,mark).
child(zara,anne).
child(zara,mark).

child(beatrice,andrew).
child(beatrice,sarah).
child(eugenie,andrew).
child(eugenie,sarah).

child(louise,edward).
child(louise,sophie).
child(james,edward).
child(james,sophie).

% sibling
sibling(elizabeth,margaret).
sibling(margaret,elizabeth).

sibling(charles,anne).
sibling(anne,charles).
sibling(charles,andrew).
sibling(andrew,charles).
sibling(charles,edward).
sibling(edward,charles).
sibling(anne,andrew).
sibling(andrew,anne).
sibling(anne,edward).
sibling(edward,anne).
sibling(andrew,edward).
sibling(edward,andrew).

sibling(william,harry).
sibling(harry,william).
sibling(peter,zara).
sibling(zara,peter).
sibling(beatrice,eugenie).
sibling(eugenie,beatrice).
sibling(louise,james).
sibling(james,louise).

% spouse
spouse(george,mum).
spouse(mum,george).
spouse(elizabeth,philip).
spouse(philip,elizabeth).
spouse(spencer,kydd).
spouse(kydd,spencer).
spouse(diana,charles).
spouse(charles,diana).
spouse(anne,mark).
spouse(mark,anne).
spouse(andrew,sarah).
spouse(sarah,andrew).
spouse(edward,sophie).
spouse(sophie,edward).

father(X,Y):-child(Y,X),male(X).
mother(X,Y):-child(Y,X),female(X).

grandchildren(X,Y):-child(X,Z),child(Z,Y).
greatgrandparent(X,Y):-child(Y,Z),grandchildren(Z,X).

ancestors(X,Y):-child(Y,X).
ancestors(X,Y):-child(Y,Z),ancestors(X,Z).

brother(X,Y):-sibling(X,Y),male(X).
sister(X,Y):-sibling(X,Y),female(X).
daughter(X,Y):-child(X,Y),female(X).
son(X,Y):-child(X,Y),male(X).
firstcousin(X,Y):-child(X,A),child(Y,B),sibling(A,B).
brotherinlaw(X,Y):-spouse(Y,Z),brother(X,Z).
sisterinlaw(X,Y)::-spouse(Y,Z),sister(X,Z).
aunt(X,Y):-child(Y,Z),sister(Z,X).
uncle(X,Y):-child(Y,Z),brother(Z,X).

distance_n(X,Y,N):-ancestors(A,X),ancestors(A,Y),distance(A,X,Ret1),distance(A,Y,Ret2),N is abs(Ret1-Ret2).
distance_m(X,Y,M):-ancestors(A,X),ancestors(A,Y),distance(A,Y,Ret1),M is Ret1-1.
distance(X,X,0).
distance(X,Y,Ret):-child(Y,Z),ancestors(X,Z),distance(X,Z,Ret1),Ret is Ret1+1.


mthCousinNremoved(X,Y,M,N):-distance_m(X,Y,Ret1),distance_n(X,Y,Ret2),M is Ret1, N is Ret2.
