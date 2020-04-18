%% Sarah Simon Luz
%% Ana Ferro

%estado_inicial(Lista, jogador)
%Lista- Lista que contém as posições do tabuleiro 4x5
%jogador:
%	x -> jogador x
%	o -> jogador o (computador)
%   b -> espaço	em branco
estado_inicial([(p(1,1),_), (p(1,2),_), (p(1,3),_), (p(1,4),_), (p(1,5),_),
				(p(2,1),_), (p(2,2),_), (p(2,3),_), (p(2,4),_), (p(2,5),_),
				(p(3,1),_), (p(3,2),_), (p(3,3),_), (p(3,4),_), (p(3,5),_),
				(p(4,1),_), (p(4,2),_), (p(4,3),_), (p(4,4),_), (p(4,5),_)],_).

terminal((E,_)):-linhas(E); colunas(E); 
			  diagonais(E);empate(E).

linhas(E):-
	(findall(X1,(member(X1,E), X1=(p(1,_),_)),L1)),tres_seguidos();
	(findall(X2,(member(X2,E), X2=(p(2,_),_)),L2)),tres_seguidos();
	(findall(X3,(member(X3,E), X3=(p(3,_),_)),L3)),tres_seguidos();
	(findall(X4,(member(X4,E), X4=(p(4,_),_)),L4)),tres_seguidos().

colunas(E):-
	(findall(X1,(member(X1,E), X1=(p(_,1),_)),L1)),tres_seguidos();
	(findall(X2,(member(X2,E), X2=(p(_,2),_)),L2)),tres_seguidos();
	(findall(X3,(member(X3,E), X3=(p(_,3),_)),L3)),tres_seguidos();
	(findall(X4,(member(X4,E), X4=(p(_,4),_)),L4)),tres_seguidos();
	(findall(X5,(member(X5,E), X5=(p(_,5),_)),L5)),tres_seguidos().


diagonais(E):-
	(findall(X1,(member(X1,E), X1=(p(X,X),_)),L4)),tres_seguidos().

empate([]).
empate([p(_,_),J|T]):-
	%(J = x; J = o),
	atom(J),
	empate(T).

tres_seguidos():- retracta
tres_seguidos():-.

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

troca_jogador(O,P):-
	(O = x
		-> P = o 
		; P = x
	).

%oper(Eact,Jogada,Eseg)
oper((Eact,Jact), coluna1 , (Eseg,Jseg)):-
	troca_jogador(Jact,Jseg),
	insere(1, Jseg, Eact, Eseg).

oper((Eact,Jact), coluna2 , (Eseg,Jseg)):-
	troca_jogador(Jact,Jseg),
	insere(2, Jseg, Eact, Eseg).

oper((Eact,Jact), coluna3 , (Eseg,Jseg)):-
	troca_jogador(Jact,Jseg),
	insere(3, Jseg, Eact, Eseg).

oper((Eact,Jact), coluna4 , (Eseg,Jseg)):-
	troca_jogador(Jact,Jseg),
	insere(4, Jseg, Eact, Eseg).

oper((Eact,Jact), coluna5 , (Eseg,Jseg)):-
	troca_jogador(Jact,Jseg),
	insere(5, Jseg, Eact, Eseg).


insere().

casas_vagas().
