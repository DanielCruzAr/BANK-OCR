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
            
            " _ |_| _|": "9"
        }
        self.path = path
        self.blocks = self.get_blocks()
        self.numbers = []
        self.parse_numbers()
        
    def get_blocks(self):
        print(f"leyendo archivo {self.path}...")
        with open(self.path, "r") as file:
            lines = file.readlines()
            lines = [line.replace('\n', '') for line in lines]
            blocks = [lines[i:i+4] for i in range(0, len(lines), 4)]
        return blocks
    
    def get_number(self, block):
        digits = ["".join([block[row][col:col+3] for row in range(3)]) for col in range(0, 27, 3)]
        number = "".join([self.digit_map.get(digit, "?") for digit in digits])
        return number
    
    def parse_numbers(self):
        print("transformando numeros...")
        for block in self.blocks:
            number = self.get_number(block)
            self.numbers.append(number)
    
    def checksum(self, number):
        if len(number) != 9:
            return False
        return sum([int(number[i]) * (9 - i) for i in range(9)]) % 11 == 0
    
    def write_output(self, path):
        with open(path, "w") as file:
            for number in self.numbers:
                print(f"validando {number}...", end=" ")
                if "?" in number:
                    print("ILL")
                    file.write(f"{number} ILL\n")
                elif not self.checksum(number):
                    print("ERR")
                    file.write(f"{number} ERR\n")
                else:
                    print("OK")
                    file.write(f"{number} OK\n")
        print(f"resultados guardados en {path}")