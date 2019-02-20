
from . import api
import logging
from flask import current_app

@api.route("/index")
def index():
    # logging.error("xxx") # 错误级别
    # logging.warn("xxxx") # 警告级别
    # logging.info("xxx") # 消息提示级别
    # logging.debug("xxx") # 调试级别
    current_app.logger.error("error msg")
    current_app.logger.warn("warn msg")
    current_app.logger.info("info msg")
    current_app.logger.debug("debug msg")
    return "index page"