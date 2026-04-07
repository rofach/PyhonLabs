def get_treasure_coordinates(route_steps):
    x_coord = 0
    y_coord = 0

    for step in route_steps:
        parts = step.split()
        if len(parts) != 2:
            continue

        direction = parts[0]
        distance = int(parts[1])

        if direction == "North":
            y_coord += distance
        elif direction == "South":
            y_coord -= distance
        elif direction == "East":
            x_coord += distance
        elif direction == "West":
            x_coord -= distance

    return x_coord, y_coord


def main():
    route_steps = []
    print("Вводьте команди")
    while True:
        line = input()
        if line == "Treasure!":
            break
        route_steps.append(line)

    x_coord, y_coord = get_treasure_coordinates(route_steps)
    print("Координати:", x_coord, y_coord)


if __name__ == "__main__":
    main()
