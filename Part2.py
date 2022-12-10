totalCycles = 0
totalSignalStrength = 0
screen = ""


def readFile():
    file = open("InputData.txt", "r")
    return file


def increaseX(x, command, value):
    global totalCycles
    if (command == "noop"):
        totalCycles += 1
        checkpoint(x)
    else:
        for i in range(2):
            totalCycles += 1
            checkpoint(x)
        x += value
    return x


def checkpoint(x):
    global totalSignalStrength
    global screen

    if (x <= totalCycles % 40 <= x + 2):
        # Add # to screen
        screen += "#"
        pass
    else:
        # Add . to screen
        screen += "."
        pass
    if (totalCycles % 40 == 0):
        # Add /n to screen
        screen += "\n"
        totalSignalStrength += (totalCycles * x)


def main():
    file = readFile()
    x = 1
    for line in file:
        split = line.strip().split(" ")
        if (split[0] == "noop"):
            x = increaseX(x, split[0], 0)
        else:
            x = increaseX(x, split[0], int(split[1]))
    print(f"{screen}")
    file.close()


if (__name__ == "__main__"):
    main()
