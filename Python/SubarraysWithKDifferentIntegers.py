class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:

        return 0
    

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
    