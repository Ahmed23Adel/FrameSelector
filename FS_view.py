from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from FS_tabs import *
import numpy as np
from matplotlib import cm
import cv2 
from moviepy.editor import *
import math


class View():

    def __init__(self, controller):    
        self.WIDTH = 1200; self.HEIGHT = 800
        self.root =Tk()
        self.root.title("(FS) Frame selector")
        self.root.iconbitmap(r"pics\logo.ico")
        self.root.geometry("1200x800")
        self.controller = controller
        self.fs_tabs = FS_tabs(self.WIDTH,self.HEIGHT, self.root)
        self.vid_img,self.label_vid_img,self.vid_capture = None, None, None
        self.root.filename = r'D:\Phones\phone\videos\ssa.mp4'
        self.play_btn, self.pause_btn = None, None
        self.design_all()

    def run(self):   
        self.root.mainloop()

    def get_root(self):
        return self.root

    def design_all(self):
        self.design_menu()
        self.design_video()
        self.design_control_btns()
        self.design_name_tab()

    def design_menu(self):
        self.menu = Menu(self.root)
        self.root.config(menu = self.menu)

        self.file_menu = Menu(self.menu)
        self.menu.add_cascade(label= "File", menu=self.file_menu)
        self.file_menu.add_command(label = "Import new video", command = lambda: self.controller.importNewVideo(self.root))


    def design_video(self):
        self.original_clip = VideoFileClip(self.root.filename) 
        self.clip = VideoFileClip(self.root.filename) 
        self.frames = self.clip.iter_frames()
        self.frame = next(self.frames)
        self.vid_img = ImageTk.PhotoImage(Image.fromarray(self.frame))
        self.label_vid_img = Label(self.fs_tabs.get_tab_fs(),image=self.vid_img, width = self.WIDTH, height = int((2/3)*self.HEIGHT), pady=20, padx=20)
        self.label_vid_img.grid(row = 0, column = 0, columnspan=14)
        self.controller.fps = int(math.ceil(self.clip.fps))



    def init_video_pic(self):
        self.design_video()


    def show_play(self):
        try:
            self.play_btn.destroy()
        except:
            pass
        self.play_btn=Button(self.fs_tabs.get_tab_fs(),  text= "Play",padx=40, pady=20, command = self.controller.play_btn)
        self.play_btn.grid(row=1, column=6,pady=0)
        try:
            self.pause_btn.destroy()
        except:
            pass

    def show_pause(self):
        try:
            self.play_btn.destroy()
            print("not pause")
        except:
            print("pass")
        self.pause_btn=Button(self.fs_tabs.get_tab_fs(),  text= "Pause",padx=40, pady=20, command = self.controller.pause_btn)
        self.pause_btn.grid(row=1, column=6,pady=0)
        
        


    def design_control_btns(self):
        self.last5Second_btn=Button(self.fs_tabs.get_tab_fs(),  text= "Last 5 second",padx=30, pady=20, command = self.controller.last5Second_btn)
        self.last5Second_btn.grid(row=1, column=0,pady=30)

        self.lasttSecond_btn=Button(self.fs_tabs.get_tab_fs(),  text= "Last second",padx=30, pady=20, command = self.controller.lastSecond_btn)
        self.lasttSecond_btn.grid(row=1, column=2,pady=30)

        self.lastFrame_btn=Button(self.fs_tabs.get_tab_fs(),  text= "Last Frame",padx=30, pady=20, command = self.controller.lastFrame_btn)
        self.lastFrame_btn.grid(row=1, column=4,pady=30)

        self.show_play()
        
        self.nextFrame_btn=Button(self.fs_tabs.get_tab_fs(),  text= "next Frame",padx=30, pady=20, command = self.controller.nextFrame_btn)
        self.nextFrame_btn.grid(row=1, column=8,pady=30)

        self.nextSecond_btn=Button(self.fs_tabs.get_tab_fs(),  text= "next second",padx=30, pady=20, command = self.controller.nextSecond_btn)
        self.nextSecond_btn.grid(row=1, column=10,pady=30)

        self.next5Second_btn=Button(self.fs_tabs.get_tab_fs(),  text= "next 5 second",padx=30, pady=20, command = self.controller.next5Second_btn)
        self.next5Second_btn.grid(row=1, column=12,pady=30)

        self.root.bind("j", self.controller.nextFrame_btn_event); self.fs_tabs.get_tab_fs().bind("J", self.controller.nextFrame_btn_event)
        self.root.bind("k", self.controller.nextSecond_btn_event); self.fs_tabs.get_tab_fs().bind("K", self.controller.nextSecond_btn_event)
        self.root.bind("l", self.controller.next5Second_btn_event); self.fs_tabs.get_tab_fs().bind("L", self.controller.next5Second_btn_event)
        
        self.root.bind("f", self.controller.lastFrame_btn_event); self.fs_tabs.get_tab_fs().bind("F", self.controller.lastFrame_btn_event)
        self.root.bind("d", self.controller.lastSecond_btn_event); self.fs_tabs.get_tab_fs().bind("D", self.controller.lastSecond_btn_event)
        self.root.bind("s", self.controller.last5Second_btn_event); self.fs_tabs.get_tab_fs().bind("S", self.controller.last5Second_btn_event)

        self.root.bind("c", self.controller.save_frame_event); self.fs_tabs.get_tab_fs().bind("C", self.controller.save_frame_event)

    def design_time(self):
        self.time_now = Label(self.fs_tabs.get_tab_fs(),text = "Current time in sec: ")
        self.time_now.grid(row=3, column = 4,pady=30)



        seconds = int(self.controller.current_fps // self.controller.fps)
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        self.time_label = Label(self.fs_tabs.get_tab_fs(),text = "%d:%02d:%02d" % (hour, minutes, seconds))
        self.time_label.grid(row=3, column = 5,pady=30)

        self.time_now = Label(self.fs_tabs.get_tab_fs(),text = "From: ")
        self.time_now.grid(row=3, column = 6,pady=30)


        self.time_label = Label(self.fs_tabs.get_tab_fs(),text = str(self.original_clip.duration))
        self.time_label.grid(row=3, column = 7,pady=30)


    def design_name_tab(self):
        self.name_label = Label(self.fs_tabs.get_tab_name(),text = "Name: ")
        self.name_label.grid(row=0, column = 1, pady = 30)
        self.name_entry = Entry(self.fs_tabs.get_tab_name(), width=50, fg='black')
        self.name_entry.grid(row=1, column = 1, pady = 30)
        self.name_button = Button(self.fs_tabs.get_tab_name(), text = "Submit", command = lambda: self.controller.submit_name(self.name_entry.get()))
        self.name_button.grid(row=2, column = 1, pady = 30)

        self.counter_label = Label(self.fs_tabs.get_tab_name(),text = "Start counter from: ")
        self.counter_label.grid(row=3, column = 1, pady = 30)
        self.counter_entry = Entry(self.fs_tabs.get_tab_name(), width=50, fg='black')
        self.counter_entry.grid(row=4, column = 1, pady = 30)
        self.couter_button = Button(self.fs_tabs.get_tab_name(), text = "Submit", command = lambda: self.controller.submit_counter(self.counter_entry.get()))
        self.couter_button.grid(row=5, column = 1, pady = 30)


