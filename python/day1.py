# part1
def part1(): 
  file_path = "inputFile1.txt"

  chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  total = 0;

  with open(file_path, "r") as file:
    for line in file.readlines():
      line = line.strip()
      line = ''.join(char for char in line if char.isdigit())
      if line:  # check if line is not empty
        total += int(line[0] + line[-1])

  return total;


#print(part1());
#Answer: 56465

# part2

WORD_TO_DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def get_combined_digits(line):
    # positions stores tuples of (idx, digit) for each spelled-out 
    # number found in the line, this helps in replacing the spelled-out numbers 
    # with their corresponding digits, considering their order and overlaps in the string
    positions = [
        (idx, digit)
        for word, digit in WORD_TO_DIGIT_MAP.items()
        for idx in range(len(line))
        if line.startswith(word, idx)
    ]
    
    print(positions)

    # add existing numerical digits and their positions
    positions.extend((idx, ch) for idx, ch in enumerate(line) if ch.isdigit())

    # handle no digits case
    if not positions:
        return 0

    # sort by position idx
    positions.sort(key=lambda x: x[0])

    # extract first and last digit based on combined order
    first, last = positions[0][1], positions[-1][1]
    return int(first + last)

def part2():
  file_path = "testInputFile2.txt"
  with open(file_path, "r") as file:
    sum = 0
    for line in file.readlines():
        tmp = get_combined_digits(line.strip())
        # print(f"{line.strip()} -> {tmp}")
        sum += tmp

    return sum
          

print(part2())
#Answer:  


