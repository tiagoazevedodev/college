fahrenheitToCelsius :: Float -> Float
fahrenheitToCelsius f = (f - 32) * 5 / 9

main = do
    putStrLn "Digite a temperatura em Fahrenheit:"
    f <- readLn
    let c = fahrenheitToCelsius f
    putStrLn ("A temperatura em Celsius é: " ++ show c)
