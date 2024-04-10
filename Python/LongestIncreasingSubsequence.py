class Solution:
    def lengthOfLIS(self, nums) -> int:
        
        dp = [1] * len(nums)  # Inicializa uma lista de comprimento igual a `nums` com todos os elementos como 1
        
        # Percorre os elementos da lista
        for i in range(len(nums)):
            # Verifica os elementos anteriores a `i`
            for j in range(i):
                # Se `nums[i]` for maior que `nums[j]`, atualiza o comprimento da subsequência na posição `i`
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Retorna o comprimento máximo da subsequência
        return max(dp)
    

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
    print("Expected: 1")


if __name__ == "__main__":
    main()