%% Sarah Simon Luz
%% Ana Ferro

%representacao dos nos
%no(Estado,Operador,Heuristica)

pesquisa_local_hill_climbingSemCiclos(E, _) :- 
	estado_final(E).

pesquisa_local_hill_climbingSemCiclos(E, L) :- 
	expande(E,LSeg),
	sort(2, @=<, LSeg, LOrd),
	obtem_no(LOrd, no(ES, _)),
	\+ member(ES, L),
	(pesquisa_local_hill_climbingSemCiclos(ES,[E|L]) ; fail).

expande(E, L):- 
	length(E, N),
	findall(no(En, Heur),
                (oper(N,E,En), heur(En, Heur)),
                L).

obtem_no([H|_], H).
obtem_no([_|T], H1) :-
	obtem_no(T, H1).
