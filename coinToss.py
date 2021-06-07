#coin_toss.py
import random
class Coin:
    
    sideup = ""
    
    def __init__(self):
        self.sideup = "Heads"
        
    def toss(self):
        if random.randint(0, 1) == 1:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"
            
    def get_sideup(self):
        return self.sideup
    
def main():
    
    gambling_coin = Coin()
    
    gambling_coin.toss()
    coinSide = gambling_coin.get_sideup()
    print("Toss #1 turned ", coinSide)

    gambling_coin.toss()
    coinSide = gambling_coin.get_sideup()
    print("Toss #2 turned ", coinSide)

    gambling_coin.toss()
    coinSide = gambling_coin.get_sideup()
    print("Toss #3 turned ", coinSide)

    gambling_coin.toss()
    coinSide = gambling_coin.get_sideup()
    print("Toss #4 turned ", coinSide)

main()
