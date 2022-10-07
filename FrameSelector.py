from tkinter import *
from PIL import ImageTk, Image
from FS_view import  *
from FS_controller import *

controller = Controller()
view = View(controller)
controller.set_view(view)
view.run()