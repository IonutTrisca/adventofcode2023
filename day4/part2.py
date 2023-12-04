def main():
    scratchcards = dict()

    with open("input.txt", "r") as in_file:
        lines = in_file.readlines()
        lines = [i for i in lines if i.strip() != ""]

        for i in range(0, len(lines)):
            scratchcards[i + 1] = 1

        for line in lines:
            card_idx = int(line.split(":")[0].split()[1])

            number_sets = line.split(":")[1].split("|")
            winning_numbers = number_sets[0].strip().split()
            owned_numbers = number_sets[1].strip().split()
            
            winning_numbers_owned = 0

            for number in owned_numbers:
                if number in winning_numbers:
                    winning_numbers_owned += 1

            for i in range(1, winning_numbers_owned + 1):
                scratchcards[card_idx + i] += scratchcards[card_idx]

    total_scratchcards = 0

    for scratchcard in scratchcards.values():
        total_scratchcards += scratchcard

    print(total_scratchcards)


if __name__ == "__main__":
    main()
