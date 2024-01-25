import ast


class LL1:
    def __init__(self, expression):

        self.C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.O = ['*', ':', '+', '-', '^']
        self.opening_bracket = ['(']
        self.closing_bracket = [')']
        self.semicolon = [';']
        self.dot = ['.']
        self.eof = ['$']
        self.arithmetic_expression = []

        self.first_S = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
        self.first_P = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
        self.follow_P = ['*', ':', '+', '-', '^', ')', '$']
        self.first_R = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.follow_R = ['*', ':', '+', '-', '^', '@', ';', ')', '$']
        self.first_L = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.first_Lp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@']
        self.first_W = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(']
        self.follow_W = ['*', ':', '+', '-', '^', '@', ';', ')', '$']

        self.char = 0

        for i in expression:
            self.arithmetic_expression.append(i)
        print(self.arithmetic_expression)


    def parse(self):
        while self.arithmetic_expression[self.char] in self.first_R:
            self.read_S()
        return True


    def read_S(self):
        if self.arithmetic_expression[self.char] in self.first_P:
            self.read_P()
            if self.arithmetic_expression[self.char] in self.O:
                self.read_P()
            if self.arithmetic_expression[self.char] in self.semicolon:
                self.read_S()



        if self.arithmetic_expression[self.char] in self.first_P:
            self.read_P()
            if self.arithmetic_expression[self.char] in self.O:
                self.char = self.char + 1
                self.read_S()
            if self.arithmetic_expression[self.char] in self.semicolon:
                # self.char = self.char + 1
                self.read_S()
            if self.arithmetic_expression[self.char] in self.eof:
                return True
        return False
            # raise ValueError(f'Invalid self.character {arithmetic_expression[self.char]}. Expected one of {self.O} or {self.C} or {self.semicolon}')

# Działa!!!!!!!!!!!
    def read_P(self):
        if self.arithmetic_expression[self.char] in self.first_P:
            if self.arithmetic_expression[self.char] in self.C:
                return self.read_R()
            elif self.arithmetic_expression[self.char] in self.opening_bracket:
                self.char = self.char + 1
                if self.read_W():
                    if self.arithmetic_expression[self.char] in self.closing_bracket:
                        self.char = self.char + 1
                        return True
                    return False
            return False
        return False

# Działa!!!!!!!!!!!
    def read_W(self):
        if self.arithmetic_expression[self.char] in self.first_W:
            if self.read_P():
                if self.arithmetic_expression[self.char] in self.O:
                    self.char = self.char + 1
                    return self.read_W()
                return True
            return False
        return False



# Działa!!!!!!!!!!!
    def read_R(self):
        dot_encountered = False  # Flag to indicate if a dot has been encountered
        digit_encountered_before_dot = False

        while True:
            if self.arithmetic_expression[self.char] in self.first_R:
                if not dot_encountered:
                    digit_encountered_before_dot = True
                self.char = self.char + 1
                continue # If the character is a digit, move to the next character
            elif self.arithmetic_expression[self.char] in self.dot:
                if (dot_encountered or not digit_encountered_before_dot
                    or self.arithmetic_expression[self.char + 1] not in self.first_R):
                    return False # If dot already encountered or no digit before dot or no digit after dot, return False
                dot_encountered = True # Set the flag if a dot is encountered for the first time
                self.char = self.char + 1
            elif self.arithmetic_expression[self.char] in self.follow_R:
                return True
            else: # If any other character is encountered, return False
                return False

        # In case there is no '$' at the end of the string, which should not happen as per the requirements
        return False

    def read_C(self):
        if arithmetic_expression[self.char] in self.C:
            self.char = self.char + 1
            return True
        self.char = self.char + 1
        return False

    def read_O(self):
        if arithmetic_expression[self.char] in self.O:
            self.char = self.char + 1
            return True
        self.char = self.char + 1
        return False

# arithmetic_expression = input('Enter: ')
arithmetic_expression = '((2-6)-1.3)' + '$'
ll1 = LL1(arithmetic_expression )

ret = ll1.read_P()
if ret:
    print('True')
else:
    print('False')