class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        

        return 0

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3")
    n = [3,0,1,1,9,7]
    print("Output: ", s.countGoodTriplets(n))
    print("Expected: 4")

    # case 2
    print("Case 2")
    print("Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1")
    n = [1,1,2,2,3]
    print("Output: ", s.countGoodTriplets(n))
    print("Expected: 0")


if __name__ == "__main__":
    main()
    