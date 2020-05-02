%% Sarah Simon Luz
%% Ana Ferro

%"O problema em si
%consistem em colocar um determinado número n maior ou igual a 2, de rainhas em um
%tabuleiro de xadrez de forma que elas não se ataquem simultaneamente,"

%para a resolução doproblema de colocar “n” rainhas num tabuleiro de “n x n” dimensões.
%O programa tem como parâmetro o número de rainhas e tem como output as coordenadas
%em que cada rainha foi colocada.Para um número “n” menor do que 20 deverá também ter 
%como output o tabuleiro com as rainhas colocadas.

main:-
	[hill_climbing_SC],
	write('		PROBLEMA DAS N RAINHAS'),nl
	write('Introduza o número de rainhas (entre 4 e 20):'),nl,
	read(X),nl,
	dimensao(X, N),
	tabuleiro(N, T),
	estado_inicial(T),
	pesquisa_local_hill_climbingSemCiclos(T, []).


dimensao(X, N):- N = X.

tabuleiro(_,[]).
tabuleiro(N, L):- 
	criar_linhas(N, N, L).

criar_linhas(0,_,[]):- !.
criar_linhas(NL, NC, [H|T]):-
	Linha is NL - 1,
	init_linhas(NC, H),
	criar_linhas(Linha, NC, T).

%nao esta acabada
init_linhas(0, []) :- !.
init_linhas(NC, [(|T]) :-
	Coluna is NC - 1,
	init_rows(Coluna, H).


estado_inicial([]).