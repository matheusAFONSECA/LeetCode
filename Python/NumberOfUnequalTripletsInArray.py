class Solution:
    def unequalTriplets(self, nums) -> int:

        return 0
    

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
    