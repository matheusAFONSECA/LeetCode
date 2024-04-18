class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        # Função auxiliar para contar subarrays com no máximo K números distintos
        def atMostKDistinct(nums, k):
            count = {}  # Dicionário para contar a frequência dos números
            res = 0     # Resultado: número de subarrays válidos
            i = 0       # Início da janela deslizante
            
            # Expandir a janela com a extremidade 'j'
            for j in range(len(nums)):
                # Se o número é novo na janela, reduzir k (número de tipos distintos permitidos restantes)
                if count.get(nums[j], 0) == 0:
                    k -= 1
                # Incrementar a contagem do número atual na janela
                count[nums[j]] = count.get(nums[j], 0) + 1

                # Enquanto tivermos mais tipos distintos do que o permitido, ajustar a janela a partir do início
                while k < 0:
                    count[nums[i]] -= 1  # Reduzir a contagem do número no início da janela
                    if count[nums[i]] == 0:  # Se a contagem chegar a zero, significa que um tipo distinto foi removido
                        k += 1
                    i += 1  # Mover o início da janela para a direita

                # Adicionar o número de subarrays que terminam em 'j' e têm no máximo 'k' tipos distintos
                res += j - i + 1
            return res

        # A diferença entre subarrays com no máximo k e no máximo k-1 números distintos
        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [1,2,1,2,3], k = 2")
    n = [1,2,1,2,3]
    k = 2
    print("Output: ", s.subarraysWithKDistinct(n, k))
    print("Expected: 7")

    # case 2
    print("Case 2")
    print("Input: nums = [1,2,1,3,4], k = 3")
    n = [1,2,1,3,4]
    k = 3
    print("Output: ", s.subarraysWithKDistinct(n, k))
    print("Expected: 3")


if __name__ == "__main__":
    main()
    