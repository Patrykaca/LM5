# Patryk Kaca 253473
# Wariant na ocenę dostateczną


class LL1:
    def __init__(self, expression):

        # self.C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # self.O = ['*', ':', '+', '-', '^']
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
        # print(self.arithmetic_expression)
        self.arithmetic_expression.append('$')
    
    def next_char(self):
        self.char += 1
        
    def check_first(self, first):
        return self.arithmetic_expression[self.char] in first

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
                # if self.check_first(self.O):
                if self.read_O():
                    self.next_char()
                    return self.read_W()
                return True
            return False
        return False


    def read_P(self):
        if self.check_first(self.first_P):
            # if self.check_first(self.C):
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
        dot_encountered = False  # Flag to indicate if a dot has been encountered
        digit_encountered_before_dot = False

        while True:
            if self.check_first(self.first_R):
                if not dot_encountered:
                    digit_encountered_before_dot = True
                # self.next_char()
                # continue  # If the character is a digit, move to the next character
                if self.read_C():
                    self.next_char()
                    continue  # If the character is a digit, move to the next character
                else:
                    return False
            elif self.check_first(self.dot):
                self.next_char()
                if (dot_encountered or not digit_encountered_before_dot
                        or self.arithmetic_expression[self.char] not in self.first_R):
                    return False  # If dot already encountered or no digit before dot or no digit after dot, return False
                dot_encountered = True  # Set the flag if a dot is encountered for the first time
                continue
            elif not self.check_first(self.first_R):
                return True
            else:  # If any other character is encountered, return False
                return False
        return False

# arithmetic_expression = '(1.2*3)+5-(3^(23.4+3)+0.05)^3;8:3;'
# arithmetic_expressions = [
#     '(1.2*3)+5-(3^(23.4+3)+0.05)^3;8:3;'
#     , '2+2-4523.234556+(53-3);'
#     , '((53.53:5)-5);13-(53.3^6);'
#     , '((53.53:5)-5);13-(.53.3^6);'
#     , '.43+56;'
#     , '2.2;.5;'
#     , '(4-0)^43;53-(53:56);'
#     , '(4-+1);'
#     , '2^4;'
# ]
#
#
# for arithmetic_expression in arithmetic_expressions:
#     ll1 = LL1(arithmetic_expression)
#     result = ll1.read_S()
#     if result:
#
#         print(f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[92mzostało zaakceptowane\033[92m\033[0m.')
#     else:
#         print(f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[91mnie zostało zaakceptowane\033[91m\033[0m.')
#
#
# ll1 = LL1(arithmetic_expression)
# result = ll1.read_S()


arithmetic_expression = input('Podaj wyrażenie (pamiętaj o średniku):\n')
ll1 = LL1(arithmetic_expression)
result = ll1.read_S()
if result:
    print(f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[92mzostało zaakceptowane\033[92m\033[0m.')
else:
    print(f'Wyrażenie "\x1B[3m\033[93m{arithmetic_expression}\033[93m\x1B[0m" \033[1m\033[91mnie zostało zaakceptowane\033[91m\033[0m.')

