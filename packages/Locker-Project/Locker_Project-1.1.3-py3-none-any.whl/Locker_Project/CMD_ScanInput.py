import threading
import time
from datetime import datetime
from Locker_Project import Func


class ScanInput(threading.Thread):
    tinhieuchot = False
    def __init__(self, lstinput, lstlock, lstID, exitEvent, input1, input2, output1, output2):
        threading.Thread.__init__(self)
        self.lstinput = lstinput
        self.lstlock = lstlock
        self.lstId = lstID
        self._Exit = exitEvent
        self._Input1 = input1
        self._Input2 = input2
        self._Output1 = output1
        self._Output2 = output2
        self.host = ''

    @property
    def Exit(self):
        return self._Exit

    @Exit.setter
    def Exit(self, exitEvent):
        self._Exit = exitEvent

    @property
    def Host(self):
        return self.host

    @Host.setter
    def Host(self, host):
        self.host = host

    def run(self):
        while 1:
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            if dt_string == '23:58:00':
                Func.restart()
            print(dt_string)
            if self._Exit.is_set():
                # self._blynk.notify('Thread Scan input Stop')
                break
            try:
                for i in self.lstId:
                    if self._Exit.is_set():
                        break
                    self.lstlock.acquire()
                    if int(i) > 16 and self.lstinput[i] == 0:
                        if self._Input2[int(i) - 17].value == self.tinhieuchot:
                            pass
                            # self._Output2[int(i)-17].value=True
                            # time.sleep(1)
                            # self._Output2[int(i)-17].value=False
                    elif self.lstinput[i] == 0:
                        if self._Input1[int(i) - 1].value == self.tinhieuchot:
                            pass
                            # self._Output1[int(i)-1].value=True
                            # time.sleep(1)
                            # self._Output1[int(i)-1].value=False
                    self.lstlock.release()
                    time.sleep(1)

            except Exception as e:
                print('ScanInput Error: ', str(e))
                continue
