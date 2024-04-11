class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:

        count = 0           # contador para quando as condições são satisfeitas
        n = len(arr)        # quantidade de elementos da array

        # Iterate over all possible triplets
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
                            
        return count
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3")
    n = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    print("Output: ", s.countGoodTriplets(n, a, b, c))
    print("Expected: 4")

    # case 2
    print("Case 2")
    print("Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1")
    n = [1,1,2,2,3]
    a = 0
    b = 0
    c = 1
    print("Output: ", s.countGoodTriplets(n, a, b, c))
    print("Expected: 0")


if __name__ == "__main__":
    main()
    