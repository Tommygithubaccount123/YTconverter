import tkinter as tk
import converter
class ConverterWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Converter')
        window_width = 300
        window_height = 200
        
        #center screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


if __name__ == "__main__":
    window1 = ConverterWindow()
    window1.mainloop()