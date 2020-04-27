%% Sarah Simon Luz
%% Ana Ferro

%estado_inicial(Lista de tuplos)
%Tuplo composto por uma posição,p(X,Y), e a jogada para essa posição
%Jogada simbolizada por:
%	x -> jogador x
%	o -> jogador o (computador)
%   v -> espaço	vazio
estado_inicial([(p(1,1),o), (p(1,2),v), (p(1,3),v), (p(1,4),v), (p(1,5),v),
				(p(2,1),x), (p(2,2),o), (p(2,3),x), (p(2,4),v), (p(2,5),v),
				(p(3,1),x), (p(3,2),o), (p(3,3),x), (p(3,4),o), (p(3,5),x),
				(p(4,1),o), (p(4,2),x), (p(4,3),o), (p(4,4),o), (p(4,5),x)]).

terminal(E):-
	linhas(E); 
	colunas(E); 
	diagonais(E);
	empate(E).

linhas(E):-
	(findall(J1,member((p(1,_),J1),E),L1),tres_seguidos(L1,0,0));
	(findall(J2,member((p(2,_),J2),E),L2),tres_seguidos(L2,0,0));
	(findall(J3,member((p(3,_),J3),E),L3),tres_seguidos(L3,0,0));
	(findall(J4,member((p(4,_),J4),E),L4),tres_seguidos(L4,0,0)).

colunas(E):-
	(findall(J1,member((p(_,1),J1),E),L1),tres_seguidos(L1,0,0));
	(findall(J2,member((p(_,2),J2),E),L2),tres_seguidos(L2,0,0));
	(findall(J3,member((p(_,3),J3),E),L3),tres_seguidos(L3,0,0));
	(findall(J4,member((p(_,4),J4),E),L4),tres_seguidos(L4,0,0));
	(findall(J5,member((p(_,5),J5),E),L5),tres_seguidos(L5,0,0)).	

diagonais(E):-
	(findall(J1,(member((p(X1,Y1),J1),E), (diagonal_dir_esq(1,3,3,LL1), member((X1,Y1),LL1))),L1),tres_seguidos(L1,0,0));
	(findall(J2,(member((p(X2,Y2),J2),E), (diagonal_dir_esq(1,4,4,LL2), member((X2,Y2),LL2))),L2),tres_seguidos(L2,0,0));
	(findall(J3,(member((p(X3,Y3),J3),E), (diagonal_dir_esq(1,5,4,LL3), member((X3,Y3),LL3))),L3),tres_seguidos(L3,0,0));
	(findall(J4,(member((p(X4,Y4),J4),E), (diagonal_dir_esq(2,5,4,LL4), member((X4,Y4),LL4))),L4),tres_seguidos(L4,0,0));
	(findall(J5,(member((p(X5,Y5),J5),E), (diagonal_esq_dir(2,1,4,LL5), member((X5,Y5),LL5))),L5),tres_seguidos(L5,0,0));
	(findall(J6,(member((p(X6,Y6),J6),E), (diagonal_esq_dir(1,1,4,LL6), member((X6,Y6),LL6))),L6),tres_seguidos(L6,0,0));
	(findall(J7,(member((p(X7,Y7),J7),E), (diagonal_esq_dir(1,2,4,LL7), member((X7,Y7),LL7))),L7),tres_seguidos(L7,0,0));
	(findall(J8,(member((p(X8,Y8),J8),E), (diagonal_esq_dir(1,3,3,LL8), member((X8,Y8),LL8))),L8),tres_seguidos(L8,0,0)).


diagonal_esq_dir(X,Y,Max,[(X,Y)|T]):-
	X<Max,
	X1 is X+1,
	Y1 is Y+1,
	diagonal_esq_dir(X1,Y1,Max,T).

diagonal_esq_dir(X,Y,Max,[(X,Y)]):-
	X = Max.

diagonal_dir_esq(X,Y,Max,[(X,Y)|T]):-
	X<Max,
	X1 is X+1,
	Y1 is Y-1,
	diagonal_dir_esq(X1,Y1,Max,T).

diagonal_dir_esq(X,Y,Max,[(X,Y)]):-
	X = Max.


%%tres_seguidos(Lista,NumX,NumO)
tres_seguidos([],NumX,NumO):-
	NumX < 3,
	NumO < 3,
	fail.

tres_seguidos([H|T],NumX,NumO):-
	(H = x
		-> NumX1 is NumX + 1,
		tres_seguidos(T,NumX1,NumO)
		;( H = o
			-> NumO1 is NumO + 1,
			tres_seguidos(T,NumX,NumO1)
			; tres_seguidos(T, NumX, NumO)
		)
	).

tres_seguidos(_,3,0):- asserta(vencedor(x)), !.
tres_seguidos(_,0,3):- asserta(vencedor(o)), !.

empate(E):-
	casas_preenchidas(E),
	asserta(empate).

casas_preenchidas([]).
casas_preenchidas([(p(_,_), X)|T]):-
	(X = v
		-> fail
		; casas_preenchidas(T)
	).

%função de utilidade:
%		-1 perde
%		0 empata
%		1 ganha
valor(E,-1):-
	(linhas(E); colunas(E); diagonais(E)),
	vencedor(o), !.

valor(E,0):-
	empate(E), !.

valor(E,1):- 
	(linhas(E); colunas(E); diagonais(E)),
	vencedor(x), !.

%oper(Eact,Jogador,Coluna,Eseg)
oper(Eact, J, Coluna , Eseg):-
	member(Coluna, [1,2,3,4,5]),
	casas_vagas(Coluna, Eact, Linha),
	insere(Coluna, Linha, J, Eact, Eseg).

casas_vagas(Coluna, Eact, Linha):-
	findall(X,(member((p(_,Coluna),v),Eact), X=v),L),
	length(L,V),
	V>0,
	Linha = V.

insere(Coluna, Linha, J, [H|T], [H|Ts]):-
	H = (p(X,Y),_),
	(dif(Linha,X); dif(Coluna,Y)),
	insere(Coluna, Linha, J,T,Ts).

insere(Coluna, Linha, J, [H|T], [Hs|T]):-
	H = (p(Linha, Coluna),v),
	Hs = (p(Linha, Coluna),J), !.
