def BEQ(self, r1, r2, addr):
    if self.registers[r1] == self.registers[r2]:
        self.PC = addr
        cpu.registers[1] = 5
        cpu.registers[2] = 5
        cpu.BEQ(1, 2, 20)
        print(f"PC after BEQ: {cpu.PC}")



