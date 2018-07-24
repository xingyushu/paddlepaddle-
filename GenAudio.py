#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
# 
# Copyright (c) 2017 aibot.me, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: gen_wav.py
Date: 2017/03/24 12:36:27
Brief: 通过麦克风录音 生成 wav文件
"""

import os
import sys
import wave
import numpy as np 
from datetime import datetime
from pyaudio import PyAudio, paInt16



class GenAudio(object):
    def __init__(self):
        self.num_samples = 2000    #pyaudio内置缓冲大小
        self.sampling_rate = 8000  #取样频率
        self.level = 1500          #声音保存的阈值
        self.count_num = 20        #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.save_length = 8       #声音记录的最小长度：save_length * num_samples 个取样
        self.time_count = 30        #录音时间，单位s
        self.voice_string = []

    
    #保存文件
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(self.sampling_rate) 
        wf.writeframes(np.array(self.voice_string).tostring())
        wf.close()
    
    
    def read_audio(self):
        pa = PyAudio() 
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate, input=True, 
                frames_per_buffer=self.num_samples) 
        
        save_count = 0
        save_buffer = [] 
        time_count = self.time_count

        while True:
            time_count -= 1
            
            # 读入num_samples个取样
            string_audio_data = stream.read(self.num_samples)     
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype = np.short)
            #计算大于 level 的取样的个数
            large_sample_count = np.sum(audio_data > self.level)
            
            print(np.max(audio_data)),  "large_sample_count=>", large_sample_count

            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                save_count = self.save_length
            else: 
                save_count -= 1
            if save_count < 0:
                save_count = 0
            
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = [] 
                    print("Recode a piece of  voice successfully!")
                    return True
            
            if time_count == 0: 
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False
        return True




if __name__ == "__main__":
    r = GenAudio()
    r.read_audio()
    r.save_wav("./test.wav")
