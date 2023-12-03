def main():
    
    #Read contents of input
    with open('input.txt', 'r') as file:
        contents = file.read()
    arr = []
    arr = contents.split('\n')
    
    puzzle_input = []
    for line in arr:
        puzzle_input.append(list(line))
        
    #Part 1        
    print("Sum Part 1: " + str(part_1(puzzle_input)))
    print("Sum Part 2: " + str(part_2(puzzle_input)))

def part_1(puzzle_input) -> int:
    sum_1 = 0
    for row, line in enumerate(puzzle_input):
        start_num = None
        end_num = None
        for index, symbol in enumerate(line):
            if symbol.isdigit() and start_num == None:
                start_num = index
            elif symbol.isdigit() and start_num != None:
                end_num = index
                
            if (not symbol.isdigit() or index == len(line) - 1)  and start_num != None :
                #check before row for special
                if not end_num:
                    end_num = start_num 
                
                
                #join number
                temp = ""
                for temp_index in range(end_num - start_num + 1):
                    temp += line[start_num + temp_index]
                
                number = int(temp)
                
                bottom_range = start_num - 1
                top_range = end_num + 1
                
                if bottom_range < 0:
                    bottom_range = 0
                
                elif top_range >= len(line):
                    top_range = len(line) - 1
                    
                
                start_num, end_num = None, None
                found_special = False
                if row != 0:
                    temp = puzzle_input[row - 1][bottom_range:top_range + 1]
                    for symbol in temp:
                        if not (symbol.isdigit() or symbol == "."):
                            found_special = True
                            break
                
                if row != len(puzzle_input) - 1:
                    temp = puzzle_input[row + 1][bottom_range:top_range + 1]
                    for symbol in temp:
                        if not (symbol.isdigit() or symbol == "."):
                            found_special = True
                            break
                
                #check sideways
                temp = puzzle_input[row][bottom_range:top_range + 1]
                for symbol in temp:
                    if not (symbol.isdigit() or symbol == "."):
                        found_special = True
                        break
                
                if found_special:
                    sum_1 += number
    
    return sum_1

def part_2(puzzle_input) -> int:
    sum = 0
    gear = {}
    for row, line in enumerate(puzzle_input):
        start_num = None
        end_num = None
        for index, symbol in enumerate(line):
            if symbol.isdigit() and start_num == None:
                start_num = index
            elif symbol.isdigit() and start_num != None:
                end_num = index
                
            if (not symbol.isdigit() or index == len(line) - 1)  and start_num != None :
                #check before row for special
                if not end_num:
                    end_num = start_num 
                
                
                #join number
                temp = ""
                for temp_index in range(end_num - start_num + 1):
                    temp += line[start_num + temp_index]
                
                number = int(temp)
                
                bottom_range = start_num - 1
                top_range = end_num + 1
                
                if bottom_range < 0:
                    bottom_range = 0
                
                elif top_range >= len(line):
                    top_range = len(line) - 1
                    
                
                start_num, end_num = None, None
                found_special = False
                if row != 0:
                    temp = puzzle_input[row - 1][bottom_range:top_range + 1]
                    for offset, symbol in enumerate(temp):
                        if symbol == "*":
                            pos = str(row - 1) + "-" + str(offset+bottom_range)
                            if gear.get(pos)== None:
                                gear[pos] = [number]
                                found_special = True
                            else:
                                gear[pos].append(number)
                            break
                
                
                if row != len(puzzle_input) - 1 and not found_special:
                    temp = puzzle_input[row + 1][bottom_range:top_range + 1]
                    for offset, symbol in enumerate(temp):
                        if symbol == "*":
                            pos = str(row + 1) + "-" + str(offset+bottom_range)
                            if gear.get(pos) == None:
                                gear[pos] = [number]
                                found_special = True
                            else:
                                gear[pos].append(number)
                            break
                
                #check sideways
                if not found_special:
                    temp = puzzle_input[row][bottom_range:top_range + 1]
                    for offset, symbol in enumerate(temp):
                        if symbol == "*":
                            pos = str(row) + "-" + str(offset+bottom_range)
                            if gear.get(pos) == None:
                                gear[pos] = [number]
                                found_special = True
                            else:
                                gear[pos].append(number)
                            break
                
    
    
    for key in gear.keys():
        temp = gear[key]
        if len(temp) == 2:
            sum += temp[0] * temp[1]
                    
    return sum
        
if __name__ == "__main__":
    main()