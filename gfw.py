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
import platform

reload(sys)
sys.setdefaultencoding( "utf-8" )

open_unix = "sudo systemctl restart NetworkManager"
open_win = "ipconfig /flushdns"
open_mac = "sudo killall -HUP mDNSResponder"
win_host = "C:\Windows\System32\drivers\etc\hosts"
unix_host = "/etc/hosts"
message = ''
data = ''
sysstr=''
cmd =''


def download (url,numretries=5):
    global data
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
    request = urllib2.Request(url ,headers=headers)
    try:
        data = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        data = None
        if numretries >0:
            if hasattr(e,'code') and 500<= e.code<=600:
                return download(url,numretries-1)
    return data
    

def show_result(how, cmds):
    global message
    os.system(cmd)
    if how == 1:
            message.set("连接外网成功,重启浏览器,请使用https访问外网")
    else:
            message.set("还原成功")

def cnt():
    global sysstr
    global cmd
    sysstr = platform.system()
    if sysstr=="Windows":
        if os.path.exists(win_host+'.bak'):
            pass
        if os.path.exists(win_host):
            os.rename(win_host,win_host+'.bak')
        download("https://raw.githubusercontent.com/njcx/gfw-data/master/hosts_win.DAT")
        
        with open(win_host, 'w+') as f:
            f.write(data)
            f.close()
        cmd = open_win
        show_result(1, cmd)

    elif sysstr =="Linux":
        if os.path.exists(unix_host+'.bak'):
            pass
        if os.path.exists(unix_host):
            os.rename(unix_host,unix_host+'.bak')
        download("https://raw.githubusercontent.com/njcx/gfw-data/master/hosts_unix.DAT")
        
        with open(unix_host, 'w+') as f:
            f.write(data)
            f.close()
        cmd = open_unix
        show_result(1, cmd)
        
    else:
        if os.path.exists(unix_host+'.bak'):
            pass
        if os.path.exists(unix_host):
            os.rename(unix_host,unix_host+'.bak')
        download("https://raw.githubusercontent.com/njcx/gfw-data/master/hosts_win.DAT")
        
        with open('/etc/hosts', 'w+') as f:
            f.write(data)
            f.close()
        cmd = open_mac
        show_result(1, cmd)
        
def back():
    global sysstr
    if sysstr =="Windows":
        if os.path.exists(win_host+'.bak'):
            os.remove(win_host)
            os.rename(win_host+'.bak',win_host)
        else:
            pass
        cmd = "dir"
        show_result(0, cmd)
        
    elif(sysstr == "Linux"):
        if os.path.exists(unix_host+'.bak'):
            os.remove(unix_host)
            os.rename(unix_host+'.bak',unix_host)
        else:
            pass
        cmd = "dir"
        show_result(0, cmd)
    else:
        if os.path.exists(unix_host+'.bak'):
            os.remove(unix_host)
            os.rename(unix_host+'.bak',unix_host)
        else:
            pass
        cmd = "dir"
        show_result(0, cmd)
        
    
def main():
    root =Tk()  
    xx = Toplevel(root)
    root.title("网络助手_njcx");
    xx.geometry('0x0')
    global message
    message = StringVar()
    message.set("一次连接,永久使用",)
    
    ft = tkFont.Font(family="Arial", size=10, weight=tkFont.BOLD)
    bm = PhotoImage(file='./timg.gif')
    label = Label(root, image=bm)
    label.grid(row=0, columnspan=2)

    open_button = Button(root, text="连接", font=ft,  pady=5, width=10, borderwidth=2, bg="#F3E9CC", command=cnt)
    open_button.grid(row=1, column=0)

    close_button = Button(root, text="还原", font=ft, pady=5, width=10, borderwidth=2, bg="#F3E9CC", command=back)
    close_button.grid(row=1, column=1)

    status_message = Message(root, textvariable=message, pady=5, width=250)
    status_message.grid(row=2, columnspan=2)
    
    xx.mainloop()
    
if __name__ == '__main__':
    main()