class Luhn:
    def __init__(self, card_num):
        self.card_num = self.input_valid(card_num)
    
    def input_valid(self, card_num):
        card = card_num.replace(' ', '')
        if len(card) < 2:
            return False
            # raise ValueError("Please enter a number with at least 2 digits.")
        if not card.isdigit():
            return False
            # raise ValueError("Please enter only numbers.")
        return card

    def valid(self):
        if not self.card_num:
            return False
        checksum = 0
        for i, num in enumerate(self.card_num):
            digit = int(num)
            if i % 2 == 0:
                checksum += 2 * digit
                if digit >= 5:
                    checksum -= 9
            else:
                checksum += digit
            # print(i, digit, checksum)
        
        return True if checksum % 10 == 0 else False

if __name__ == "__main__":
    c1 = "4539 1488 0343 6467"
    c2 = "8273 1232 7352 0569"
    c3 = "8273 1232 7352 056df"
    c4 = "3"
    c = "095 245 88"
    c = "059"

    card = Luhn(c1)
    print(card.valid())
    print(card.valid())
