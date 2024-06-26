class PDA:
    def __init__(self):
        self.stack = []
        self.state = 'q0'
    
    def transition(self, char):
        if self.state == 'q0':
            if char.isdigit():
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
                self.state = 'q3'
            else:
                self.state = 'error'
        
        elif self.state == 'q1':
            if char in '+-*/':
                self.state = 'q2'
            elif char == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                    self.state = 'q1'
                else:
                    self.state = 'error'
            elif char.isdigit():
                self.state = 'q1'
            else:
                self.state = 'error'
        
        elif self.state == 'q2':
            if char.isdigit():
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
                self.state = 'q3'
            else:
                self.state = 'error'
        
        elif self.state == 'q3':
            if char.isdigit():
                self.state = 'q1'
            elif char == '(':
                self.stack.append('(')
                self.state = 'q3'
            elif char == ')':
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
                    self.state = 'q1'
                else:
                    self.state = 'error'
            else:
                self.state = 'error'
    
    def process_input(self, input_string):
        for char in input_string:
            self.transition(char)
            if self.state == 'error':
                return False
        
        if self.state == 'q1' and not self.stack:
            return True
        else:
            return False

if __name__ == "__main__":
    while True:
        expression = input("Bir matematiksel ifade girin (çıkmak için 'q' tuşlayın): ")
        if expression.lower() == 'q':
            print("Program sonlandırıldı.")
            break
        pda = PDA()
        result = pda.process_input(expression)
        if result:
            print(f"İfade geçerli: {expression}")
        else:
            print(f"İfade geçersiz: {expression}")
