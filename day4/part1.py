def main():
    final_points = 0

    with open("input.txt", "r") as in_file:
        for line in in_file:
            number_sets = line.split(":")[1].split("|")
            winning_numbers = number_sets[0].strip().split()
            owned_numbers = number_sets[1].strip().split()
            
            winning_numbers_owned = 0

            for number in owned_numbers:
                if number in winning_numbers:
                    winning_numbers_owned += 1

            if winning_numbers_owned != 0:
                final_points += 2 ** (winning_numbers_owned - 1)

    print(final_points)


if __name__ == "__main__":
    main()