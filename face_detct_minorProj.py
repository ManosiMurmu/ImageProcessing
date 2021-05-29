# -*- coding: utf-8 -*-
"""
Created on Sun May  9 12:41:12 2021

@author: KIIT
"""
import cv2
from tkinter import * 

root=Tk()
root.eval('tk::PlaceWindow . center')
root.geometry("500x500")



Cblind_label = Label(root, text = 'FACE DETECTION', font=('calibre',10, 'bold'))
C_entry = Entry(root,textvariable = blind_var, font=('calibre',10,'normal'))
sub_btn=Button(root,text = 'Start', command = start)
sub_btn1=Button(root,text = 'Stop', command = stop)

Cblind_label.grid(row=0,column=0)
C_entry.grid(row=0,column=1)
sub_btn.grid(row=1,column=1)
sub_btn1.grid(row=1,column=2)
