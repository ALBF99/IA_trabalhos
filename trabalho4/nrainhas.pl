%% Sarah Simon Luz
%% Ana Ferro


main:-
	[hill_climbing_SC],
	write('		PROBLEMA DAS N RAINHAS'),nl,
	write('Introduza o número de rainhas (entre 4 e 20):'),nl,
	read(X),nl,
	dimensao(X, N),
	random_rainhas(N,LR),
	tabuleiro(N,LT,LR),
	estado_inicial(LT).
	%pesquisa_local_hill_climbingSemCiclos(L, []).


dimensao(X, N):- N = X.

estado_inicial(L).

random_rainhas(N,LR):-
	random_rainhas(0,N,LR).

random_rainhas(Col, N, []):-
	Col = N, !.
random_rainhas(Col,N,[H|T]):-
	Col1 is Col + 1,
	random_between(1,N,Linha),
	H = (Linha, Col1),
	random_rainhas(Col1, N, T).


tabuleiro(Tam, L,LR):- 
	criar_linhas(0, Tam, L),
	flatten(L,L1),
	sort(1, @=<, LR, LROrd),
	LF = [],
	insere_rainhas(L1,LROrd,LF),
	print_tabuleiro(Tam,LF).

criar_linhas(NL, Tam, []):-
	NL = Tam, !.
criar_linhas(NL, Tam, [H|T]):-
	L1 is NL + 1, 
	init_linhas(1, L1, Tam, H),
	criar_linhas(L1, Tam, T).

init_linhas(NC, _, Tam, []):-
	NC > Tam, !.
init_linhas(NC, L, Tam, [(p(L,NC),_)|T]) :-
	C1 is NC + 1,
	init_linhas(C1, L, Tam, T).


insere_rainhas([H|T], [HR|TR], LF):-
	H = (p(L,C),_),
	HR = (X,Y),
	( (L==X , C ==Y)
		-> H1 = (p(L,C),r),
		append([H1],LF,LF1),
		insere_rainhas(T,TR,LF1)
		; append([H],LF,LF1),
		insere_rainhas(T,[HR|TR],LF1)
	).










insere(Coluna, Linha, J, [H|T], [H|Ts]):-
	H = (p(X,Y),_),
	(dif(Linha,X); dif(Coluna,Y)),
	insere(Coluna, Linha, J,T,Ts).

insere(Coluna, Linha, J, [H|T], [Hs|T]):-
	H = (p(Linha, Coluna),v),
	Hs = (p(Linha, Coluna),J), !.


print_tabuleiro([]).
print_tabuleiro(N,[(p(_,Y),J)|T]):-
	write(J), 
	write(' | '),
	(Y = N
		-> nl,
		print_tabuleiro(T)
		; print_tabuleiro(T)
	).

restricoes():-
	linhas(),
	diagonais().

linhas().

diagonais().

op():-.

%https://sites.icmc.usp.br/sandra/G6_t2/rainha.htm