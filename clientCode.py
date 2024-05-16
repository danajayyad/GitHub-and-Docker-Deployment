import socket



c_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
c_socket.connect(("localhost", 11111)) 


word = input("Enter a word to get Its meaning: ")   
c_socket.send(word.encode()) 

print(c_socket.recv(1024).decode())


c_socket.close()   


input() 