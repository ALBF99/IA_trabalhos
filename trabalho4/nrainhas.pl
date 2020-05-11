%% Sarah Simon Luz
%% Ana Ferro

main:-
	[hill_climbing],
	write('		PROBLEMA DAS N RAINHAS'),nl,
	write('Introduza o número de rainhas (entre 4 e 20):'),nl,
	read(X),nl,
	dimensao(X, N),
	random_rainhas(N,LR),
	estado_inicial(LR),
	time(pesquisa_local_hill_climbing(LR)).

main_SC:-
	[hill_climbing_SC],
	write('		PROBLEMA DAS N RAINHAS'),nl,
	write('Introduza o número de rainhas (entre 4 e 20):'),nl,
	read(X),nl,
	dimensao(X, N),
	random_rainhas(N,LR),
	estado_inicial(LR),
	pesquisa_local_hill_climbingSemCiclos(LR,[]).

dimensao(X, N):- N = X.

estado_inicial(_).

random_rainhas(N,LR):-
	random_rainhas(0,N,LR).

random_rainhas(Col, N, []):-
	Col = N, !.
random_rainhas(Col,N,[H|T]):-
	Col1 is Col + 1,
	random_between(1,N,Linha),
	H = (Linha, Col1),
	random_rainhas(Col1, N, T).

oper(N, E, Es):-
	nova_linha(Ls,1,N),
	movimenta((L,C), (Ls,C), E, Es),
	dif(L,Ls).

nova_linha(_,Linf,Lsup):-
	Linf > Lsup,!,
	fail.

nova_linha(Ls,Ls,_).
nova_linha(Ls, Linf, Lsup):-
	Linf1 is Linf + 1,
	nova_linha(Ls, Linf1, Lsup).

movimenta(Rainha1, Rainha2, [Rainha1|T],[Rainha2|T]).
movimenta(Rainha1, Rainha2, [H|T1], [H|T2]):-
	movimenta(Rainha1, Rainha2, T1, T2).

%Conta o num de rainhas que atacam outras rainhas
heur(E, H):-
	ataques(E, H).

ataques(E,H):-
	contagem_ataques(E,E,0,H).

contagem_ataques([],_,N,N).

contagem_ataques([Rainha|T], E, NA, N):-
	ataca(Rainha, E, X),
	NA1 is NA+X,
	contagem_ataques(T, E, NA1, N).

ataca(Rainha, E, X):-
	(nao_ataca(Rainha, E)
		-> X = 0
		; X = 1
	).

nao_ataca(_,[]).
nao_ataca(Rainha, [Rainha|T]):-
	nao_ataca(Rainha, T).

nao_ataca((L,C), [(L1,C1)|T]):-
	L =\= L1,
	C =\= C1,
	Laux is L-L1,
	Laux =\= C-C1,
	Laux =\= C1-C,
	nao_ataca((L,C),T).

estado_final(E):-
	ataques(E,H),
	H == 0.

%https://sites.icmc.usp.br/sandra/G6_t2/rainha.htm
%http://wiki.di.uminho.pt/twiki/pub/Education/LC/0506/prolog93-100.pdf
%https://sites.icmc.usp.br/sandra/G6_t2/rainha.htm
%https://pt.wikibooks.org/wiki/Prolog/Exemplos
%http://www.cse.unsw.edu.au/~billw/prologdict.html


