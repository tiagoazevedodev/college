fn encrypt(pk: (u64, u64), plaintext: &str) -> Vec<u64> {
    let (key, n) = pk;
    plaintext.chars()
        .map(|c| (c as u64).pow(key) % n)
        .collect()
}

fn main() {
    let public_key = (65537, 3233); // Exemplo de chave pública
    let plaintext = "Hello, RSA!";
    let encrypted_msg = encrypt(public_key, plaintext);
    println!("Mensagem Criptografada: {:?}", encrypted_msg);
}


