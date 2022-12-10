totalCycles = 0
totalSignalStrength = 0


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
    if (totalCycles == 20 or ((totalCycles - 20) % 40 == 0)):
        print(f"Cycle: {totalCycles}, X: {x}, Signal strength: {totalCycles * x}")
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
    print(f"Total Signal Strength: {totalSignalStrength}")
    file.close()

if (__name__ == "__main__"):
    main()

