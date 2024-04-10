class Solution:
    def increasingTriplet(self, nums) -> bool:

        first = second = float('inf')

        # Percorre os elementos da lista
        for num in nums:
            # Se o número for menor que o primeiro, atualiza o primeiro
            if num < first:
                first = num
            # Se o número estiver entre o primeiro e o segundo, atualiza o segundo
            elif first < num < second:
                second = num
            # Se o número for maior que o segundo, uma sequência foi encontrada
            elif num > second:
                return True

        return False

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [1,2,3,4,5]")
    n = [1,2,3,4,5]
    print("Output: ", s.increasingTriplet(n))
    print("Expected: True")

    # case 2
    print("Case 2")
    print("Input: nums = [5,4,3,2,1]")
    n = [5,4,3,2,1]
    print("Output: ", s.increasingTriplet(n))
    print("Expected: False")

    # case 3
    print("Case 3")
    print("Input: nums = [2,1,5,0,4,6]")
    n = [2,1,5,0,4,6]
    print("Output: ", s.increasingTriplet(n))
    print("Expected: True")

    # case 4
    print("Case 4")
    print("Input: nums = [20,100,10,12,5,13]")
    n = [20,100,10,12,5,13]
    print("Output: ", s.increasingTriplet(n))
    print("Expected: True")

if __name__ == "__main__":
    main()
    