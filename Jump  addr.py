class CPU:
    def __init__(self):
        self.PC = 0
        
    def JMP(self, addr):
        self.PC = addr

cpu=CPU()
cpu.JMP(10)
print(f"PC after JMP: {cpu.PC}")

