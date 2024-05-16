import tkinter as tk  #used for graphics
import socket
from turtle import color



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Dictionary Client")
        self.master.geometry("400x300")
        self.master.resizable(True, True)
        self.create_widgets()


    def create_widgets(self):

        definition_frame = tk.Frame(self.master)
        definition_frame.pack(pady=10)

        self.definition_label = tk.Text(definition_frame, font=("Arial", 14), wrap=tk.WORD, bg="#f0f0f0", relief="sunken", borderwidth=3)
        self.definition_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        
        scrollbar = tk.Scrollbar(definition_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        
        self.word_entry = tk.Entry(self.master, font=("Arial", 14), fg="red")
        self.word_entry.pack(pady=10)

        word_label = tk.Label(self.master, text="Enter a word:", font=("Arial", 14))
        word_label.pack()

        submit_button = tk.Button(self.master, text="Submit", font=("Arial", 14) ,command=self.send_word)
        submit_button.pack(pady=10)

        scrollbar.config(command=self.definition_label.yview)



    def send_word(self):
        word = self.word_entry.get()

       
        c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c_socket.connect(("localhost", 11111))
        c_socket.send(word.encode())

        
        definition = c_socket.recv(1024).decode()

        # Update the definition label
        self.definition_label.delete(1.0, tk.END)
        self.definition_label.insert(tk.END, definition)

      
        c_socket.close()



root = tk.Tk()
app = Application(master=root)
app.mainloop()
