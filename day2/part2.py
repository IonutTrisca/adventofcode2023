def main():
    max_cube_data = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    cubes_sum = 0

    with open("input.txt", "r") as in_file:
        for line in in_file:
            line_data = line.split(":")
            subsets_raw = line_data[1].split(";")

            min_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }

            for subset in subsets_raw:
                subset_cube_data = subset.strip().split(",")

                for draw in subset_cube_data:
                    draw_data_raw = draw.strip().split(" ")
                    draw_number = int(draw_data_raw[0])
                    draw_color = draw_data_raw[1]

                    if draw_number > min_cubes[draw_color]:
                        min_cubes[draw_color] = draw_number
            
            set_power = 1

            for cube in min_cubes.keys():
                set_power *= min_cubes[cube]

            cubes_sum += set_power
    
    print(cubes_sum)


                    


if __name__ == "__main__":
    main()