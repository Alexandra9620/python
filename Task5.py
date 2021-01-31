my_f = open('input_files/Task5.txt', 'w')
nums = '2 34 678 43 694 57383 458674598 34985734'
my_f.writelines(nums)
my_f.close()
with open('input_files/Task5.txt', 'r') as f:
    nums2 = f.readlines()[0]
    total = 0
    for n in nums2.split():
        n = float(n)
        total += n

    print(total)
