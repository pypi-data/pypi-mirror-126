import socket
# import subprocess
import threading
import time

from Locker_Project import Func

data = ''
lstip = []


class Producer(threading.Thread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(60)

    def __init__(self, Cmd, condition, host, Port, exitEvent, lstthreadStop):
        threading.Thread.__init__(self)
        self.Cmd = Cmd
        self.condition = condition
        self.host = host
        self.Port = Port
        self._Exit = exitEvent
        self.lstThread = lstthreadStop

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
        check = False
        self.sock.connect((self.Host, self.Port))
        threadmain = '<id>121</id><type>socket</type><data>main</data>'
        threadmain = threadmain.encode('utf-8')
        size = len(threadmain)
        self.sock.sendall(size.to_bytes(4, byteorder='big'))
        self.sock.sendall(threadmain)
        time.sleep(1)
        while 1:
            time.sleep(0.5)
            try:
                if self._Exit.is_set():
                    break
                while 1:
                    if self._Exit.is_set():
                        break
                    full_msg = ''
                    Dta = self.sock.recv(1024)

                    if len(Dta) > 0:
                        full_msg += Dta.decode('utf-8')

                    if 1024 >= len(Dta) > 0:
                        Dta = full_msg.split(";")
                        if Dta[1].split("\n")[0] is 'Update':
                            print('vao chuong trinh update')
                            if Func.is_connected():
                                exit_event = threading.Event()
                                exit_event.set()
                                self._Exit.set()
                                print('Chương trinh dang update....')
                                t1 = threading.Thread(target=Func.Update())
                                t1.start()
                                self.sock.close()
                            else:
                                print('Vui Long Kiem Tra Ket Noi internet. Thu Lai...')
                        self.condition.acquire()
                        self.Cmd.append(full_msg.split("\n")[0])
                        self.condition.notify()
                        self.condition.release()
                        pass
                    full_msg = ''
                    if len(Dta) == 0:
                        self.sock.close()
                        check = True
                    time.sleep(0.1)
                    pass
            except Exception as e:
                try:
                    lstIp = Func.get_default_gateway_linux()
                    for i in lstIp:
                        if i == self.Host:
                            break
                        self.Host = i
                        check = True
                        try:
                            with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as Sk:
                                Sk.settimeout(5)
                                Sk.connect((self.Host, self.Port))
                                Sk.close()
                                print('tim ra host=', self.Host)
                                Sk.close()
                                for t in self.lstThread:
                                    t.Host = self.Host
                        except Exception as e:
                            print(str(e))
                    lstIp.clear()
                    if check:
                        self.sock.close()
                        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.sock.settimeout(60)
                        try:
                            self.sock.connect((self.Host, self.Port))
                            print('Connected')
                            threadmain = '<id>121</id><type>socket</type><data>main</data>'
                            threadmain = threadmain.encode('utf-8')
                            size = len(threadmain)
                            self.sock.sendall(size.to_bytes(4, byteorder='big'))
                            self.sock.sendall(threadmain)
                            check = False

                        except Exception as e:
                            print('Mat ket noi', str(e))
                            check = True
                            self.sock.close()

                except Exception as e:
                    print(str(e))
                    check = True
                    self.sock.close()
                    continue

    # def __del__(self):
    #     print('Doi tuong preducer bi xoa')
