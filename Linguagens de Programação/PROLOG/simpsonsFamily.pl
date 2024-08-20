% Relações familiares
pai(homer, bart).
mae(marge, bart).
pai(homer, lisa).
mae(marge, lisa).
pai(abe, homer).
mae(jackie, homer).
pai(clancy, marge).
mae(jacqueline, marge).
pai(maridoSelma, selma).
pai(maridoSelma, patty).

% Consultas
% a. Quem sao as mulheres da família?
mulher(X) :- pai(X, _); mae(X, _).
?- findall(X, mulher(X), Mulheres).

% b. Quem sao os tios e tias maternos do Bart?
tio_tia_materno(X, bart) :- mae(marge, bart), pai(X, marge); mae(X, marge), X \= marge.
?- findall(X, tio_tia_materno(X, bart), TioseTiasMaternos).

% c. Quem sao os tios e tias paternos do Bart?
tio_tia_paterno(X, bart) :- pai(homer, bart), pai(X, homer); mae(X, homer), X \= homer.
?- findall(X, tio_tia_paterno(X, bart), TioseTiasPaternos).

% d. Quem sao os tios e tias do Bart que se casaram com parentes seus (dos dois lados juntos, pai e mãe)?
tio_tia_casado_parente(X, bart) :-
    (tio_tia_materno(X, bart); tio_tia_paterno(X, bart)),
    pai(X, Y); mae(X, Y), pai(Y, bart); mae(Y, bart).
?- findall(X, tio_tia_casado_parente(X, bart), TioseTiasCasadosParentes).

% e. Quem sao os primos paternos do Bart?
primo_paterno(X, bart) :-
    pai(homer, bart),
    pai(Y, X),
    pai(homer, Y).
?- findall(X, primo_paterno(X, bart), PrimosPaternos).

% f. Quem sao os primos maternos do Bart?
primo_materno(X, bart) :-
    mae(marge, bart),
    pai(Y, X),
    mae(marge, Y).
?- findall(X, primo_materno(X, bart), PrimosMaternos).