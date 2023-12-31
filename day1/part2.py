import re

def main():
    infile = open("input.txt", "r")
    
    word_to_num = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8', 
        'nine': '9',
    }
    
    num_lst = list(word_to_num.keys()) + list(word_to_num.values())

    sum = 0

    for line in infile:
        nums = re.findall(r"(?=("+'|'.join(num_lst)+r"))", line)
        current_num = ""

        for i in range(0, len(nums)):
            if nums[i] in word_to_num.keys():
                nums[i] = word_to_num[nums[i]]

        if len(nums) == 1:
            current_num = nums[0] * 2
        else:
            current_num = nums[0] + nums[-1]

        current_num = int(current_num)

        sum += current_num
    
    infile.close()

    print(sum)


if __name__ == "__main__":
    main()