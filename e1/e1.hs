e1 n = sum [ x | x <- [1..n], x `mod` 5 == 0 || x `mod` 3 == 0]
e1_1 = sum [ x | x <- [1..999], mod x 5 == 0 || mod x 3 == 0]
