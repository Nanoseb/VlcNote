#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telnetlib
import time
import re
import vim 


def int2time(inttime):
    hours = int(inttime/3600)
    minutes = int((inttime - hours*3600)/60)
    secondes = inttime - hours*3600 - minutes*60
    return '{num:02d}'.format(num=hours) + ":" + '{num:02d}'.format(num=minutes) + ":" + '{num:02d}'.format(num=secondes) + " -- "


def time2int(time):
    [ hours, minutes, secondes] = time.split(':') 
    return int(hours)*3600 + int(minutes)*60 + int(secondes)



class VlcNote:
    def __init__(self, port="4212", host="127.0.0.1", password="passwordVLC"):
        self.telnet = telnetlib.Telnet()
        self.telnet.open(host, port, 2)
        telnet_running = self.telnet.read_until(b"Password: ", timeout=2)
        self.telnet.write(bytes(password))
        self.telnet.write(b"\n")


    def pause(self):
        self.telnet.write(b"pause")
        self.telnet.write(b"\n")


    def get_timestamp(self):
        self.telnet.write(b"get_time")
        self.telnet.write(b"\n") 
        time.sleep(0.2)
        raw_timestamp = self.telnet.read_eager().split(b'\n')[-2]
        timestamp = int(re.sub(r"\D", "", str(raw_timestamp)))

        return timestamp

    def write_timestamp(self):
        try:
            timestamp = self.get_timestamp()
            timestamp_format = int2time(timestamp)
        except:
            return
        vim.current.line = timestamp_format + vim.current.line

    def goto_timestamp(self):
        try:
            timestamp_format = re.sub(" -- .*", "", vim.current.line)
            timestamp = time2int(timestamp_format)
        except:
            return
        self.telnet.write(b"goto 1")
        self.telnet.write(b"\n") 
        time.sleep(0.3)

        self.telnet.write(b"seek ")
        self.telnet.write(bytes(timestamp))
        self.telnet.write(b'\n')
        
    def logout(self):
        time.sleep(0.3)
        self.telnet.write(b"logout\n")
