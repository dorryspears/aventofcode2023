class GameRound(object):
    def __init__(self, config: str):
        config = config.split(":")
        self.game_id = int(config[0].split(" ")[1])
        self.rounds = []
        for round in config[1].split(";"):
            temp = {}
            for color in round.split(","):
                color_split =  color.strip().split(" ")
                temp[color_split[1]] = int(color_split[0])
                
            self.rounds.append(temp)
            
    def meetsWinConditon(self, wonConfig : dict) -> bool:
        for r in self.rounds:
            for key in r.keys():
                if r[key] > wonConfig[key]:
                    return False
                
        return True
    
    def getMinPowerOfCubes(self) -> int:
        min_cubes = {}
        for r in self.rounds:
            for key in r.keys():
                if min_cubes.get(key) == None:
                    min_cubes[key] = r[key]
                elif min_cubes.get(key) < r[key]:
                    min_cubes[key] = r[key]
        sum = 1            
        for value in min_cubes.values():
            sum *= value
            
        return sum
        
def main():
    with open('input.txt', 'r') as file:
        contents = file.read()
    arr = []
    arr = contents.split('\n')
    
    sum_1 = 0
    sum_2 = 0
    
    #12 red cubes, 13 green cubes, and 14 blue cubes
    win_con = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    
    for gameConfig in arr:
        game = GameRound(gameConfig)
        if game.meetsWinConditon(win_con):
            sum_1 += game.game_id 
        
        sum_2 += game.getMinPowerOfCubes()
    
    #Part 1  
    print("Sum: " + str(sum_1))

    #Part 2
    print("Sum: " + str(sum_2))
    
if __name__ == "__main__":
    main()