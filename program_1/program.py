with open('input.txt', 'r') as file:
    total_number = 0

    for line in file:
        str_number = ""

        for letter in line:
            if str.isdigit(letter):
                str_number+=letter
                break

        for letter in line[::-1]:
            if str.isdigit(letter):
                str_number+=letter
                break
        
        
        total_number += int(str_number)

    
    print(total_number)


