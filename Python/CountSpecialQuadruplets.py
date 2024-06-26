class Solution:
    def countQuadruplets(self, nums) -> int:

        cont = 0            # contador da quantidade de combinações que dão certo
        n = len(nums)       # quantidade de elmentos

        # Percorre cada conjunto possível de quatro índices
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            cont += 1

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
    