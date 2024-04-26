class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}      # vogais do alafabeto
        count = 0                               # contador inicial

        # passando por todas as letras da palavra dada
        for i in range(len(word)):

            substring_vowels = set()        # definindo o conjunto(set) de subvogais encontradas na palavra 

            for j in range(i, len(word)):   # analisando a subpalavra com inicio na letra em 'i'
                if word[j] in vowels:       # verifica se a letra é uma vogal

                    substring_vowels.add(word[j])       # adiciona a letra nas subvogais

                    if len(substring_vowels) == len(vowels):    # verifica se a quantidade é a mesma das vogais
                        count += 1
                else:
                    break

        return count

def main():         # função principal
    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: word = 'aeiouu'")
    n = 'aeiouu'
    print("Output: ", s.countVowelSubstrings(n))
    print("Expected: 2")

    # case 2
    print("Case 2")
    print("Input: word = 'unicornarihan'")
    n = 'unicornarihan'
    print("Output: ", s.countVowelSubstrings(n))
    print("Expected: 0")

    # case 3
    print("Case 3")
    print("Input: word = 'cuaieuouac'")
    n = 'cuaieuouac'
    print("Output: ", s.countVowelSubstrings(n))
    print("Expected: 7")

if __name__ == "__main__":
    main()
