logs=[]
import json
import time as ti
import colorama
colorama.init(wrap=True,autoreset=True)
logger_setting={"time":1,
                "speaker_display":1,
                "type_display":1,
                "type":"INFO",
                "message":'No message input,please check the value of logger',
                "speaker":"Main Program",
                "color":"Normal"}
def endl():
    print("\n")

def information_and_copyright():
    name="Bilogger 铋日志"
    describe="一个简洁的log工具"
    copyright="Bi2Nb9O3"
    version="V0.0.3"
    print(f"===================={name}====================\nVersion:{version}\nDescribe:{describe}\nCopyright:{copyright} All copyright reserve",end="\n")

def settingDefault(time=1,
                   type="INFO",
                   message="No message input,please check the value of logger",
                   speaker="Main Program",
                   speaker_display=1,
                   type_display=1,
                   color="Normal"):
    logger_setting["time"]=time
    logger_setting["type"]=type
    logger_setting["message"]=message
    logger_setting["speaker"]=speaker
    logger_setting["speaker_display"]=speaker_display
    logger_setting["type_display"]=type_display
    logger_setting["color"]=color

def logger(time=logger_setting["time"],
            type=logger_setting["type"],
            message=logger_setting["message"],
            speaker=logger_setting["speaker"],
            speaker_display=logger_setting["speaker_display"],
            type_display=logger_setting["type_display"],
            color=logger_setting["color"]):
    global logs,ti
    t=ti.gmtime()
    gt=ti.strftime("%Y-%m-%d %H:%M:%S",t)
    logt=""
    if time:
        logt+=f'[{gt}]'
    if type_display:
        logt+=f"[{type}]"
    if speaker_display:
        logt+=f"[{speaker}]"
    if color=="Normal":
        ocolor=colorama.Fore.WHITE
    elif color=="red":
        ocolor=colorama.Fore.RED
    elif color=="green":
        ocolor=colorama.Fore.GREEN
    elif color=="yellow":
        ocolor=colorama.Fore.YELLOW
    elif color=="gw":
        ocolor=colorama.Fore.WHITE+colorama.Back.GREEN
    logt+=message
    print(ocolor+logt+colorama.Fore.RESET)
    logs.append(logt)

def outputLogs(dir,filetype):
    t=ti.gmtime()
    gt=ti.strftime("%Y_%m_%d_%H_%M_%S",t)
    try:
        with open(file=dir+'/'+gt+'.'+filetype,mode="w+") as f:
            for i in logs:
                f.write(i+"\n")
        logger(time=1,type="INFO",message="Log file created successfully!",speaker="Logger Thread",color="gw")
        logs.clear()
    except:
        logger(time=1,type="ERROR",message="Log file created unsuccessfully!Please check!",speaker="Logger Thread",color="red")
def outputSettings(dir):
    global logger_setting
    try:
        result=json.dumps(logger_setting,ensure_ascii=False)
        with open(dir+"/BiloggerSettings.json",mode="w+",encoding="UTF-8") as f:
            f.write(result)
        logger(type="INFO",message="Setting File created successfully!",speaker="Logger Thread",color="gw")
    except:
        logger(type="ERROR",message="Setting File created unsuccessfully!Please check!",speaker="Logger Thread",color="red")
def inputSettings(dir):
    try:
        with open(dir,mode="r",encoding="UTF-8") as f:
            logger_setting=json.load(f)
        logger(type="INFO",message="Setting File read successfully!",speaker="Logger Thread",color="gw")
    except:
        logger(type="ERROR",message="Setting File read unsuccessfully!Please check!",speaker="Logger Thread",color="red")
