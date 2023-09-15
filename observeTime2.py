import datetime
import os
import time

# 指定要监测的文件路径
file_path = "./video2/multidash.mpd"
log_file_path = "./video2/log.txt"  # 日志文件路径

# 定义一个函数来检测文件是否存在并记录时间
def monitor_file_creation(file_path):
    while True:
        if os.path.exists(file_path):
            # 文件已创建，获取当前时间，包括毫秒
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            
            # 检查日志文件是否存在，如果不存在则创建它
            if not os.path.exists(log_file_path):
                with open(log_file_path, "w") as log_file:
                    pass
            
            # 记录时间到日志文件
            with open(log_file_path, "w") as log_file:
                log_file.write(f"File created at: {current_time}\n")
            
            print(f"File created at: {current_time}")
            break
        else:
            # 文件尚未创建，等待一段时间后再次检查
            time.sleep(0.1)

if __name__ == "__main__":
    monitor_file_creation(file_path)