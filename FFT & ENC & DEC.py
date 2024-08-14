import numpy as np
from scipy.fft import fft, ifft

class CPU:
    def __init__(self, memory_size=256):
        self.registers = [0] * 8  
        self.memory = [0] * memory_size  

    def FFT(self, r1, r2):
        
        data_start = self.memory[r2]  
        data = np.array(self.memory[data_start:data_start + 8])  
        result = fft(data)
        result_addr = self.registers[r1]
        self.memory[result_addr:result_addr + len(result)] = result.real.astype(int).tolist()  
    
    def ENC(self, r1, r2):
        """Encrypt the data starting at address r2, and store the result at the location pointed to by r1."""
        data_start = self.memory[r2]
        data = self.memory[data_start:data_start + 8]  # Example: 8 bytes of data
        encrypted_data = self.encrypt(data)
        result_addr = self.registers[r1]
        self.memory[result_addr:result_addr + len(encrypted_data)] = encrypted_data
    
    def DEC(self, r1, r2):
        data_start = self.memory[r2]
        encrypted_data = self.memory[data_start:data_start + 8]  
        result_addr = self.registers[r1]
        self.memory[result_addr:result_addr + len(decrypted_data)] = decrypted_data
    
    def encrypt(self, data):
        return [byte ^ 0xFF for byte in data]  
    
    def decrypt(self, data):
        return [byte ^ 0xFF for byte in data] 

cpu = CPU()
cpu.memory[50:58] = [1, 2, 3, 4, 5, 6, 7, 8]  

cpu.registers[1] = 100  
cpu.registers[2] = 50   ]
cpu.FFT(1, 2)
print(f"Memory after FFT at address 100: {cpu.memory[100:108]}")

cpu.registers[1] = 150  
cpu.ENC(1, 2)
print(f"Memory after ENC at address 150: {cpu.memory[150:158]}")

cpu.registers[1] = 200  
cpu.registers[2] = 150  
cpu.DEC(1, 2)
print(f"Memory after DEC at address 200: {cpu.memory[200:208]}")
