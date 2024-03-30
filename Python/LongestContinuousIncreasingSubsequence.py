class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        
        return int(2)
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [1,3,5,4,7]")
    n = [1,3,5,4,7]
    print("Output: ", s.findLengthOfLCIS(n))
    print("Expected: 3")

    # case 2
    print("Case 2")
    print("Input: nums = [2,2,2,2,2]")
    n = [2,2,2,2,2]
    print("Output: ", s.findLengthOfLCIS(n))
    print("Expected: 1")


if __name__ == "__main__":
    main()