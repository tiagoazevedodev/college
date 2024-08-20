% Prolog facts
bird(tweety).
fish(goldie).
worm(molie).
likes(bird, worm).
likes(cat, fish).
likes(cat, bird).
likes(friend, friend).
friend(silvester, me).
eats(silvester, X) :- likes(silvester, X).

% Queries
?- eats(silvester, X).