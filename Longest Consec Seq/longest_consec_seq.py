def longest_consec_seq(nums):
    numSet = set(nums)
    longest = 0
    for n in numSet:
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length += 1
            longest = max(length,longest)
    return longest
nums = [100,4,200,1,3,2]
print(longest_consec_seq(nums))
