# Bilogger 铋日志 一个简洁好用的log工具
&copy; BiNb9O3 Stdio 2022
##主体部分
**导入：**
下载Bilogger.py文件到你的项目目录，并在项目文件中导入Bilogger
>import Bilogger as bl

介绍文件中所有Bilogger会以bl出现

**information_and_copyright函数在调用后会输出有关本工具的信息 **
>bl.information_and_copyright()

**settingDefault函数在调用后会修改日日志器的设置**

示例: 
time=1  控制输出日志时是否输出时间
type="INFO"  输出日志时的日志类型
message="Default Message"  日志默认信息，如果调用日志器什么都不传入的话会输出此信息
speaker="Test Thread"输出日志的线程
speaker_display=1  控制输出日志时是否输出调用线程信息
type_display=1  控制输出日志时是否输出类型
color 控制颜色
>bl.settingDefault(time=1,
type="INFO",
message="Default Message",
speaker="Test Thread",
speaker_display=1,
type_display=1,
color="red")

**此时再输出设置：**
>print(bl.logger_setting)
{'time': 1, 'speaker_display': 1, 'type_display': 1, 'type': 'INFO', 'message': 'Default Message', 'speaker': 'Test Thread', 'color': 'red'}

**如果什么参数都不带，则会回到默认设置：**
>bl.settingDefault() 

**此时再输出设置：**
>print(bl.logger_setting) {'time': 1, 'speaker_display': 1, 'type_display': 1, 'type': 'INFO', 'message': 'No message input,please check the value of logger', 'speaker': 'Main Program', 'color': 'Normal'}

**logger**函数是日志器，传入参数时可以只传入message，color可以传入颜色（所有字母小写）：
- red:红色
- green:绿色
- Normal:白色
- yellow:黄色
- gw:绿色背景 白色文字

**其余参数来自于默认设置，所有输出的日志内容会被记录在logs列表内 不传入任何参数：**
>bl.logger() 

输出日志：
>[2022-12-01 12:20:30][INFO][Main Program]No message input,please check the value of logger

**也可以传入部分参数来修改日志内容:**
>bl.logger(time=0,speaker="Test Thread",message="Hello world!")

输出日志：
>[INFO][Test Thread]Hello world!

**outputlogs**函数会将所有日志信息存储到dir传参中的文件夹内，文件名为当前的时间，后缀名为filetype传参。

**filetype:无需“.” dir:只传入文件夹，不传入文件名！！！！！！！！！**

如果尝试写入失败，则会发出警告 
如果成功就会清空logs列表，从新开始记录 
> bl.outputLogs(dir="./logs",filetype="log")

**outputSettings**
函数可以导出本次Bilogger的设置，dir只传入文件夹！ 如果尝试写入失败，则会发出警告
> bl.outputSettings(dir="./settings")

**inputSettings**函数可以导入Bilogger设置，dir传入文件的路径。 如果尝试读取失败，则会发出警告
>bl.inputSettings(dir="./settings/BiloggerSettings.json")

##附带的小工具

**endl**函数名来源于C++库iostream中cout的用法，表示换行，调用后会输出转义字符\n 
> bl.endl()
