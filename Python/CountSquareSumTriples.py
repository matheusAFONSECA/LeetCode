class Solution:
    def countTriples(self, n: int) -> int:

        count = 0           # contador para quando as condições são satisfeitas

        for c in range(1, n + 1):
            c2 = pow(c, 2)          # elevando o elmento ao quadrado
            for a in range(1, c):
                a2 = pow(a, 2)      # elevando o elmento ao quadrado
                for b in range(a, c):   # começa de a para evitar duplicatas
                    b2 = pow(b, 2)      # elevando o elmento ao quadrado
                    if (a2 + b2) == c2:     # coodição atingida -> a² + b² = c²
                        count += 2 if a != b else 1  # conta duas vezes, a menos que a == b (neste caso, não é possível aqui pela condição)

        return count
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: n = 5")
    n = 5
    print("Output: ", s.countTriples(n))
    print("Expected: 2")

    # case 2
    print("Case 2")
    print("Input: n = 10")
    n = 10
    print("Output: ", s.countTriples(n))
    print("Expected: 4")


if __name__ == "__main__":
    main()
    