from pyzbar.pyzbar import decode
import cv2
import pyautogui


class getCode:
    def qrCode():
        cam = cv2.VideoCapture(0)
        cam.set(3,640)
        cam.set(4,480)

        while True:
            success, img = cam.read()
            
            for barcode in decode(img):
                code = barcode.data.decode('utf-8')
                return code
            
            cv2.imshow('Result',img)
            cv2.waitKey(1)

class verification:
    def __init__(self, code):
        self.code = code

    def check(self):
        # Insert your the andress of directory
        with open('C:/#/idCardCode.txt', mode='r') as r:
            employees = r.read().splitlines()
            checking = [self.code if str(self.code) in employees else 'error']
            for employee in checking:
                return employee

class openTool:
    def excel():
        pyautogui.hotkey('win','r')
        pyautogui.write('excel')
        pyautogui.press('enter')

    def gmail():
        pyautogui.hotkey('win','r')
        pyautogui.write('https://www.google.com/intl/pt-BR/gmail/about/')
        pyautogui.press('enter')

    def outlook():
        pyautogui.hotkey('win','r')
        pyautogui.write('https://outlook.live.com/')
        pyautogui.press('enter')


if __name__ == '__main__':
    pass