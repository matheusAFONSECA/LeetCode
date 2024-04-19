class Solution:
    def countVowelSubstrings(self, word: str) -> int:


        return 0
    

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
    