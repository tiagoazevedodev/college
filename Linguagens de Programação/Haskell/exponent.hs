main = do
    putStrLn "Digite o valor de x:"
    x <- readLn
    putStrLn "Digite o valor de n (não-negativo):"
    n <- readLn
    let result = x ^ n
    putStrLn ("O resultado de " ++ show x ++ "^" ++ show n ++ " é: " ++ show result)
