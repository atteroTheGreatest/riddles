-module(ninety_nine).
-export([last/1, last_but_not_least/1, nth/2, len/1, reverse/1]).


last([]) -> nil;
last([H|Tail]) -> last(H, Tail).

last(D, []) -> D;
last(_, [H|Tail]) -> last(H, Tail).


last_but_not_least([H|[P|Tail]]) -> last_but_not_least(H,[P|Tail]);
last_but_not_least(_) -> nil.

last_but_not_least(_, [H|[P|Tail]]) -> last_but_not_least(H, [P|Tail]);
last_but_not_least(H, [_|_]) -> H.


nth([], _) -> nil;
nth([H|_], 1) -> H;
nth([_|T], N) -> nth(T, N-1).


len([]) -> 0;
len([_|T]) -> len(T, 1).

len([], N) -> N;
len([_|T], N) -> len(T, N+1).


reverse([]) -> [];
reverse(L) -> reverse(L, []).

reverse([], Acc) -> Acc;
reverse([H|T], Acc) -> reverse(T, [H|Acc]).

