#!/usr/bin/env python
# Modified by Jonathan Liang @ 2015

from Tkinter import *
import os, glob, threading, socket, time, numpy
import cv2
import cv2.cv as cv
from PIL import Image, ImageTk
from optparse import OptionParser
# For debugging, we randomly drop the packets with certain probabilities
import random

#####   GLOBAL Variables #####
DEBUG = False    # Flag for debugging version
running_flag_send = True    # Flag to record sender status -- True:already sending
running_flag_receive = True # Flag to record receiver status -- True:already receiving
click_before = False        # Record whether click send before
receive_before = False      # Record whether click receive before
receive_not_stop = False
send_not_stop = False
client_lock = threading.Lock()
server_lock = threading.Lock()
##############################

UDP_PAYLOAD_SIZE = 1450

def string_to_hex_list(s):
    """ Map string to hex """
    return map(lambda x: hex(ord(x)), s)

class Client:
    """
    Client is used to send Video stream to server

    Attributes:
        server_host: Server's IP Address
        port: Destination port
        framesize: Frame size shown on UI, default=160*120
        fps: Frame per second, default=10
        send_speed: Calculation based on (frame_num * frame_size / send_time)
        send_size: True frame size for sending
    """
    def __init__(self,server_host="localhost",port=6123,framesize=(160,120),fps=10):
        """ Init the base class for all parameter """
        self.server_host = server_host
        self.port = port
        self.framesize = framesize
        self.fps = fps
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #sock: UDP socket to handle send and recv
        self.send_frame_num = 0     #send_frame_num: Total sent frame number
        self.send_speed = 0
        self.display_speed = 0
        self.send_size = (160,120)
        self.compression_rate = 20    #compression_rate: Based on zlib, frame will be compressed to save bandwidth
        self.pkt_seq = 0    #pkt_seq: Sequence number of packet

    def prepare_video(self,server_host="localhost",port=6123,send_size_x=160,send_size_y=120,send_fps=10,compress_rate=20):
        """ Prepare the video cpature class and set the parameters """
        self.server_host = server_host
        self.port = port
        self.send_size = (send_size_x,send_size_y)
        self.fps = send_fps
        self.compression_rate = compress_rate
        self.capture = cv2.VideoCapture(0)
        print "Video Cpaturing prepared with --",self.capture

        # Initial timer for software statistics
        self.timer = time.time()
        self.total_send_bytes = 0

        global click_before,send_not_stop
        click_before = True
        send_not_stop = True

    def reset_parameters(self,server_host, port, send_size_x, send_size_y, send_fps, compress_rate):
        """ Reset the parameters for new start """
        self.server_host = server_host
        self.port = port
        self.send_size = (send_size_x,send_size_y)
        self.fps = send_fps
        self.compression_rate = compress_rate
        self.pkt_seq = 0

    def connect(self):
        """ connect the remote Destination """
        global stop_flag
        while stop_flag:
            #set the framesize in the client side, size only for showing locally
            frame = self.get_frame(window_size=(640,480))

            #set the fps
            time.sleep(1/self.fps)

            self.send_frame(frame)

    def get_frame(self,resize_size=None,window_size=None):
        """ Get the capture and return it to the client IMMEDIATELY """
        success = False
        while not success:
          success, frame = self.capture.read()

        if not success:
            return

        if resize_size is None:
            resize_size = self.send_size
        if window_size is None:
            window_size=self.framesize

        resize_image = cv2.resize(frame,resize_size)
        window_size_image = cv2.resize(frame,window_size)
        jpegImg_window = window_size_image
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),self.compression_rate]
        ret, data = cv2.imencode('.jpg', resize_image, encode_param)

        return data,jpegImg_window

    def split_frame(self,frame,frame_size):
        """To splite the frame to fit the size of UDP packet and the frame size of underlayer

        Sequence number is needed to detect the corresponding sequence
        Note: I redesign the packet structure for storing extra status information

        Structure of the frame:(4 bytes for status header)
        pkt_seq | split_total_number | split_seq | frame_data ...
        split_total_number -- represent the total packets number of ONE frame after split
        split_seq -- the sequence number of each split packet in ONE frame

        Args:
            frame: the frame string that used to be split
            frame_size: the required size for each packet to send

        Returns:
            A frame_list that contains one/multiple frames by splitting input frame
        """
        frame_list = []
        split_total_number = len(frame) / frame_size
        split_seq = 0
        if len(frame) % frame_size == 0:
            split_total_number = split_total_number - 1

        if split_total_number > 0:
            for i in range(split_total_number):
                seq_str = "%02d" % self.pkt_seq
                frame_list.append(seq_str + str(split_total_number) + str(split_seq) + frame[i*frame_size:(i+1)*frame_size])
                split_seq = split_seq + 1
                self.pkt_seq = self.pkt_seq + 1
                if self.pkt_seq > 99:
                    self.pkt_seq = 0
            seq_str = "%02d" % self.pkt_seq
            frame_list.append(seq_str + str(split_total_number) + str(split_seq) + frame[split_total_number*frame_size:])
            self.pkt_seq = self.pkt_seq + 1
        else:
            seq_str = "%02d" % self.pkt_seq
            frame_list.append(seq_str + str(split_total_number) + str(split_seq) + frame[:])
            self.pkt_seq = self.pkt_seq + 1
        assert(split_total_number==split_seq)

        if self.pkt_seq > 99:
            self.pkt_seq = 0

        return frame_list

    def send_frame(self,frame):
        """ Send frame to destination """
        data = numpy.array(frame)
        frame = data.tostring()

        # to split the frame and get a frame string list
        # CAUTION: first byte is sequence number
        frame_list = self.split_frame(frame,UDP_PAYLOAD_SIZE)

        # Main functions to send the frame
        # Mofification: use for loop to send
        for i in range(len(frame_list)):
            # randomly drop the packets with certain probabilities
            # Goal: To test the packet recovery ability at the receiver side
            # we deploy Gaussian random distribution to get drop rate, sigma = 1, mean = 1, 3*sigma=3
            if DEBUG and random.uniform(0,1)<=0.1:
                continue

            self.sock.sendto(frame_list[i],(self.server_host,self.port))

            self.total_send_bytes += len(frame_list[i])
            self.send_frame_num = self.send_frame_num + 1
            client_lock.acquire()
            self.display_speed = self.total_send_bytes * 1.0 / (time.time()-self.timer)
            client_lock.release()


