def productExceptSelf(nums):
    """Sets an output array filled with the value 1 for the length of the input array
    Iterates through numbers going forwards to calculate prefixes
    Updates output array to the value of prefix on each iteration
    Updates prefix AFTER updating output array
    Iterates through numbers starting from the right
    Multiplies our prefix value in output by our postfix value
    Updates postfix AFTER updating output array
    returns: array of products, excluding the ith number"""
    output = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        
        output[i] *= postfix
        postfix *= nums[i]
    return output


print(productExceptSelf([1,2,3,4])) #[24, 12, 8, 6]
print(productExceptSelf([-1,1,0,-3,3])) #[0, 0, 9, 0, 0]