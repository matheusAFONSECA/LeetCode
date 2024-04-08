class Solution:
    def lengthOfLIS(self, nums) -> int:
        
        max_length = 1  # Comprimento máximo da sequência crescente
        current_length = 1  # Comprimento atual da sequência crescente
        
        # Percorre os elementos da lista, começando do segundo elemento
        for i in range(1, len(nums)):
            # Se o elemento atual for maior que o elemento anterior, a sequência continua
            if nums[i] > nums[i - 1]:
                current_length += 1
                # Atualiza o comprimento máximo, se necessário
                max_length = max(max_length, current_length)
            else:
                # Se não, reinicia o comprimento atual da sequência
                current_length = 1
        
        return max_length
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [10,9,2,5,3,7,101,18]")
    n = [10,9,2,5,3,7,101,18]
    print("Output: ", s.lengthOfLIS(n))
    print("Expected: 4")

    # case 2
    print("Case 2")
    print("Input: nums = [0,1,0,3,2,3]")
    n = [0,1,0,3,2,3]
    print("Output: ", s.lengthOfLIS(n))
    print("Expected: 4")

    # case 3
    print("Case 3")
    print("Input: nums = [7,7,7,7,7,7,7]")
    n = [7,7,7,7,7,7,7]
    print("Output: ", s.lengthOfLIS(n))
    print("Expected: 3")


if __name__ == "__main__":
    main()