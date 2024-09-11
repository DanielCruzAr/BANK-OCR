from bank_ocr import BankOCR

def main():
    input_file = "inputs/input.txt"
    output_file = "outputs/output.txt"
    
    ocr = BankOCR(input_file)
    ocr.write_output(output_file)

if __name__ == '__main__':
    main()