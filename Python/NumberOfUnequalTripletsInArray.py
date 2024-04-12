class Solution:
    def unequalTriplets(self, nums) -> int:

        count = 0           # contador para quando as condições são satisfeitas
        n = len(nums)        # quantidade de elementos da array

        # nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k]

        # itere sobre todas as possíveis combinações
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1
                            
        return count
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [4,4,2,4,3]")
    n = [4,4,2,4,3]
    print("Output: ", s.unequalTriplets(n))
    print("Expected: 3")

    # case 2
    print("Case 2")
    print("Input: nums = [1,1,1,1,1]")
    n = [1,1,1,1,1]
    print("Output: ", s.unequalTriplets(n))
    print("Expected: 0")


if __name__ == "__main__":
    main()
    