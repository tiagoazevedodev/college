isPrime :: Int -> Bool
isPrime n = n > 1 && all (\d -> n `mod` d /= 0) [2..n-1]

main = do
    putStrLn "Digite um número inteiro positivo:"
    n <- readLn
    if isPrime n
        then putStrLn (show n ++ " é primo.")
        else putStrLn (show n ++ " não é primo.")
