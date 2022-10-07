from tkinter import ttk

class FS_tabs():
    def __init__(self, width, height, root):
        self.root = root
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=15)
        self.tab_fs = ttk.Frame(self.notebook, width = width, height = height)
        self.tab_transorms = ttk.Frame(self.notebook, width = width, height = height)
        self.tab_name = ttk.Frame(self.notebook, width = width, height = height)
        
        self.tab_fs.pack(fill="both", expand=1)
        self.tab_transorms.pack(fill="both", expand=1)
        self.tab_name.pack(fill="both", expand=1)

        self.notebook.add(self.tab_fs, text = "Frame selector")
        self.notebook.add(self.tab_transorms, text = "transorms")
        self.notebook.add(self.tab_name, text = "name")

    def get_tab_fs(self):
        return self.tab_fs

    def get_tab_transorms(self):
        return self.tab_transorms

    def get_tab_name(self):
        return self.tab_name

