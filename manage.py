import os
from app import create_app
from flask_script import Manager, Shell
import logging
import logging.handlers
from logging.handlers import TimedRotatingFileHandler

import time

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


def create_log():
    log = logging.getLogger('pro.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s %(filename)s %(funcName)s %(lineno)d %(process)d ')  # 每行日志的前缀设置
    fileTimeHandler = TimedRotatingFileHandler('pro.log', "D", 1, 30)
    fileTimeHandler.suffix = "%Y%m%d-%H%M.log"  # 设置 切分后日志文件名的时间格式 默认 filename+"." + suffix 如果需要更改需要改logging 源码
    fileTimeHandler.setFormatter(formatter)
    fileTimeHandler.setLevel(logging.DEBUG)
    fileTimeHandler.mode = 'a'
    logging.basicConfig(level=logging.DEBUG)
    fileTimeHandler.setFormatter(formatter)
    log.addHandler(fileTimeHandler)


if __name__ == '__main__':

    manager.run()