class Server:
    """
    Server is used to receive Video stream from client

    Attributes:
        port: receive port
        framesize: Frame size shown on UI, default=160*120
        receive_speed: Calculation based on (frame_num * frame_size / send_time)
        receive_frame_num: Total received frame number
    """
    def __init__(self,client_host="",port=6124,framesize=(160,120)):
        """ Init the base class for all parameter """
        self.client_host = client_host
        self.port = port
        self.framesize = framesize
        self.sock = None    # will be set in socket_prepared()
        self.buffer_size = 65536
        self.receive_frame_num = 0
        self.receive_speed = 0
        self.display_speed = 0
        self.fps = 10
        self.receive_total_bytes = 0
        self.timer = None
        self.first_frame = True

        # Two header buffer for packet lost recovery
        # Assumption: A frame will be splited into at most 3 packets
        self.prev_packet_1 = ""
        self.prev_packet_2 = ""

    def receiving(self):
        """ Receiving the frame """
        global running_flag_receive
        while running_flag_receive:
            frame = self.receive_frame()
            decimg = cv2.imdecode(frame,1)

    def set_frame(self,frame,resize_size=None):
        """ Set the received frame on UI """
        jpegPIL = Image.fromstring("RGB",self.framesize,frame,"jpeg","RGB","raw")
        temp_img = cv.CreateImage(self.framesize,cv.IPL_DEPTH_8U,3)
        cv.SetData(temp_img,jpegPIL.tostring())

        #resize operation
        if resize_size is None:
            resize_size = self.framesize
        resize_image = cv.CreateImage(resize_size,cv.IPL_DEPTH_8U,3)
        cv.Resize(temp_img,resize_image)

    def socket_prepared(self,receive_port=6124,fps=10):
        """ Prepare the socket for frame receiving """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.client_host,receive_port))
        self.fps = fps
        global receive_before,receive_not_stop
        receive_before = True
        receive_not_stop = True

    def receive_packet(self):
        chunk, addr = self.sock.recvfrom(self.buffer_size)
        if self.first_frame:
            self.timer = time.time()
        self.receive_frame_num = self.receive_frame_num + 1

        # Modified by Jonathan @ 2015
        self.receive_total_bytes += len(chunk)
        if self.first_frame:
            self.first_frame = False
            server_lock.acquire()
            self.display_speed = self.receive_total_bytes
            server_lock.release()
        else:
            server_lock.acquire()
            self.display_speed = self.receive_total_bytes * 1.0 / (time.time()-self.timer)
            server_lock.release()
        return chunk

    ################################
    # receive and re-assemble the frame
    # Functions: When receiving a frame, find the modding number,
    # if counting mod size = 0, then re-assemble the frame and draw on the screen
    # if frame lost, borrow the previous frame
    # For simplicity: assume 2 packets per frame
    ################################

    def recover_frame(self,packet_list,split_total_number):
        frame_data = ''

        last_seq = packet_list[len(packet_list)-1][0]
        expect_seq = last_seq - split_total_number

        for data in packet_list:
            if expect_seq == data[0]:
                frame_data = frame_data + data[1][4:]
                expect_seq = expect_seq + 1
            elif expect_seq < data[0]:
                frame_data = frame_data + data[1][4:] + data[1][4:]
                expect_seq = expect_seq + 2
            else:
                print "Packet overlap! Frame end packet lost"
                return (frame_data,False)
        return (frame_data,True)

    def receive_frame(self):
        """
        Modification: Due to the packet split in the sender side,
        packet re-assemble is needed in receiving side (trigger re-assemble when )

        Caution: in receiving side, packet lost need dealing by borrowing neighbor frame

        packet list will be used to store temp packets before assembling,
        each packet will be store as a tuple (receive_seq,data)
        """
        packet_list = []
        frame_data = ""

        while 1:
            chunk = self.receive_packet()
            receive_seq = int(chunk[:2])
            split_total_number = int(chunk[2])
            split_seq = int(chunk[3])
            #print "Receive packet seq:", receive_seq

            # Note: here it will re-assemble the frame from multiple packets.
            # when it finds that split_total == split_frame, it will trigger assemble process and return data
            # for packet recovering, we borrow the data from neighbor packet and pad the frame
            # TODO: a more resonable recovering method will be designed
            if split_total_number > split_seq:
                packet_list.append((receive_seq,chunk))
            elif split_total_number == split_seq:
                packet_list.append((receive_seq,chunk))
                if len(packet_list) == (split_total_number+1):
                    for data in packet_list:
                        frame_data = frame_data + data[1][4:]
                    self.prev_packet_1 = frame_data
                    break
                else:
                    print "Packet need recovering! len(packet_list)=%d, split_total_number=%d \n" % (len(packet_list),split_total_number+1)
                    # TODO: Enhance the data recovery function
                    '''
                    (frame_data,success) = self.recover_frame(packet_list,split_total_number)
                    if not success:
                        frame_data = self.prev_packet_1
                    '''

                    # Here we skip the error data (no recvoery)
                    frame_data = self.prev_packet_1
                    break
            else:
                print "split_total_number < split_seq, packet overlap!\n"
                '''
                for data in packet_list:
                        frame_data = frame_data + data[1][4:]
                '''
                # Here we skip the error data (no recvoery)
                frame_data = self.prev_packet_1
                break

        return numpy.fromstring(frame_data, dtype='uint8')

