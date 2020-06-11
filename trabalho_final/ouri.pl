%% Sarah Simon Luz
%% Ana Ferro

%estado_inicial(fila do computador, fila do jogador, jogador atual)
estado_inicial(fila([4,4,4,4,4,4],0,c), fila([4,4,4,4,4,4],0,j)).

terminal(E):-
	empate(E),
	contagem_sementes(E).

%D1 - depósito do computador
%D2 - deposito do jogador
empate(fila(_,D1,_), fila(_,D2,_)):-
	D1 == 24,
	D2 == 24,
	asserta(empate).

contagem_sementes(fila(_,D1,_), fila(_,D2,_)):-
	D1 < 25,
	D2 < 25,
	fail.

contagem_sementes(fila(_,D1,_),_):-
	D1 >= 25,
	asserta(vencedor(c)), !.

contagem_sementes(_, fila(_,D2,_)):-
	D2 >=25,
	asserta(vencedor(j)), !.

oper(Eact, J, Buraco , Eseg):-
	member(Buraco, [1,2,3,4,5,6]),
	(sem_sementes(Eact, J)
		-> introduzir_sementes()
		; jogada_normal()
	),
	capturar().

sem_sementes((fila(B1,_,J1),fila(B2,_,J2)),J):-
	(J != J1
		-> zero(B1)
		; zero(B2)
	).

jogada_normal((fila(B1,_,J1), fila(B2,_,J2)), J, Buraco):-
	(J == J1
		-> nth0(Buraco,B1,Sementes)
		; nth0(Buraco,B2, Sementes)
	),
	jogada_normal()

zero([]).
zero([0|T]):- zero(T);
