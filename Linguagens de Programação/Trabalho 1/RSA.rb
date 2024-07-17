def encrypt(pk, plaintext)
    key, n = pk
    plaintext.chars.map { |char| (char.ord ** key) % n }
end

public_key = [65537, 3233] # Exemplo de chave pública
plaintext = "Hello, RSA!"
encrypted_msg = encrypt(public_key, plaintext)
puts "Mensagem Criptografada: #{encrypted_msg}"






