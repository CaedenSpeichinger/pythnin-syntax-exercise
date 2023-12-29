def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    for x in nums:
      if x >= lowest and x <= highest:
        print (f'{nums} fits')

      # IF 10,20,30,40,50 IS GREATER THAN OR EQUAL TO 15 THEN TAKE THAT NUMBER 
      # IF 10,20,30,40,50 IS LESS THAN OR EQAUAL TO 30 THEN TAKE THAT
      #RESULT WOULD BE 20 AND 30 BECAUSE IN THE RANGE OF 10,20,30,40,50 THOSE FIT 


in_range([10, 20, 30, 40, 50], 15, 30)            
