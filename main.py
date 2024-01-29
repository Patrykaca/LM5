# Patryk Kaca 253473
# Wariant na ocenę dostateczną


class LL1:
    def __init__(self, expression):

        self.opening_bracket = ['(']
        self.closing_bracket = [')']
        self.semicolon = [';']
        self.dot = ['.']
        self.eof = ['$']
        self.arithmetic_expression = []
        self.first_C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.first_O = ['*', ':', '+', '-', '^']
        self.first_S = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
        self.first_P = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
        self.first_R = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.first_W = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
        self.char = 0

        for i in expression:
            self.arithmetic_expression.append(i)
        self.arithmetic_expression.append('$')

    # funkcje pomocnicze
    def next_char(self):
        self.char += 1

    def check_first(self, first):
        return self.arithmetic_expression[self.char] in first

    # funkcje czytające produkcje
    def read_C(self):
        return self.check_first(self.first_C)

    def read_O(self):
        return self.check_first(self.first_O)

    def read_S(self):
        if self.check_first(self.first_S):
            if self.read_W():
                if self.check_first(self.semicolon):
                    self.next_char()
                    if self.check_first(self.first_S):
                        return self.read_S()
                    elif self.check_first(self.eof):
                        return True
                    return False
                return False
            return False
        return False

    def read_W(self):
        if self.check_first(self.first_W):
            if self.read_P():
                if self.read_O():
                    self.next_char()
                    return self.read_W()
                return True
            return False
        return False

    def read_P(self):
        if self.check_first(self.first_P):
            if self.check_first(self.first_R):
                return self.read_R()
            elif self.check_first(self.opening_bracket):
                self.next_char()
                if self.read_W():
                    if self.check_first(self.closing_bracket):
                        self.next_char()
                        return True
                    return False
                return False
            return False
        return False

    def read_R(self):
        dot_encountered = False
        digit_encountered_before_dot = False

        while True:
            if self.check_first(self.first_R):
                if not dot_encountered:
                    digit_encountered_before_dot = True
                if self.read_C():
                    self.next_char()
                    continue
                else:
                    return False
            elif self.check_first(self.dot):
                self.next_char()
                if (dot_encountered or not digit_encountered_before_dot
                        or self.arithmetic_expression[self.char] not in self.first_R):
                    return False  # jeśli już napotkano kropkę lub brak liczby przed kropką lub brak liczby po kropce
                dot_encountered = True  # flaga - napotkano kropkę
                continue
            elif not self.check_first(self.first_R):
                return True
            else:
                return False
        return False


arithmetic_expression = '(1.2*3)+5-(3^(23.4+3)+0.05)^3;8:3;'
arithmetic_expressions = [
    '(1.2*3)+5-(3^(23.4+3)+0.05)^3;8:3;'
    , '2+2-4523.234556+(53-3);'
    , '((53.53:5)-5);13-(53.3^6);'
    , '((53.53:5)-5);13-(.53.3^6);'
    , '.43+56;'
    , '2.2;.5;'
    , '(4-0)^43;53-(53:56);'
    , '(4-+1);'
    , '2^4;'
]

print('\033[95mPrzypadki testowe:\033[0m')
for arithmetic_expression in arithmetic_expressions:
    ll1 = LL1(arithmetic_expression)
    result = ll1.read_S()
    if result:
        print(
            f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[92mzostało zaakceptowane\033[92m\033[0m.')
    else:
        print(
            f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[91mnie zostało zaakceptowane\033[91m\033[0m.')

ll1 = LL1(arithmetic_expression)
result = ll1.read_S()

arithmetic_expression = input('Podaj wyrażenie (pamiętaj o średniku):\n')
ll1 = LL1(arithmetic_expression)
result = ll1.read_S()
if result:
    print(f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[92mzostało zaakceptowane\033[92m\033[0m.')
else:
    print(f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[91mnie zostało zaakceptowane\033[91m\033[0m.')

