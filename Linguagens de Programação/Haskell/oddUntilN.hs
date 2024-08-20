oddNumbers :: Int -> [Int]
oddNumbers n = take n [x | x <- [1,3..]]

main = do
    putStrLn "Digite um número inteiro positivo:"
    n <- readLn
    let result = oddNumbers n
    putStrLn ("Os primeiros " ++ show n ++ " números ímpares são: " ++ show result)
