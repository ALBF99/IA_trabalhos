pesquisa_local_hill_climbing(E) :- 
	estado_final(E).

pesquisa_local_hill_climbing(E) :- 
	expande(E,Lseg),
    melhor_vizinho(Lseg,no(Es,_)),
    pesquisa_local_hill_climbing(Es).

expande(E, L):- 
	length(E, N),
	findall(no(En, Heur),
                (oper(N,E,En), heur(En, Heur)),
                L).

melhor_vizinho([no(E,H)], no(E,H)).
melhor_vizinho([no(E,H)|T], V) :-
	melhor_vizinho(T, no(ET, HeurT)),
	(H < HeurT, V = no(E,H) ; V = no(ET,HeurT)).
