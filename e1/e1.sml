(* euler 1 *)

fun length nil = 0
  | length (_::t) = 1 + length t
