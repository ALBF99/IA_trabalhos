%% Sarah Simon Luz
%% Ana Ferro

%estado_inicial(Lista, jogador)
%Lista- Lista que contém as posições do tabuleiro 4x5
%jogador:
%	x -> jogador x
%	o -> jogador o (computador)
%   b -> espaço	em branco
estado_inicial(([(p(1,1),_), (p(1,2),_), (p(1,3),_), (p(1,4),_), (p(1,5),_),
				(p(2,1),_), (p(2,2),_), (p(2,3),_), (p(2,4),_), (p(2,5),_),
				(p(3,1),_), (p(3,2),_), (p(3,3),_), (p(3,4),_), (p(3,5),_),
				(p(4,1),_), (p(4,2),_), (p(4,3),_), (p(4,4),_), (p(4,5),_)],_)).

terminal((E,_)):-
	linhas(E); 
	colunas(E); 
	diagonais(E);
	empate(E).

linhas(E):-
	(findall(X1,member((p(_,1),X1),E),L1),tres_seguidos(L1,0,0));
	(findall(X2,member((p(_,2),X2),E),L2),tres_seguidos(L2,0,0));
	(findall(X3,member((p(_,3),X3),E),L3),tres_seguidos(L3,0,0));
	(findall(X4,member((p(_,4),X4),E),L4),tres_seguidos(L4,0,0)).

colunas(E):-
	(findall(X1,member((p(1,_),X1),E),L1),tres_seguidos(L1,0,0));
	(findall(X2,member((p(2,_),X2),E),L2),tres_seguidos(L2,0,0));
	(findall(X3,member((p(3,_),X3),E),L3),tres_seguidos(L3,0,0));
	(findall(X4,member((p(4,_),X4),E),L4),tres_seguidos(L4,0,0));
	(findall(X5,member((p(5,_),X5),E),L5),tres_seguidos(L5,0,0)).	

diagonais(E):-
	(findall(X1,(member((p(X,Y),X1),E), X is X+1, Y is Y-1),L1),tres_seguidos(L1,0,0));
	(findall(X2,(member((p(X,Y),X2),E), X is X+1, Y is Y+1),L2),tres_seguidos(L2,0,0)).

%%tres_seguidos(Lista,NumX,NumO)
tres_seguidos([],NumX,NumO):-
	NumX < 3,
	NumO < 3,
	fail.

tres_seguidos([x|T],NumX,NumO):-
	NumX is NumX + 1,
	tres_seguidos(T,NumX,NumO).

tres_seguidos([o|T],NumX,NumO):-
	NumO is NumO + 1,
	tres_seguidos(T,NumX,NumO).

tres_seguidos(_,3,0):- asserta(vencedor(x)), !.
tres_seguidos(_,0,3):- asserta(vencedor(o)), !.

empate([]).
empate([p(_,_),J|T]):-
	(J = x; J = o),
	empate(T).

%função de utilidade:
%		-1 perde
%		0 empata
%		1 ganha
valor((Eact,_),-1):-
	(linhas(Eact); colunas(Eact); diagonais(Eact)),
	vencedor(o), !.

valor((Eact,_),0):-
	empate(Eact), !.

valor((Eact,_),1):- 
	(linhas(Eact); colunas(Eact); diagonais(Eact)),
	vencedor(x), !.

%oper(Eact,Coluna,Eseg)
oper((Eact,_), Jact, Coluna , (Eseg,Jseg)):-
	member(Coluna, [1,2,3,4,5]),
	troca_jogador(Jact,Jseg),
	casas_vagas(Coluna, Eact, Linha),
	insere(Coluna, Linha, Jseg, Eact, Eseg).

troca_jogador(O,P):-
	(O = x
		-> P = o 
		; P = x
	).

casas_vagas(Coluna, Eact, Linha):-
	findall(X,(member((p(Coluna,_),b),Eact), X=b),L),
	length(L,V),
	V>0,
	(V = 1
		-> Linha = 4
		;(V = 2
			-> Linha = 3
			;(V = 3
				-> Linha = 2
				; Linha = 1
			)
		)
	).

insere(Coluna, Linha, Jseg, [H|T], [H|Ts]):-
	H = (p(X,Y),_),
	(dif(Coluna,X); dif(Linha,Y)),
	insere(Coluna, Linha, Jseg,T,Ts).

insere(Coluna, Linha, Jseg, [H|T], [Hs|T]):-
	H = (p(Coluna,Linha),b),
	Hs = (p(Coluna,Linha),Jseg), !.


