using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static List<ulong> Encrypt((ulong, ulong) pk, string plaintext)
    {
        var (key, n) = pk;
        return plaintext.Select(c => (ulong)Math.Pow(c, key) % n).ToList();
    }

    static void Main()
    {
        var publicKey = (65537UL, 3233UL); // Exemplo de chave pública
        var plaintext = "Hello, RSA!";
        var encryptedMsg = Encrypt(publicKey, plaintext);
        Console.WriteLine("Mensagem Criptografada: " + string.Join(", ", encryptedMsg));
    }
}
