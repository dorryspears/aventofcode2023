from collections import deque
def computeNumbers(text: str, numbers: dict) -> int:
    nums = dict()

    #remove nums that dont need to be counted
    for key in numbers.keys():
        if text.find(key) != -1:
            nums[key] = numbers.get(key)


    first = None
    last = None
    left = 0
    while left < len(text):
        found = False
        if not first:
            if text[left].isdigit():
                first = int(text[left])
                left += 1
            else:
                for key in nums.keys():
                    if text[left:left+len(key)] == key:
                        first = nums.get(key)
                        left += 1
                        found = True
                        break
                if not found:
                    left += 1

        else:
            if text[left].isdigit():
                last = int(text[left])
                left += 1
            else:
                for key in nums.keys():
                    if text[left:left+len(key)] == key:
                        last = nums.get(key)
                        left += 1
                        found = True
                        break
                if not found:
                    left += 1
                        
                
    if last == None:
        last = first       
    return (first * 10) + last

    

def main():

    numbers = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }

    with open('input.txt', 'r') as file:
        contents = file.read()


    arr = []
    arr = contents.split('\n')

    print(arr[0])
    sum = 0
    for text in arr:
        sum +=  computeNumbers(text, numbers)

    print("Sum: " + str(sum))

if __name__ == "__main__":
    main()
    numbers = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
    }

    print(computeNumbers("7pqrstsixteen", numbers))
    print(computeNumbers("abcone2threexyz", numbers))
    print(computeNumbers("fivetwocrhmvxqkvbeightfive1qzcxvds", numbers))

    
