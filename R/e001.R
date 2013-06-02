# Project Euler 1

e1 <- c(1:999);
e1[e1%%3 != 0 & e1%%5 != 0] = 0
sum(e1)
