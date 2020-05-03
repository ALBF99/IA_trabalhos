%% Sarah Simon Luz
%% Ana Ferro

%"O problema em si
%consistem em colocar um determinado número n maior ou igual a 2, de rainhas em um
%tabuleiro de xadrez de forma que elas não se ataquem simultaneamente,"

%Implemente em Prolog o algoritmo iterativo (baseado no “hill-climbing”)
%para a resolução doproblema de colocar “n” rainhas num 
%tabuleiro de “n x n” dimensões. O programa tem como parâmetro
%o número de rainhas e tem como output as coordenadas em que cada
%rainha foi colocada.Para um número “n” menor do que 20 deverá também
%ter como output o tabuleiro com as rainhascolocadas.Avalie a sua solução,
%apresentando o tempo que demora a execução do algoritmo para cada 
%“n”entre 4 e 20.  Caso use uma posição inicial aleatória, faça, 
%para cada “n”, a média de 10 execuçõesdo programa..


main:-
	[hill_climbing_SC],
	write('		PROBLEMA DAS N RAINHAS'),nl,
	write('Introduza o número de rainhas (entre 4 e 20):'),nl,
	read(X),nl,
	dimensao(X, N),
	tabuleiro(N, L),
	estado_inicial(L).
	%pesquisa_local_hill_climbingSemCiclos(L, []).


dimensao(X, N):- N = X.

tabuleiro(Tam, L):- 
	criar_linhas(0, Tam, L).

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

estado_inicial(L).


%LR-Lista de posiçoes random rainha
%LT-Lista tabuleiro que vai sendo atualizado com as posiçoes das rainhas
random_posicoes(_,Rep,_,_):-
	Rep =< 0, !.
random_posicoes(N, Rep, LR, LT):-
	random_between(1,N,X),
	random_between(1,N,Y),
		( member((X,Y),LR)
			->fail,
			random_posicoes(N, Rep, LR, LT)
			; insere_rainha(X,Y,LR, LR1),
			insere_tabuleiro(X, Y, LT, LT1),
			Rep1 is Rep-1,
			random_posicoes(N, Rep1, LR1, LT1)
		).

%lista auxiliar
%insere no inicio da lista, a ordem dos elementos nao importa
insere_rainha(X,Y,LR,[(X,Y)|LR]):- !.

insere_tabuleiro(X,Y,[H|T], [H|Ts]):-
	H = (p(Linha,Coluna),_),
	(dif(X,Linha); dif(Y,Coluna)),
	insere_tabuleiro(X,Y,T,Ts).


linhas().

colunas().

diagonais().

op().

%IMPORTANTE:
%Exemplos de rotinas em Prolog que trabalham com listas: 
%https://pt.wikibooks.org/wiki/Prolog/Exemplos
 