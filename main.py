from classes import *
import time

code = getCode.qrCode()

if verification(code).check() == 'error':
    print('Not authorized')
else:
    print('Welcome to more a work day!!!')
    openTool.excel()
    time.sleep(3)
    openTool.gmail()
    time.sleep(3)
    openTool.outlook()