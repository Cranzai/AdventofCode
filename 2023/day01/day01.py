import re

#part A
with open("day01.inp", "r") as input:
    sum = 0
    for line in input.readlines():
        nums = re.findall(r'\d', line)
        sum += int(nums[0]+nums[-1])

    print(sum)

#part B
with open("day01.inp", "r") as input:
    sum = 0
   
    num_dict = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    pattern = "(?=(\d)|(%s))" % ")|(".join(num_dict.keys())

    for line in input.readlines():
        nums = []
        for num in [item for row in re.findall(pattern,line) for item in row]:
            if num in num_dict.keys():
                nums.append(num_dict[num])
            elif num in num_dict.values():
                nums.append(num)

        sum += int(nums[0]+nums[-1])

    print(sum)
