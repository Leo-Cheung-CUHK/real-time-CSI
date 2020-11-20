window_size=(320,240)
compression_rate = 20 
UDP_PAYLOAD_SIZE = 1450

success = False
while not success:
    success, frame = capture.read()

    if not success:
        return

    if resize_size is None:
        resize_size = send_size
    if window_size is None:
        window_size=framesize

    resize_image = cv2.resize(frame,resize_size)
    window_size_image = cv2.resize(frame,window_size)
    jpegImg_window = window_size_image
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),compression_rate]
    ret, data = cv2.imencode('.jpg', resize_image, encode_param)

str_img,frame = sender.get_frame(window_size=(320,240))
data = numpy.array(frame)
frame = data.tostring()

frame_list = []
split_total_number = len(frame) / frame_size
split_seq = 0
pkt_seq = 0

if len(frame) % frame_size == 0:
    split_total_number = split_total_number - 1

    if split_total_number > 0:
        for i in range(split_total_number):
            seq_str = "%02d" % pkt_seq
            frame_list.append(seq_str + str(split_total_number) + str(split_seq) + frame[i*frame_size:(i+1)*frame_size])
            split_seq = split_seq + 1
            pkt_seq = pkt_seq + 1
            if pkt_seq > 99:
                pkt_seq = 0
        seq_str = "%02d" % pkt_seq
        frame_list.append(seq_str + str(split_total_number) + str(split_seq) + frame[split_total_number*frame_size:])
        pkt_seq = pkt_seq + 1
    else:
        seq_str = "%02d" % pkt_seq
        frame_list.append(seq_str + str(split_total_number) + str(split_seq) + frame[:])
        pkt_seq = pkt_seq + 1
    assert(split_total_number==split_seq)

    if pkt_seq > 99:
        pkt_seq = 0

for i in range(len(frame_list)):
    frame_list[i]

    chunk = frame_list[i]
    receive_seq = int(chunk[:2])
    split_total_number = int(chunk[2])
    split_seq = int(chunk[3])

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
            frame_data = self.prev_packet_1
            break
    else:
        print "split_total_number < split_seq, packet overlap!\n"
        frame_data = self.prev_packet_1

frame = numpy.fromstring(frame_data, dtype='uint8')
decimg = cv2.imdecode(frame,1)
if decimg is None:
    continue
im = cv2.cvtColor(decimg, cv2.COLOR_BGR2RGB)
temp_frame = Image.fromarray(im)
temp_frame = ImageTk.PhotoImage(temp_frame)