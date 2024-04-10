class ColorScheme:
    def __init__(self):
        self.bg_color = "#dee2e6"
        self.bg_offset = "#ced4da"
        self.primary = "#275d38"
        self.secondary = "#416f4f"
        self.white = "#ffffff"
        self.black = "#000000"
        self.title = "#275d38"
        self.font1 = "#000000"
        self.font2 = "#ffffff"
    
    def set_color_scheme_custom(self, primary : str, secondary : str):
        self.primary = primary
        self.secondary = secondary

    def set_color_scheme_dark(self):
        self.bg_color = "#275d38"
        self.bg_offset = "#416f4f"
        self.primary = self.white
        self.secondary = "#ced4da"
        self.font1 = self.white
        self.font2 = self.black

    def reset_to_default(self):
        self.bg_color = "#dee2e6"
        self.bg_offset = "#ced4da"
        self.primary = "#275d38"
        self.secondary = "#416f4f"