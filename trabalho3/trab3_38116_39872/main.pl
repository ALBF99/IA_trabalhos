%% Sarah Simon Luz
%% Ana Ferro

inicia_contador:-
	retractall(nos(_)),
	asserta(nos(0)),!.

contador_nos(X):-
	retract(nos(N)),
	N1 is X+N,
	asserta(nos(N1)),!.

main:- 
	write('\n 		MENU    	\n'),
	write('1 - Jogar 3 em linha (minimax)'),nl,
	write('2 - Jogar 3 em linha (alfabeta)'),nl,
	write('3 - Sair'),nl,
	write('Opção:'),nl,
	read(X),nl,
	menu_opcao(X).

menu_opcao(1):-
	[minimax],
	[treslinha],
	inicia_contador,
	estado_inicial(Ei),
	ciclo('min',x,Ei).

menu_opcao(2):-
	[alfabeta],
	[treslinha], 
	inicia_contador,
	estado_inicial(Ei),
	ciclo('alf',x,Ei).

menu_opcao(3).

tabuleiro([]).
tabuleiro([(p(_,Y),J)|T]):-
	write(J), 
	write(' | '),
	(Y = 5
		-> nl,
		tabuleiro(T)
		; tabuleiro(T)
	).

coluna(X, Op):- Op = X.
	
%%ciclo(Opcao,Jogador, Jogada)
%% Opcao: minimax ou alfabeta
%% Jogador: "o"-computador, "x"-jogador
%% Jogada: tuplo(Estado,Jogador)
ciclo(_,_,E):-
	(linhas(E);colunas(E);diagonais(E)),
	tabuleiro(E),nl,
	write('Vencedor: '),
	vencedor(J), 
	write(J), !.

ciclo(_,_,E):-
	empate(E),
	tabuleiro(E),nl,
	write('Empate'), !.

ciclo('min', o, E):-
	tabuleiro(E),nl,
	statistics(real_time,[Ti,_]),
	minimax_decidir(E,Op),
	statistics(real_time,[Tf,_]), T is Tf-Ti,
	write('Tempo: '),
	write(T), nl,
	write('Nós: '),
	nos(N),
	write(N),nl,
	write('Jogada computador: '),
	write(Op),nl,
	inicia_contador,
	oper(E,o,Op,Es),
	ciclo('min',x,Es).

ciclo('min',x,E):-
	tabuleiro(E),nl,
	write('Coluna:'),nl,
	read(X),nl,
	coluna(X,Op),
	oper(E, x, Op, Es),
	ciclo('min',o, Es).

ciclo('alf',o,E):-
	tabuleiro(E),nl,
	statistics(real_time,[Ti,_]),
	alfabeta(E,Op),
	statistics(real_time,[Tf,_]), T is Tf-Ti,
	write('Tempo: '),
	write(T), nl,
	write('Nós: '),
	nos(N),
	write(N),nl,
	write('Jogada computador:'),
	write(Op),nl,
	inicia_contador,
	oper(E,o,Op,Es),
	ciclo('alf',x,Es).

ciclo('alf',x,E):-
	tabuleiro(E),nl,
	write('Coluna:'),nl,
	read(X),nl,
	coluna(X,Op),
	oper(E, x, Op, Es),
	ciclo('alf',o, Es).
