# logger对象的形式来操作日志文件

# 创建一个logger对象
# 创建一个文件管理操作符
# 创建一个屏幕管理操作符
# 创建一个日志输出的格式

# 文件管理操作符 绑定一个 格式
# 屏幕管理操作符 绑定一个 格式

# logger对象 绑定 文件管理操作符
# logger对象 绑定 屏幕管理操作符

import logging

# 创建一个logger对象
logger = logging.getLogger()
# 创建一个文件管理操作符
fh = logging.FileHandler('logger.log',encoding='utf-8')
# 创建一个屏幕管理操作符
sh = logging.StreamHandler()
# 创建一个日志输出的格式
format1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 文件管理操作符 绑定一个 格式
fh.setFormatter(format1)
# 屏幕管理操作符 绑定一个 格式
sh.setFormatter(format1)
logger.setLevel(logging.DEBUG)
# logger对象 绑定 文件管理操作符
logger.addHandler(fh)
# logger对象 绑定 屏幕管理操作符
logger.addHandler(sh)

logger.debug('debug message')      # 调试模式
logger.info('我的信息')        # 基础信息
logger.warning('warning message')  # 警告
logger.error('error message')      # 错误
logger.critical('critical message')# 严重错误
