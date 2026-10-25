% Prolog program to represent family relationships
% 1

% Facts
parent(ram, shyam).
parent(ram, geeta).
parent(shyam, amit).
parent(geeta, neha).

% Rules
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \== Y.

% Display messages
show :-
    write('Family relationship program'),
    nl.

% Query examples:
?- parent(ram, shyam).
?- grandparent(ram, amit).
?- sibling(shyam, geeta).
?- show.

% Additional family relationships
% 2

% Fact
male(dashrath).
male(ram).
male(laxman).

female(kausalya).
female(kaikeyi).
female(sita).

parent(dashrath, ram).
parent(kaikeyi, ram).
parent(kausalya, laxman).

husband(ram, sita).

% Rule
father(X,Y) :- male(X), parent(X,Y).

mother(X,Y) :- female(X), parent(X,Y).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.

grandfather(X,Y) :- male(X), parent(X,Z), parent(Z,Y).

grandmother(X,Y) :- female(X), parent(X,Z), parent(Z,Y).


% Query examples:
?- male(ram).
?- female(sita).
?- father(dashrath, ram).
?- mother(kausalya, laxman).
?- sibling(ram, ram).
?- sibling(X, Y).
?- grandfather(dashrath, laxman).
?- grandmother(kausalya, ram).
?- father(X, Y).
?- mother(X, Y).