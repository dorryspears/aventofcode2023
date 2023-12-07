def part_1(dist, time) -> int:

    final = None

    for i in range(len(dist)):
        temp = getNumberOfWays(dist[i], time[i])
        if final == None:
            final = temp
        else:
            final *= temp
    
    return final

def getNumberOfWays(dist, time) -> int:
    # [430, 1036, 1307, 1150]
    # [61, 67, 75, 71]
    count = 0
    holdLevel = 0
    while holdLevel < time:
        current_time = time - holdLevel 
        if holdLevel * current_time > dist:
            count += 1
            
        holdLevel += 1
        
    return count
    

def main():
    with open('input.txt', 'r') as file:
        contents = file.read()
    arr = []
    arr = contents.split('\n')
    
    dist = arr[1].split(":")[1].strip().split(" ")
    
    dist = list(filter(None, dist))
    
    for i in range(len(dist)):
        dist[i] = int(dist[i])
        
    time = arr[0].split(":")[1].strip().split(" ")
    
    time = list(filter(None, time))
    
    for i in range(len(time)):
        time[i] = int(time[i])
        
    
    print("Sum 1: " + str(part_1(dist, time)))
    
    #join list as strings and convert to int
    part_2_time = int("".join(map(str, time)))
    part_2_dist = int("".join(map(str, dist)))
    
    print("Sum 2: " + str(getNumberOfWays(part_2_dist, part_2_time)))
    

if __name__ == "__main__":
    main()