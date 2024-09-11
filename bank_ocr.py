class BankOCR:
    '''Clase que lee un archivo de texto con bloques de digitos formados por "|", "_" y los transforma a numeros.
    '''
    
    def __init__(self, path) -> None:
        '''Constructor de la clase BankOCR.
            Params:
                path (str): ruta del archivo de texto con los bloques de digitos.
        '''
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
        '''Lee el archivo de texto y regresa una lista de bloques de digitos.
        '''
        print(f"leyendo archivo {self.path}...")
        with open(self.path, "r") as file:
            lines = file.readlines()
            lines = [line.replace('\n', '') for line in lines]
            blocks = [lines[i:i+4] for i in range(0, len(lines), 4)]
        return blocks
    
    def get_number(self, block):
        '''Un bloque de digitos a un numero.
            Params:
                block (list): bloque de digitos.
            Returns:
                number (str): numero formado por los digitos del bloque.
        '''
        digits = ["".join([block[row][col:col+3] for row in range(3)]) for col in range(0, 27, 3)]
        number = "".join([self.digit_map.get(digit, "?") for digit in digits])
        return number
    
    def parse_numbers(self):
        '''Transforma los bloques de digitos a numeros.
        '''
        print("transformando numeros...")
        for block in self.blocks:
            number = self.get_number(block)
            self.numbers.append(number)
    
    def checksum(self, number):
        '''Valida el numero con el algoritmo de checksum con la fórmula
            (d1*9 + d2*8 + d3*7 + d4*6 + d5*5 + d6*4 + d7*3 + d8*2 + d9*1) % 11 == 0
            Params:
                number (str): numero a validar.
            Returns:
                bool: True si el numero es valido, False en otro caso.
        '''
        if len(number) != 9:
            return False
        return sum([int(number[i]) * (9 - i) for i in range(9)]) % 11 == 0
    
    def write_output(self, path):
        '''Valida los números y escribe los resultados en un archivo de texto
            con el formato "numero OK/ERR/ILL".
            Params:
                path (str): ruta del archivo de texto donde se guardaran los resultados.
        '''
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