class ImageGUI(Frame):
    """
    ImageGUI that we will use to show the UI on user screen
    """
    def __init__(self, parent):
        self.parser = OptionParser()
        self.parser.add_option("-d", "--dir_url", type="str", default="/img_data", help="dirurl")
        self.parser.add_option("-s", "--send_port", type="int", default=6123, help="sendport")
        self.parser.add_option("-r", "--receive_port", type="int", default=6123, help="receiveport")
        self.parser.add_option("-i", "--send_ip", type="str", default="192.168.200.1", help="sendip")  # 192.168.200.1
        self.parser.add_option("-e", "--self_ip", type="str", default="127.0.0.1", help="selfip")
        self.parser.add_option("-x", "--window_size_x",type="int", default=640, help="windowsizex")
        self.parser.add_option("-y", "--window_size_y",type="int", default=480, help="windowsizey")
        self.parser.add_option("-a", "--send_size_x",type="int", default=320, help="sendsizex") #320
        self.parser.add_option("-b", "--send_size_y",type="int", default=240, help="sendsizey") #240
        self.parser.add_option("-f", "--fps",type="float", default=5, help="fps") #5
        self.parser.add_option("-c", "--compress_rate",type="int", default=10, help="compress_rate") #20
        (self.options, self.args) = self.parser.parse_args()

        self.ip = self.options.self_ip

        self.dirPath = os.getcwd()+self.options.dir_url
        self.send_port = self.options.send_port
        self.send_ip = self.options.send_ip
        self.receive_port = self.options.receive_port
        self.window_size_x = self.options.window_size_x
        self.window_size_y = self.options.window_size_y
        self.send_size_x = self.options.send_size_x
        self.send_size_y = self.options.send_size_y
        self.fps = self.options.fps
        self.compress_rate = self.options.compress_rate

        self.sendPacketValue = StringVar()
        self.sendByteValue = StringVar()
        self.receivePacketValue = StringVar()
        self.receiveByteValue = StringVar()

        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        #client side
        self.parent.title("Video Stream")
        self.pack(fill=BOTH, expand=1)

        self.labelPort2 = Label(self, text="receive port number")
        self.labelPort2.place(x=510,y=0.5)

        self.portText2 = Text(self, width = 10, height = 1)
        self.portText2.place(x=510,y=20)
        self.portText2.insert(END, str(self.receive_port))

        self.receiveButton = Button(self, text="Start to Receive", width = 15, height = 1, command=self.onReceiveClick)
        self.receiveButton.place(x=600,y=450)

        self.receiveStopButton = Button(self, text="Stop Receiving", width=15,height=1,command=self.onStopReceivingClick)
        self.receiveStopButton.place(x=800,y=450)

        self.sendPacketLabel = Label(self, text="Frame Sent:")
        self.sendPacketLabel.place(x=750,y=0.5)
        self.sendPacket = Label(self, textvariable=self.sendPacketValue)
        self.sendPacket.place(x=900,y=0.5)

        self.sendByteLabel = Label(self, text="Transmit Speed:")
        self.sendByteLabel.place(x=750,y=20)
        self.sendByte = Label(self, textvariable=self.sendByteValue)
        self.sendByte.place(x=900,y=20)

        self.receivePacketLabel = Label(self, text="Frame received:")
        self.receivePacketLabel.place(x=750,y=40.5)
        self.receivePacket = Label(self, textvariable=self.receivePacketValue)
        self.receivePacket.place(x=900,y=40.5)

        self.receiveByteLabel = Label(self, text="Receive Speed:")
        self.receiveByteLabel.place(x=750,y=62)
        self.receiveByte = Label(self, textvariable=self.receiveByteValue)
        self.receiveByte.place(x=900,y=62)

        '''
        self.timeLabel = Label(self, text="Elapsed time:")
        self.timeLabel.place(x=750,y=40)
        self.time = Label(self, textvariable=self.elapsedTimeValue)
        self.time.place(x=900,y=40)

        self.rateLabel = Label(self, text="Rate:")
        self.rateLabel.place(x=750,y=60)
        self.rate = Label(self, textvariable=self.averageRateValue)
        self.rate.place(x=900,y=60)
        '''

        self.sender = Client()
        self.receiver = Server()

        #sending window initialization
        self.initialImage = Image.open("videochat.jpg")
        tkimage = ImageTk.PhotoImage(self.initialImage)
        self.imgLabel = Label(self,image=tkimage)
        self.imgLabel.image = tkimage
        self.imgLabel.place(x=80,y=100)

        #receiving window initialization
        tkimage2 = ImageTk.PhotoImage(self.initialImage)
        self.imgLabel2 = Label(self,image=tkimage2)
        self.imgLabel2.image = tkimage2
        self.imgLabel2.place(x=600,y=100)

        #server side

        self.labelPort = Label(self, text="send port number")
        self.labelPort.place(x=10,y=0.5)

        self.portText = Text(self, width = 10, height = 1)
        self.portText.place(x=10,y=20)
        self.portText.insert(END, str(self.send_port))

        self.labelframe = Label(self, text="send frame size")
        self.labelframe.place(x=200,y=0.5)

        self.labelfps = Label(self, text="send FPS")
        self.labelfps.place(x=200,y=40.5)
        self.fpsText = Text(self, width = 10, height = 1)
        self.fpsText.place(x =200,y=60)
        self.fpsText.insert(END, str(self.fps))

        self.labelcom_rate = Label(self, text="Compression Rate")
        self.labelcom_rate.place(x=300,y=40.5)
        self.com_rateText = Text(self, width = 10, height = 1)
        self.com_rateText.place(x =300,y=60)
        self.com_rateText.insert(END, str(self.compress_rate))

        self.frameXText = Text(self, width = 10, height = 1)
        self.frameXText.place(x=200,y=20)
        self.frameXText.insert(END, str(self.send_size_x))
        self.frameYText = Text(self, width = 10, height = 1)
        self.frameYText.place(x=300,y=20)
        self.frameYText.insert(END, str(self.send_size_y))

        self.labelIP = Label(self, text="send ip address")
        self.labelIP.place(x=10,y=40.5)

        self.ipText = Text(self, width = 15, height = 1)
        self.ipText.place(x=10,y=60)
        self.ipText.insert(END, str(self.send_ip))

        self.buttonSend = Button(self, text="Start to Send", width=10, height=1, command=self.onSendClick)
        self.buttonSend.place(x=120,y=450)

        self.buttonStopSending = Button(self, text="Stop sending", width=10, height=1, command=self.onStopSendingClick)
        self.buttonStopSending.place(x=260,y=450)

    def onSendClick(self):
        print "onSendClick"
        global click_before,send_not_stop
        if send_not_stop:
            print "Sender Not Yet Stop!"
            return
        if True:
            ip = str(self.ipText.get("0.0",END))
            port = int(str(self.portText.get("0.0",END)))
            send_frame_x = int(str(self.frameXText.get("0.0",END)))
            send_frame_y = int(str(self.frameYText.get("0.0",END)))
            frame_fps = float(str(self.fpsText.get("0.0",END)))
            compress_rate = int(str(self.com_rateText.get("0.0",END)))
            print "\n ip is ", ip, " \n port is ", port, " \n fps is ", frame_fps, " \n compress_rate is ", compress_rate
        if not click_before:
            self.sender.prepare_video(server_host=ip,port=port,send_size_x=send_frame_x,send_size_y= send_frame_y,send_fps= frame_fps,compress_rate=compress_rate)
        else:
            self.sender.reset_parameters(server_host=ip,port=port,send_size_x=send_frame_x,send_size_y= send_frame_y,send_fps= frame_fps,compress_rate=compress_rate)

        print "\n sender port is ",self.sender.port
        print "\n sender ip is",self.sender.server_host
        pSend = threading.Thread(target=self.draw_cam_frame)
        pSend.start()

    def onReceiveClick(self):
        print "onReceiveClick"
        global receive_before,receive_not_stop
        port = int(str(self.portText2.get("0.0",END)))
        frame_fps = float(str(self.fpsText.get("0.0",END)))
        #print "\n fps is ",frame_fps
        if receive_not_stop:
            print "Receiver Not Yet Stop!"
            return
        if not (self.receiver.port == port and receive_before):
            self.receiver.socket_prepared(receive_port=port,fps=frame_fps)
        #print "\n receiver port is ",self.receiver.port
        #print "\n receiver fps is ",self.receiver.fps
        pRece = threading.Thread(target=self.draw_receive_frame)
        pRece.start()


    def draw_cam_frame(self):
        global running_flag_send
        running_flag_send = True
        while running_flag_send:
            str_img,frame = self.sender.get_frame(window_size=(320,240))
            im = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            new_frame = Image.fromarray(im)
            img = ImageTk.PhotoImage(new_frame)
            self.imgLabel.configure(image=img)
            self.imgLabel.image = img
            client_lock.acquire()
            self.sendByteValue.set("%4.2f kbits" % (self.sender.display_speed/1000*8))
            client_lock.release()
            self.sendPacketValue.set(str(self.sender.send_frame_num)+" Frames")
            self.update()

            # TODO: spliting frame is needed before the frame is send
            # DONE: modification in Client class
            self.sender.send_frame(str_img)

            # IMPORTANT: This sleep() is for FPS control, a better control should be put in the send function
            time.sleep(1/self.sender.fps)

    def draw_receive_frame(self):
        global running_flag_receive
        running_flag_receive = True
        while running_flag_receive:
            server_lock.acquire()
            self.receiveByteValue.set("%4.2f kbits" % (self.receiver.display_speed/1000*8))
            server_lock.release()
            self.receivePacketValue.set(str(self.receiver.receive_frame_num)+" Frames")
            frame = self.receiver.receive_frame()
            decimg = cv2.imdecode(frame,1)
            if decimg is None:
                continue
            im = cv2.cvtColor(decimg, cv2.COLOR_BGR2RGB)
            temp_frame = Image.fromarray(im)
            temp_frame = ImageTk.PhotoImage(temp_frame)
            self.imgLabel2.configure(image=temp_frame)
            self.imgLabel2.image = temp_frame
            self.update()

    def onStopSendingClick(self):
        print "OnClickStopSending"
        global running_flag_send,send_not_stop
        send_not_stop = False
        running_flag_send = False
        global running_flag_receive,receive_not_stop
        running_flag_receive = False
        receive_not_stop = False

    def onStopReceivingClick(self):
        print "OnClickStopReceiving"
        global running_flag_receive,receive_not_stop
        running_flag_receive = False
        receive_not_stop = False


def main():
    root = Tk()
    root.geometry("1000x500+300+300")
    app = ImageGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
