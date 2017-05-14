# -*- coding: utf-8 -*-
"""
Created on Sat May 13 22:49:40 2017

@author: njcx
"""
from Tkinter import *
import tkFont
import os
import sys
import urllib2
import sys
import platform

open_wifi_cmd = "netsh wlan start hostednetwork"
close_wifi_cmd = "netsh wlan stop hostednetwork"
message = ''

def show_result(how, cmd):
    global message
    result = os.system(cmd)
    if result != 0:
        if how == 1:
            message.set("连接外网成功,重启浏览器,请使用https访问外网")
        else:
            message.set("")
    else:
        if how == 1:
            message.set("还原成功")
        else:
            message.set("")
        
def cnt():
    cmd = open_wifi_cmd
    show_result(1, cmd)

def back():
    cmd = close_wifi_cmd
    show_result(0, cmd)
    
def main():
    
    root = Toplevel()
    root.title("网络助手_njcx");
    #root.geometry('600x400')
    global message
    message = StringVar()
    message.set("一次连接,永久使用",)
    
    ft = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)
    bm = PhotoImage(file='/home/njcx/timg.gif')
    label = Label(root, image=bm)
    label.grid(row=0, columnspan=2)

    open_button = Button(root, text="连接", font=ft,  pady=5, width=10, borderwidth=2, bg="#F3E9CC", command=open_wifi)
    open_button.grid(row=1, column=0)

    close_button = Button(root, text="还原", font=ft, pady=5, width=10, borderwidth=2, bg="#F3E9CC", command=close_wifi)
    close_button.grid(row=1, column=1)

    status_message = Message(root, textvariable=message, pady=5, width=250)
    status_message.grid(row=2, columnspan=2)
    
    root.mainloop()
    
if __name__ == '__main__':
    main()



