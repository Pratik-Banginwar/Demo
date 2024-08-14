class CPU:
    def __init__(self, memory_size=256):
        self.registers = [0] * 8  
        self.PC = 0  
        self.SP = memory_size - 1  
        self.stack = [0] * memory_size  
        self.memory = [0] * memory_size

    def CALL(self, addr):
        self.stack[self.SP] = self.PC + 1  
        self.SP -= 1  
        self.PC = addr
    
    def RET(self):
         self.SP += 1
         self.PC = self.stack[self.SP]
   
    

cpu=CPU()

cpu.CALL(30)
print(f"PC after CALL: {cpu.PC}, SP: {cpu.SP}")

cpu.RET()
print(f"PC after RET: {cpu.PC}, SP: {cpu.SP}") 
    
