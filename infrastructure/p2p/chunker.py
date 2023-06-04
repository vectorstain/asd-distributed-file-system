# File to open and break apart
def chunk_file (filename):
    
    fileR = open(filename, "rb")
    
    chunk = 0
    
    byte = fileR.read(1024)
    while byte:
    
        # Open a temporary file and write a chunk of bytes
        fileN = "./chunked/chunk" + str(chunk) + "_" + filename
        fileT = open(fileN, "wb")
        fileT.write(byte)
        fileT.close()
        
        # Read next 1024 bytes
        byte = fileR.read(1024)
    
        chunk += 1
    
    return chunk-1