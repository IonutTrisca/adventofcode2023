
def main():
    infile = open("input.txt", "r")
    sum = 0

    for line in infile:
        current_number = ""
        first_num_char = ""
        crt_num_char = ""

        for character in line:
            if character >= "0" and character <= "9":
                if first_num_char == "":
                    first_num_char = character
                else:
                    crt_num_char = character

        if crt_num_char == "":
            crt_num_char = first_num_char

        current_number = first_num_char + crt_num_char
        current_number = int(current_number)

        sum += current_number
    
    print(sum)

if __name__ == "__main__":
    main()