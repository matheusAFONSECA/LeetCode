class Solution:
    def findNumberOfLIS(self, nums) -> int:
      
        # Initialize two arrays to store the length of longest increasing subsequences and their corresponding counts
        lengths = [1] * len(nums)
        counts = [1] * len(nums)

        # Traverse the array to find the longest increasing subsequence length and their counts
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        return sum(counts[i] for i in range(len(nums)) if lengths[i] == max_length)
    

def main():         # função principal

    s = Solution()      # instanciando o objeto

    # case 1
    print("Case 1")
    print("Input: nums = [1,3,5,4,7]")
    n = [1,3,5,4,7]
    print("Output: ", s.findNumberOfLIS(n))
    print("Expected: 2")

    # case 2
    print("Case 2")
    print("Input: nums = [2,2,2,2,2]")
    n = [2,2,2,2,2]
    print("Output: ", s.findNumberOfLIS(n))
    print("Expected: 5")


if __name__ == "__main__":
    main()