from logging import FileHandler
import logging
from flask import Flask
import settings
from flask.logging import default_handler

app = Flask(__name__)
app.config.from_object(settings.Dev)

# 删除原来的日志处理器
app.logger.removeHandler(default_handler)

# 添加日志处理器等级
app.logger.setLevel(logging.INFO)
# 文件日志处理器
fmt = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
file_handler = FileHandler('edu.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(fmt)

app.logger.addHandler(file_handler)
