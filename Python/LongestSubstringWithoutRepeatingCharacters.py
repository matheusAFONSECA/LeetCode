class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Inicializa um conjunto para armazenar os caracteres únicos
        char_set = set()
        # Variável para manter o comprimento máximo encontrado
        max_len = 0
        # Variável para marcar o início da janela atual
        start = 0
        
        # Itera sobre os caracteres da string
        for end in range(len(s)):
            # Se o caractere já está no conjunto, remove os caracteres da janela atual até que ele seja removido
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            # Adiciona o novo caractere ao conjunto e atualiza o comprimento máximo
            char_set.add(s[end])
            max_len = max(max_len, end - start + 1)
        
        # Retorna o comprimento máximo encontrado
        return max_len
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: s = 'abcabcbb'")
    n = "abcabcbb"
    print("Output: ", s.lengthOfLongestSubstring(n))
    print("Expected: 3")

    # case 2
    print("Case 2")
    print("Input: s = 'bbbbb'")
    n = "bbbbb"
    print("Output: ", s.lengthOfLongestSubstring(n))
    print("Expected: 1")

    # case 3
    print("Case 3")
    print("Input: s = 'pwwkew'")
    n = "pwwkew"
    print("Output: ", s.lengthOfLongestSubstring(n))
    print("Expected: 3")


if __name__ == "__main__":
    main()
    