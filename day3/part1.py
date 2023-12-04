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

            for number in re.finditer(r'\d+', crt_line):
                num_index = number.start()
                num_length = len(number.group())
                
                indices = build_indices_matrix(num_length, num_index, line_length)
                
                has_symbol_adjacent = False

                if prev_line != "":
                    for index in indices[0]:
                        if prev_line[index] != ".":
                            has_symbol_adjacent = True
                            break
                
                if not has_symbol_adjacent:
                    for index in indices[1]:
                        if crt_line[index] != ".":
                            has_symbol_adjacent = True
                            break
                    
                    if next_line != "":
                        for index in indices[2]:
                            if next_line[index] != ".":
                                has_symbol_adjacent = True
                                break

                if has_symbol_adjacent:
                    final_sum += int(number.group())
    
    print(final_sum)


if __name__ == "__main__":
    main()