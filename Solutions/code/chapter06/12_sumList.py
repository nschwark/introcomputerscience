def sumList(nums):
    sum = 0

    for num in nums:
        
        sum = sum + num

    return sum

def main():
    
    nums = [1,2,3]
    
    print(sumList(nums))

main()