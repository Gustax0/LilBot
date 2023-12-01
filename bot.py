import tkinter as tk
from tkinter import *
import time
import os

root = tk.Tk()


class App:
    def __init__(self):
        self.interface()
        root.bind("<KeyPress>", self.espaco)

    def interface(self):
        root.geometry("120x60")
        root.title("Botzinho")
        root.withdraw()

    def espaco(self, event):
        if event.keysym == "space":
            self.desligar()

    def tempo(self):
        while True:
            hora = time.localtime()
            if hora == 12 and hora.tm_min == 40 and hora.tm_sec == 0:
                self.desligar()
            time.sleep(1)

    def desligar(self):
        # Desligar o pc
        os.system('cmd /c "Shutdown -s -t 30')


if __name__ == "__main__":
    app = App()
    root.mainloop()
else:
    print("Algum erro foi detectado")
