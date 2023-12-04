import re

def build_indices_matrix(num_length: int, num_idx: int, line_length: int) -> list:
    if num_idx + num_length > line_length:
        return None

    top_bottom_line_indices = list()
    current_line_indices = list()

    if num_idx - 1 >= 0:
        top_bottom_line_indices.append(num_idx - 1)
        current_line_indices.append(num_idx - 1)

    for i in range(0, num_length):
        top_bottom_line_indices.append(num_idx + i)
    
    if num_idx + num_length < line_length:
        top_bottom_line_indices.append(num_idx + num_length)
        current_line_indices.append(num_idx + num_length)
        
    return [top_bottom_line_indices, current_line_indices, top_bottom_line_indices]


def get_number_on_index(numbers: list, index: int) -> tuple:
    for number in numbers:
        if index >= number[1] and index < number[2]:
            return number
        
    return None


def main():
    prev_line = ""
    crt_line = ""
    next_line = ""
    final_sum = 0

    with open("input.txt", "r") as in_file:
        lines = in_file.readlines()
        line_length = len(lines[0].strip())

        for i in range(0, line_length):
            if i - 1 >= 0:
                prev_line = lines[i - 1]
            else:
                prev_line = ""

            if i + 1 < line_length:
                next_line = lines[i + 1]
            else:
                next_line = ""
            
            crt_line = lines[i]

            prev_numbers = list()
            crt_numbers = list()
            next_numbers = list()
            
            if prev_line != "":
                for number in re.finditer(r'\d+', prev_line):
                    prev_numbers.append((number.group(), number.start(), number.end()))

            if next_line != "":
                for number in re.finditer(r'\d+', next_line):
                    next_numbers.append((number.group(), number.start(), number.end()))

            for number in re.finditer(r'\d+', crt_line):
                crt_numbers.append((number.group(), number.start(), number.end()))
            
            for gear in re.compile(r'\*').finditer(crt_line):
                adjacent_numbers = list()
                gear_idx = gear.start()
                indices = build_indices_matrix(1, gear_idx, line_length)
                gear_numbers = list()

                if prev_line != "":
                    for index in indices[0]:
                        number = get_number_on_index(prev_numbers, index)
                        if number not in gear_numbers and number != None:
                            gear_numbers.append(number)

                for index in indices[1]:
                    number = get_number_on_index(crt_numbers, index)
                    if number not in gear_numbers and number != None:
                        gear_numbers.append(number)

                if next_line != "":
                    for index in indices[2]:
                        number = get_number_on_index(next_numbers, index)
                        if number not in gear_numbers and number != None:
                            gear_numbers.append(number)
                
                gear_product = 0

                if len(gear_numbers) == 2:
                    gear_product = int(gear_numbers[0][0]) * int(gear_numbers[1][0])

                final_sum += gear_product
                
    
    print(final_sum)


if __name__ == "__main__":
    main()