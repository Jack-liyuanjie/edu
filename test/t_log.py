import logging
from logging import StreamHandler, FileHandler
from logging.handlers import HTTPHandler
from logging import Formatter

logger = logging.getLogger('edu_api')


def config_log():
    fmt = Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    iohandler = StreamHandler()
    iohandler.setLevel(logging.DEBUG)
    iohandler.setFormatter(fmt)

    # 文件日志处理器
    file_handler = FileHandler('edu.log')
    file_handler.setLevel(logging.WARN)
    file_handler.setFormatter(fmt)

    # 服务器端口处理日志
    http_handler = HTTPHandler(host='localhost:5000',
                               url='/log',
                               method='POST')
    http_handler.setLevel(logging.ERROR)
    http_handler.setFormatter(fmt)  # 上传的数据不需要fmt格式

    logger.setLevel(logging.DEBUG)
    logger.addHandler(iohandler)
    logger.addHandler(file_handler)
    logger.addHandler(http_handler)



config_log()
logger.info('您好，我是sb')
logger.warning('余额不足，快充值')
logger.error('服务器炸了')
logger.critical('端口被打')
