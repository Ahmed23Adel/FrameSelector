from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from matplotlib import cm
import cv2 
import time
import os
from tkinter import filedialog
import math

class Controller():
    def __init__(self):
        self.view = None
        self.start_time = 0
        self.start_frame = 0
        self.fps = 0
        self.current_fps = 0
        self.anime_name = ""
        self.counter = 0

    def set_view(self,view):
        self.view = view

    def importNewVideo(self,root):
        root.filename = filedialog.askopenfilename(initialdir = "/gui/images", title="Select a file", filetypes = (("all files","*.*"),("mov","*.mov"),("mp3","*.mp3"),("mp4","*.mp4")) )
        self.view.init_video_pic()
        

    def play_btn(self):
        self.view.show_pause()
        # while True:
        #     ret, frame = self.view.vid_capture.read()
        #     if ret == True:
        #         im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #         # self.view.vid_img = ImageTk.PhotoImage(Image.fromarray(im_rgb))
        #         # self.view.label_vid_img = Label(self.view.fs_tabs.get_tab_fs(),image=self.view.vid_img, width = self.view.WIDTH, height = int((2/3)*self.view.HEIGHT), pady=20, padx=20)
        #         # self.view.label_vid_img.grid(row = 0, column = 0, columnspan=14)
        #         # 20 is in milliseconds, try to increase the value, say 50 and observe
        #         key = cv2.waitKey(20)
                
        #         if key == ord('q'):
        #             break   
        #     else:
        #         break

    def pause_btn(self):
        self.view.show_play()

    def nextFrame_btn(self):
        self.view.frame = next(self.view.frames)
        self.view.vid_img = ImageTk.PhotoImage(Image.fromarray(self.view.frame))
        self.view.label_vid_img = Label(self.view.fs_tabs.get_tab_fs(),image=self.view.vid_img, width = self.view.WIDTH, height = int((2/3)*self.view.HEIGHT), pady=20, padx=20)
        self.view.label_vid_img.grid(row = 0, column = 0, columnspan=14)
        self.current_fps = self.current_fps +1 
        self.view.design_time()


    def load_frame(self):
        self.view.frame = next(self.view.frames)
        self.current_fps = self.current_fps +1 
    def lastFrame_btn(self):
        current_time = int((self.current_fps) // self.fps)
        old_fps_afterSec = int(self.current_fps - current_time * self.fps - 4)
        # print("current_time",current_time,"old_fps_afterSec",old_fps_afterSec,"current_fps",self.current_fps,"fps",self.fps)
        self.view.clip = self.view.original_clip.subclip(current_time, self.view.clip.end) 
        self.view.frames = self.view.clip.iter_frames()
        for _ in range(old_fps_afterSec):
            self.nextFrame_btn()
        self.current_fps = self.current_fps -1 
        self.view.design_time()

    def nextSecond_btn(self):
        current_time = self.current_fps // self.fps
        self.view.clip = self.view.original_clip.subclip(current_time+1, self.view.clip.end) 
        self.view.frames = self.view.clip.iter_frames()
        self.nextFrame_btn()
        self.current_fps = int(self.current_fps + self.fps)
        self.view.design_time()

    def lastSecond_btn(self):
        # print(self.current_fps,self.fps,self.current_fps // self.fps)
        current_time = self.current_fps // self.fps
        self.view.clip = self.view.original_clip.subclip(current_time-1, self.view.clip.end) 
        self.view.frames = self.view.clip.iter_frames()
        self.current_fps = int(self.current_fps - self.fps)
        self.nextFrame_btn()
        self.view.design_time()

    def next5Second_btn(self):
        current_time = self.current_fps // self.fps
        self.view.clip = self.view.original_clip.subclip(current_time+5, self.view.original_clip.end) 
        self.view.frames = self.view.clip.iter_frames()
        self.nextFrame_btn()
        self.current_fps = int(self.current_fps + self.fps*5)
        self.view.design_time()

    def last5Second_btn(self):
        # print(self.current_fps,self.fps,self.current_fps // self.fps)
        current_time = int(self.current_fps // self.fps)
        self.view.clip = self.view.original_clip.subclip(current_time-5, self.view.clip.end) 
        self.view.frames = self.view.clip.iter_frames()
        self.current_fps = int(self.current_fps - 5*self.fps)
        self.nextFrame_btn()
        self.view.design_time()


    def nextFrame_btn_event(self,event):
        self.nextFrame_btn()

    def nextSecond_btn_event(self,event):
        self.nextSecond_btn()

    def next5Second_btn_event(self,event):
        self.next5Second_btn()

    def lastFrame_btn_event(self,event):
        self.lastFrame_btn()

    def lastSecond_btn_event(self,event):
        self.lastSecond_btn()

    def last5Second_btn_event(self,event):
        self.last5Second_btn()

    def save_frame_event(self,event):
        self.save_frame()


    def submit_name(self,name):
        self.anime_name = name
        print(self.anime_name)

    def submit_counter(self, counter):
        self.counter = int(counter)

    def save_frame(self):
        im = Image.fromarray(self.view.frame) 
        im.save("./saved_pics/{}_{}.jpeg".format(self.anime_name,self.counter))
        self.counter = self.counter + 1