from tkinter import Tk, ttk, W

class UI:
    def __init__(self, root):
        self._root = root
   

    def handle_button_click(self,event):
        print("button clicked", event)
        
        name = self.name.get()
        username= self.username.get()
        password = self.password.get()

        print(name, username, password)



    def start(self):
        heading = ttk.Label(master=self._root, text="Register", foreground="white",  background="black")

        name = ttk.Label(master=self._root, text="Name")
        self.name = ttk.Entry(master=self._root)

        username = ttk.Label(master=self._root, text="Username")
        self.username = ttk.Entry(master=self._root)

        password = ttk.Label(master=self._root, text="Password")
        self.password = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="REGISTER")

        heading.grid(row=0, column=0, columnspan=2, sticky =W)
    
        name.grid(row =1, column=0)
        self.name.grid(row=1, column =1)

        username.grid(row=3, column=0)
        self.username.grid(row=3, column=1)

        password.grid(row=5, column=0)
        self.password.grid(row=5, column=1)

        button.grid(row=7, column=0, columnspan=2)
        
        self._root.grid_columnconfigure(1, weight=1)
        button.bind("<Button-1>", self.handle_button_click)