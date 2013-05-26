-- Project Euler 1

-- fkn
e1 n = sum [ x | x <- [1..n], x `mod` 5 == 0 || x `mod` 3 == 0]
-- hard coded
e1_999 = sum [ x | x <- [1..999], mod x 5 == 0 || mod x 3 == 0]
