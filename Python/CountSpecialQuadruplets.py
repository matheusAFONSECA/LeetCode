class Solution:
    def countQuadruplets(self, nums) -> int:

        # soma dos elmentos
        soma = int(0)

        # contador das combinações
        cont = int(0)

        # Percorre os elementos da lista, começando do segundo elemento e indo até o ante-penultimo
        for i in range(1, len(nums)-2):
            # Se o elemento atual for maior que o elemento anterior, a sequência continua
            if nums[i] > nums[i - 1]:
                # Se o elemento atual for menor que o proximo elemento, a sequência continua
                if nums[i] < nums[i + 1]:
                    soma = nums[i - 1] + nums[i] + nums[i + 1]
                    
                    if soma == nums[i + 2]:
                         cont = cont + 1

        return cont

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [1,2,3,6]")
    n = [1,2,3,6]
    print("Output: ", s.countQuadruplets(n))
    print("Expected: 1")

    # case 2
    print("Case 2")
    print("Input: nums = [3,3,6,4,5]")
    n = [3,3,6,4,5]
    print("Output: ", s.countQuadruplets(n))
    print("Expected: 0")

    # case 3
    print("Case 3")
    print("Input: nums = [1,1,1,3,5]")
    n = [1,1,1,3,5]
    print("Output: ", s.countQuadruplets(n))
    print("Expected: 4")

if __name__ == "__main__":
    main()
    