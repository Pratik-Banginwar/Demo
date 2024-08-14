class CPU:
    def __init__(self, memory_size=256):
        self.registers = [0] * 8  
        self.memory = [0] * memory_size

    def LD(self, r1, addr):
        self.registers[r1] = self.memory[addr]

    def ST(self, addr, r1):
        self.memory[addr] = self.registers[r1]

cpu = CPU()
cpu.memory[100] = 44

cpu.LD(1, 100)
print(f"Register 1 after LD: {cpu.registers[1]}")

cpu.ST(200, 1)
print(f"Memory at address 200 after ST: {cpu.memory[200]}") 
