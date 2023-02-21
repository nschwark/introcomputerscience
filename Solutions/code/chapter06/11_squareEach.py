def squareEach(nums):
    x = 0

    for num in nums:
        
        nums[x] = num ** 2

        x = x + 1

    return nums

def main():
    
    nums = [1,2,3]
    
    print(squareEach(nums))

main()