male(dhasrat).
male(ram).
male(laxman).
male(bharat).
male(shatrugan).
female(sita).
female(kaushalya).
parent(dhasrat, ram).
parent(dhasrat, laxman).
parent(dhasrat, bharat).
parent(dhasrat, shatrugan).
parent(kaushalya, ram).
parent(kaushalya, laxman).
parent(kaushalya, bharat).
parent(kaushalya, shatrugan).
wife(kaushalya, dhasrat).
wife(sita, ram).
husband(ram, sita).
father(X, Y) :-parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
brother(X, Y) :- parent(Z, X), parent(Z, Y).
father_in_law(X, Y) :- father(X, Z), wife(Y, Z).
mother_in_law(X, Y) :- mother(X, Z), wife(Y, Z).
brother_in_law(X, Y) :- wife(Y, H), brother(X, H).