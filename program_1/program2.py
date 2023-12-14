def partOf(line):
    numberToLetter = ["zero", "one", "two", "three", "four", "five", "six", 
                      "seven", "eight", "nine"]
    
    newString = ""
    for i in range(0, len(line)):
        if (line[i].isdigit()):
            return line[i]
        else:
            newString += line[i]
            for j in range(0, len(numberToLetter)):
                if numberToLetter[j] in newString:
                    return j

def partOfInverted(line):
    numberToLetter = ["zero", "one", "two", "three", "four", "five", "six", 
                      "seven", "eight", "nine"]
    
    newString = ""
    for i in range(0, len(line)):
        if (line[i].isdigit()):
            return line[i]
        else:
            newString = line[i] + newString
            for j in range(0, len(numberToLetter)):
                if numberToLetter[j] in newString:
                    return j

with open('input.txt', 'r') as file:
    total_number = 0

    for line in file:

        str_number = str(partOf(line)) + str(partOfInverted(line[::-1])) 
        print(str_number)
        total_number += int(str_number)

    
    print(total_number)
