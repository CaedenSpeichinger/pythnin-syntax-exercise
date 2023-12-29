def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for x in nums:
        if x == 7:
            return 'This is true'
        else:
            'This is false'
        

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

