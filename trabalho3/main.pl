%% Sarah Simon Luz
%% Ana Ferro

main:- 
	write('\n 		MENU    	\n'),
	write('1 - Jogar 3 em linha (minimax)'),nl,
	write('2 - Jogar 3 em linha (alfabeta)'),nl,
	write('3 - Sair'),nl,
	write('Opção:'),nl,
	read(X),
	menu_opcao(X).

menu_opcao(1):-
	[minimax],
	[treslinha],
	estado_inicial(Ei),
	ciclo('min','jog',Ei).

menu_opcao(2):-
	[alfabeta],
	[treslinha],
	estado_inicial(Ei),
	ciclo('alf','jog',Ei).

menu_opcao(3).

tabuleiro([]).
tabuleiro([(p(X,Y),J)|T]):-
	write(J), 
	write(' | '),
	X = 4 -> nl, tabuleiro(T); tabuleiro(T).

%%ciclo(Opcao,Jogador, Jogada)
%% Opcao: minimax ou alfabeta
%% Jogador: "comp"-computador, "jog"-jogador
%% Jogada: tuplo(Estado,Jogador)
ciclo('min','comp',(Eact,Jact)):-
	tabuleiro(Eact),
	minimax_decidir((Eact,Jact),Op),
	oper((Eact,Jact),Op,Es),
	ciclo('min','jog',Es).

ciclo('alf','comp',(Eact,Jact)):-
	tabuleiro(Eact),
	alfabeta((Eact,Jact),Op),
	oper((Eact,Jact),Op,Es),
	ciclo('alf','jog',Es).

ciclo('min','jog',(Eact,Jact)):-
	tabuleiro(Eact),nl,
	write('Coluna:''),nl,
	read(X),
	oper((Eact,Jact), X, Es),
	ciclo('min', 'comp', Es).

ciclo('alf','jog',(Eact,Jact)):-
	tabuleiro(Eact),nl,
	write('Coluna:''),nl,
	read(X),
	oper((Eact,Jact), X, Es),
	ciclo('alf', 'comp', Es).

ciclo(_,_,(Eact,Jact)):-
	(linhas(Eact);colunas(Eact);diagonais(Eact)),
	tabuleiro(Eact),
	write('Vencedor: '),
	write(Jact), !.

ciclo(_,_,(Eact,Jact)):-
	empate(Eact),
	tabuleiro(Eact),
	write('Empate'), !.
