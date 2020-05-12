class Interpreter:
    def __init__(self, channel = 0, tapeLength = -1, wordLength = 8, allowInput = False):
        self.channel = channel
        self.tapeLength = tapeLength
        self.wordLength = wordLength
        self.allowDynamicInput = allowInput

    def Interpret(self, code, inp = ""):
        #define Interpreter Values
        memory, memPtr, curr, inPtr, out = [0], 0, 0, 0, ""
        #begin Interpreter event loop
        while True:
            if curr == len(code):   #end interpreter/event loop when there are no more commands
                break
            #read the next command from the code
            command = code[curr]
            print(command)
            if command == ">":      #increment pointer
                memPtr += 1
                if memPtr >= len(memory):
                    memory.append(0)
                if self.tapeLength != -1:   #if tape not configured infinite wrap pointer
                    memPtr = memPtr%self.tapeLength
            elif command == "<":    #decrement pointer
                memPtr -= 1
                if self.tapeLength != -1:   #if tape not infinte wrap pointer
                    memPtr = memPtr%self.tapeLength
                elif memPtr < 0: memPtr = 0     #if infinite keep pointer at 0
            elif command == "+":    #Increment value in memory
                if self.wordLength != -1:   #if word length not infinite wrap word
                    memory[memPtr] = (memory[memPtr]+1)%(2**self.wordLength)
                else:
                    memory[memPtr] += 1
            elif command == "-":    #decrement value in memory
                if self.wordLength != -1:   #if word length not infinite wrap word
                    memory[memPtr] = (memory[memPtr]-1)%(2**self.wordLength)
                else:
                    memory[memPtr] -= 1
            elif command == ".":    #add current memory value to output buffer
                out += chr(memory[memPtr])
            elif command == ",":    #read character from input buffer if there is any and increment inPtr
                if not self.allowDynamicInput:
                    if inPtr != len(inp):
                        memory[memPtr] = inp[inPtr]
                        inPtr += 1
                else:
                    if inPtr != len(inp):
                        memory[memPtr] = inp[inPtr]
                        inPtr += 1
                    else:
                        input("waiting for input: ")
            elif command == "[":    #begin loop
                if memory[memPtr] == 0: #check if value at memory is 0 and if so end loop
                    numBraces = 1   #counter for nested loop compatibility
                    while not (code[curr] == ']' and numBraces == 0):
                        curr += 1
                        if code[curr] == '[': numBraces += 1
                        elif code[curr] == ']': numBraces -= 1
            elif command == "]":    #end of loop check
                if memory[memPtr] != 0: #if value at memory is not 0 jump back to start of loop
                    numBraces = 1   #counter for nested loop compatibility
                    while not (code[curr] == '[' and numBraces == 0):
                        curr -= 1
                        if code[curr] == ']': numBraces += 1
                        elif code[curr] == '[': numBraces -= 1
            curr += 1

        return out #return output buffer after interpreter completes
