(* Project Euler 1 *)

fun e1_1 n = 
    case n of
	0 => 0
      | n  => if n mod 3 = 0 orelse n mod 5 = 0 then
		  n + e1_1(n-1)
	      else
		  e1_1(n-1);
e1_1 999;

fun e1_2 0 = 0
  | e1_2 n = if n mod 3 = 0 orelse n mod 5 = 0 then
		 n + e1_2(n-1)
	     else
		 e1_2(n-1);
e1_2 999
