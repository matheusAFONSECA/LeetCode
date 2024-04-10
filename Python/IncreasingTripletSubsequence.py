class Solution:
    def increasingTriplet(self, nums) -> bool:
        
        return True
    

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


if __name__ == "__main__":
    main()