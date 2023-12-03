def main():
    max_cube_data = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    ids_sum = 0

    with open("input.txt", "r") as in_file:
        for line in in_file:
            line_data = line.split(":")
            game_id = int(line_data[0].split(" ")[1])
            subsets_raw = line_data[1].split(";")
            is_game_valid = True

            for subset in subsets_raw:
                subset_cube_data = subset.strip().split(",")
                
                draw_data = dict()

                for draw in subset_cube_data:
                    draw_data_raw = draw.strip().split(" ")
                    draw_data[draw_data_raw[1]] = int(draw_data_raw[0])

                for draw in draw_data.keys():
                    if draw_data[draw] > max_cube_data[draw]:
                        is_game_valid = False
                        break
                
                if not is_game_valid:
                    break

            if is_game_valid:
                ids_sum += game_id

        print(ids_sum)

                    


if __name__ == "__main__":
    main()