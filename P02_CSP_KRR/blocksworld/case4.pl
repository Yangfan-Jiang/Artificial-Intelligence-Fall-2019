:- use_module(rbfs1, [bestfirst1/2]).
:- use_module(rbfs2, [bestfirst2/2]).



:- op( 300, xfy, ->).

s(Goals->NextAction,NewGoals->Action,1):-
 member(Goal,Goals),
 achieves(Action,Goal),
 can(Action,Condition),
 preserves(Action,Goals),
 regress(Goals,Action,NewGoals).

goal1(Goals->Action):-
 mid(State),
 satisfied(State,Goals).

goal2(Goals->Action):-
 start(State),
 satisfied(State,Goals).

h1(Goals->Action,H):-
 mid(State),
 delete_all(Goals,State,Unsatisfied),
 length(Unsatisfied,H).

h2(Goals->Action,H):-
 start(State),
 delete_all(Goals,State,Unsatisfied),
 length(Unsatisfied,H).

%supporting predicates, taken from 17.8
satisfied( State, Goals)  :-
  delete_all( Goals, State, []).              % All Goals in State

select( State, Goals, Goal)  :-               % Select Goal from Goals
  member( Goal, Goals).                       % A simple selection principle

achieves( Action, Goal)  :-
  adds( Action, Goals),
  member( Goal, Goals).

preserves( Action, Goals)  :-                 % Action does not destroy Goals
  deletes( Action, Relations),
  not((member( Goal, Relations),
       member( Goal, Goals))) .



regress( Goals, Action, RegressedGoals)  :-       % Regress Goals through Action
  adds( Action, NewRelations),
  delete_all( Goals, NewRelations, RestGoals),
  can( Action, Condition),
  addnew( Condition, RestGoals, RegressedGoals).  % Add precond., check imposs.

% addnew( NewGoals, OldGoals, AllGoals):
%   OldGoals is the union of NewGoals and OldGoals
%   NewGoals and OldGoals must be compatible

addnew( [], L, L).

addnew( [Goal | _], Goals, _)  :-
  impossible( Goal, Goals),         % Goal incompatible with Goals
  !, 
  fail.                             % Cannot be added

addnew( [X | L1], L2, L3)  :-
  member( X, L2),  !,               % Ignore duplicate
  addnew( L1, L2, L3).

addnew( [X | L1], L2, [X | L3])  :-
  addnew( L1, L2, L3).

% delete_all( L1, L2, Diff): Diff is set-difference of lists L1 and L2

delete_all( [], _, []).

delete_all( [X | L1], L2, Diff)  :-
  member( X, L2), !,
  delete_all( L1, L2, Diff).

delete_all( [X | L1], L2, [X | Diff])  :-
  delete_all( L1, L2, Diff).

%conc concatenates L1, L2 into L3
conc([],L,L).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).

%Impossibles for the blocks world
impossible(on(X,X),_).
impossible(on(X,Y),Goals):-
 member(clear(Y),Goals)
 ;
 member(on(X,Y1),Goals), Y\==Y1
 ;
 member(on(X1,Y),Goals),X1\==X.
impossible(clear(X),Goals):-
 member(on(_,X),Goals).

% Definition of action move( Block, From, To) in blocks world

% can( Action, Condition): Action possible if Condition true

can( move( Block, From, To), [ clear( Block), clear( To), on( Block, From)] ) :-
  is_block( Block),      % Block to be moved
  object( To),           % "To" is a block or a place
  To \== Block,          % Block cannot bå moved to itself
  object( From),         % "From" is a block or a place
  From \== To,           % Move to new position
  Block \== From.        % Block not moved from itself

% adds( Action, Relationships): Action establishes Relationships

adds( move(X,From,To), [ on(X,To), clear(From)]).

% deletes( Action, Relationships): Action destroys Relationships

deletes( move(X,From,To), [ on(X,From), clear(To)]).

object( X)  :-           % X is an objects if
  place( X)              % X is a place
  ;                      % or
  is_block( X).          % X is a block

print([]).
print([X|L1]):-write(X),nl,print(L1).




% project case 4
place(1).
place(2).
place(3).
place(4).
place(5).
place(6).
is_block(b1).
is_block(b2).
is_block(b3).
is_block(b4).
is_block(b5).
is_block(b6).
start([clear(2),clear(4),clear(6),clear(b1),clear(b6),clear(b4),on(b1,1),on(b3,3),on(b2,b3),on(b6,b2),on(b5,5),on(b4,b5)]).

mid([clear(b1),clear(b2),clear(b3),clear(b4),clear(b5),clear(b6),on(b1,1),on(b6,2),on(b3,3),on(b2,4),on(b5,5),on(b4,6)]).

end([on(b5,1),on(b3,b5),on(b1,b3),on(b4,b1),on(b2,b4),on(b6,b2),clear(b6)]).


solution(Plan):- end(S1),mid(S2),bestfirst1(S1->stop,Plan1),bestfirst2(S2->next,Plan2),delete_all(Plan2,[S2->next],Plan3),conc(Plan3,Plan1,Plan),print(Plan).