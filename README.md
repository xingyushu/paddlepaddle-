# paddlepaddle中译英机器翻译模型
the  undergraduate's  graduate  design,just for  reference,no joking
基于paddlepaddle框架和百度开放AI技术进行相关应用的测试和探究，开发的深度学习应用，设计了一个多功能机器翻译系统，能够实现文本翻译，也能录音、视频来源的语音识别和翻译功能，为AI翻译探索新场景应用提出了一定的思路。该系统不仅使用到了机器学习技术，也涉及到自然语言处理等方面的相关知识。  

1 使用paddlepaddle训练英译中模型，主要参考paddlepaddlebook给出的法英翻译模型 
2 使用百度语音识别和sphinx识别库识别中文和英文的语音，并且转化为文字，此外paddle也给有基于Deepspeech2开发的语音识别系统，可以参考继续开发  
3 使用百度语音合成接口将文字转为语音，使用ffmpeg处理音频和视频，使用pyqt开发界面
4 使用环境： ubuntu16.04+python2.7+paddle v2+pyqt5
5 使用：需要安装相应的依赖库，包括paddle环境，百度aip接口，sphinx,pyqt等一些库，入口文件为pro.py,“python pro.py”运行即可。
（1）文本翻译（中译英）
![1](https://github.com/xingyushu/paddlepaddlework/blob/master/%E6%96%87%E6%9C%AC%E7%BF%BB%E8%AF%91%E4%B8%AD%E8%AF%91%E8%8B%B1.png)

（2）输入视频文件识别

![2](https://github.com/xingyushu/paddlepaddlework/blob/master/%E8%A7%86%E9%A2%91%E8%AF%86%E5%88%AB.png)

![3](https://github.com/xingyushu/paddlepaddlework/blob/master/%E8%A7%86%E9%A2%91%E8%AF%86%E5%88%AB%E7%BB%93%E6%9E%9C2.png)


（3）其他：语音识别，输入语音识别，输入文本文档识别 都可以
