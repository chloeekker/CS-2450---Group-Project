class ColorScheme:
    def __init__(self):
        self.font : str = None
        self.border : str = None

    def default(self):
        self.font = "#275d38"
        self.border = "#a7a8aa"
    
    def gray_scale(self):
        self.font = "#000000"
        self.border = "#4d4d4d"

    def custom(self, primary : str, secondary : str):
        self.font = primary
        self.border = secondary

    def get_font(self):
        return self.font
    
    def get_border(self):
        return self.border