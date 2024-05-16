import socket
import threading
import json



try:
    DICTIONARY_FILE = open("dictionary.json", 'r').read()
    dictionary = json.loads(DICTIONARY_FILE)

except FileNotFoundError:
    print("File not found.")


# Thread function to handle client requests
def threads_c(c_socket):   
    try:
        
        data = c_socket.recv(1024)
        if not data:
            raise Exception("No data received.")


        word = data.decode().strip() #strip method used to remove white spaces
        c_socket.send(dictionary[word].encode()) 

    except Exception as e:
        print("Error occurred: " + str(e))

    finally:
        
        c_socket.close()      


s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  



address = ('localhost', 11111)   #IP & port number
s_socket.bind(("localhost", 11111))    
s_socket.listen()                       

print('Server started on ' + str(address[0]) + ':' + str(address[1]))



while True:
    try:

        c_socket, address = s_socket.accept()        
        print('Client connected from ' + str(address[0]) + ':' + str(address[1]))
        
        thread = threading.Thread(target=threads_c, args=(c_socket,)) 
        thread.start() 


    except Exception as e:
        print('Error occurred: ' + str(e))
