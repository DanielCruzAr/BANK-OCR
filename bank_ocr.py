class BankOCR:
    def __init__(self, path) -> None:
        self.digit_map = {
            " _ | ||_|": "0",
            
            "     |  |": "1",
            
            " _  _||_ ": "2",
            
            " _  _| _|": "3",
            
            "   |_|  |": "4",
            
            " _ |_  _|": "5",
            
            " _ |_ |_|": "6",
            
            " _   |  |": "7",
            
            " _ |_||_|": "8",
            
            " _|_| _|": "9"
        }
        self.path = path
        
    def get_blocks(self):
        with open(self.path, "r") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            blocks = [lines[i:i+4] for i in range(0, len(lines), 4)]
        return blocks
    
    def get_number(self, block):
        digits = ["".join([block[row][col:col+3] for row in range(3)]) for col in range(0, 27, 3)]
        number = "".join([self.digit_map.get(digit, "?") for digit in digits])
        return number
    
    def checksum(self, number):
        return sum([int(number[i]) * (9 - i) for i in range(9)]) % 11 == 0