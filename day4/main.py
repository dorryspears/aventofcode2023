class LotoTicket():
    def calcValue(self):
        count = 0
        for num in self.nums:
            if num in self.winning_nums:
                if self.value == 0:
                    self.value = 1
                    count += 1
                else:
                    self.value *= 2
                    count += 1
        
        self.copy_count = count
        self.value = int(self.value)
            
    
    def __init__(self, config):
        temp = config.split(":")
        self.gameId = int(temp[0].split(" ")[-1])
        temp = temp[1].split("|")
        wn = temp[0].split(" ")
        n = temp[1].split(" ")
        
        #Clean
        self.winning_nums = []
        self.nums = []
        self.value = 0
        self.copy_count = 0
        
        for num in wn:
            if num != '':
                self.winning_nums.append(int(num))
        
        for num in n:
            if num != '':
                self.nums.append(int(num))
                
        self.winning_nums.sort()
        self.nums.sort()
        
        self.calcValue()
        
        

    

def main():
    #Read contents of input
    with open('input.txt', 'r') as file:
        contents = file.read()
    arr = []
    arr = contents.split('\n')
    
    copys = {}
    sum_1 = 0
    sum_2 = 0
    for ticket in arr:
        cur_ticket =  LotoTicket(ticket)
        sum_1 += cur_ticket.value
        cur_id = cur_ticket.gameId
        
        if cur_ticket.copy_count > 0:
            for i in range(cur_ticket.copy_count):
                if cur_id + 1 + i in copys:
                    copys[cur_id + 1 + i] += 1
                else:
                    copys[cur_id + 1 + i] = 1
        
        if cur_id in copys:
            if cur_ticket.copy_count > 0:
                for i in range(cur_ticket.copy_count):
                    if cur_id + 1 + i in copys:
                        copys[cur_id + 1 + i] += copys[cur_id]
                    else:
                        copys[cur_id + 1 + i] += copys[cur_id]
    
    
    for key in copys:
        sum_2 += copys[key]
        
    sum_2 += len(arr)

    print("Sum 1: " + str(sum_1))
    print("Sum 2: " + str(sum_2))

if __name__ == "__main__":
    main()