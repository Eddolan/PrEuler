euler2 = sum [ x | x <- takeWhile (<= 4000000) fibs, even x]
  where
    fibs = 1 : 1 : zipWith (+) fibs (tail fibs)