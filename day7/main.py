class Card:
    
    labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    
    def _init__(self, config: str):
        temp = config.split(' ')
        cards = temp[0]
        self.bid = int(temp[1])
        self.cards = list(cards)
    
    
    def calculateScore():
        

def main():
    with open('input.txt', 'r') as file:
        contents = file.read()
    arr = []
    arr = contents.split('\n')
    
    
    
    
if __name__ == "__main__":
    main()