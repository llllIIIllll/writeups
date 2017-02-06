-module(robot).
-export([main/1]).
-define(MAP, [
['#','#','#','#','#','#','#','#','#','#','#','#'],
['#','.','.','.','.','.','#','#','.','.','#','#'],
['#','#','.','.','.','#','#','.','.','.','.','#'],
['#','.','.','#','.','.','#','.','.','.','#','#'],
['#','#','.','.','.','.','.','.','.','.','.','#'],
['#','.','.','.','#','.','.','.','#','.','.','#'],
['#','.','.','.','.','.','#','.','.','.','.','#'],
['#','#','#','.','.','.','#','.','.','#','.','#'],
['#','.','.','.','#','.','.','.','.','#','.','#'],
['#','.','#','.','.','.','.','#','.','.','.','#'],
['#','#','#','.','.','#','.','.','#','.','.','#'],
['#','#','#','#','#','#','#','#','#','#','#','#']]).
-define(FLAG, <<97,81,91,92,93,88,123,96,116,77,115,68,85,101,4,90,88,109,83,52,106,124>>).



get_move(l) ->
    fun(X, Y) -> {X - 1, Y} end;

get_move(u) ->
    fun(X, Y) -> {X, Y - 1} end;

get_move(d) ->
    fun(X, Y) -> {X, Y + 1} end;

get_move(r) ->
    fun(X, Y) -> {X + 1, Y} end.

get_cell(Map, X, Y) ->
    lists:nth(X, lists:nth(Y, Map)).

check_X_Y(Map, X, Y) ->
    (X > 1) and (Y > 1) and (X < length(Map)) and (Y < length(Map)).

check_cell('.') -> true;
check_cell(_) -> false.

get_check(Sides) ->
    And = fun(X, Y) -> X and Y end,
    GetOneCheck = fun(X) -> get_one_check(X) end,
    Checks = lists:map(GetOneCheck, Sides),
    fun(Map, X, Y) -> 
        lists:foldl(And, true, lists:map(fun(F) -> F(Map, X, Y) end, Checks))
    end.

get_one_check(Side) ->
    fun(Map, X, Y) -> check_cell(move_to_cell(Map, X, Y, get_move(Side))) end.

move_to_cell(Map, X, Y, Move) ->
    {NewX, NewY} = Move(X, Y),
    case check_X_Y(Map, NewX, NewY) of
        true ->
            get_cell(Map, NewX, NewY);
        false ->
            '#'
    end.

go_go(Map, X, Y, Move, CheckDirections) ->
    case CheckDirections(Map, X, Y) of
        true ->
            {NewX, NewY} = Move(X, Y),
            go_go(Map, NewX, NewY, Move, CheckDirections);
        false ->
            {X, Y}
    end.

go_while_can(Map, X, Y, To, Sides) ->
    CheckDirections = get_check(Sides),
    Move = get_move(To),
    go_go(Map, X, Y, Move, CheckDirections).

execute_program(_Map, X, Y, []) -> {X, Y};
execute_program(Map, X, Y, [Instruction|RestProgram]) ->
    {To, Sides} = Instruction,
    {NewX, NewY} = go_while_can(Map, X, Y, To, Sides),
    execute_program(Map, NewX, NewY, RestProgram).

go_from_cell(Map, X, Y, RobotProgram) ->
    {NewX, NewY} = execute_program(Map, X, Y, RobotProgram),
    Cell = get_cell(Map, X, Y),
    (NewX == X) and (NewY == Y) and (Cell /= '#').
    
%true if alive, false if die
launch_robot_from_cell(X, Y) ->
    Map = ?MAP,
    RobotProgram = [
        {r, [r,u]},
        {d, [d]},
        {l, [l]},
        {u, [u,r]},
        {u, [u,l]}],
    go_from_cell(Map, X, Y, RobotProgram).

to_pairs(L) when length(L) =< 1 -> [];
to_pairs([A,B|L]) ->
    [ {A,B}|to_pairs(L) ].

str_lst_to_int_lst([]) -> [];
str_lst_to_int_lst([Elem|Rest]) ->
    {Ret,Rst} = string:to_integer(Elem),
    if
        Ret == error -> [];
        (Ret /= error) and (Rst == []) -> 
            [Ret] ++ str_lst_to_int_lst(Rest)
    end.

csv_to_int_pairs(Str) ->
    Lst = string:tokens(Str, ","),
    IntLst = str_lst_to_int_lst(Lst),
    to_pairs(IntLst).

remove_duplicates([]) -> [];
remove_duplicates(L) ->
    sets:to_list(sets:from_list(L)).

check_key(Str) ->
    Flag = binary_to_list(?FLAG),
    Coords = remove_duplicates(csv_to_int_pairs(Str)),
    case length(Coords) == (length(Flag)/2) of
        true ->
            And = fun(X, Y) -> X and Y end,
            Launch = fun({X,Y}) -> launch_robot_from_cell(X, Y) end,
            lists:foldl(And, true, lists:map(Launch, Coords));
        false -> false
    end.


decode_flag(Key) ->
    Coords = csv_to_int_pairs(Key),
    GrowingY = fun({A1,B1},{A2,B2}) -> (B1 < B2) or ((B1 == B2) and (A1 =< A2)) end,
    SortedCoords = lists:sort(GrowingY, Coords),
    FlatCoords = lists:flatten([tuple_to_list(X) || X <- SortedCoords]),
    StrCoords = [integer_to_list(X) || X <- FlatCoords],

    Xor = fun(A, B) -> A bxor B end,
    Flag = binary_to_list(?FLAG),
    Gamma = [lists:foldl(Xor, 0, Ci) || Ci <- StrCoords],
    lists:zipwith(Xor, Flag, Gamma).

scan_key() ->
    {Ret, [Key|_Rest]} = io:fread("Enter the key: ", "~s"),
    case Ret of
        error -> "";
        ok -> Key
    end.

main(_) ->
    Key = scan_key(),
    Answer = check_key(Key),
    case Answer of
        true ->
            Flag = decode_flag(Key),
            io:format("~s~n", [Flag]);
        false ->
            io:format("Invalid key!~n")
    end.
