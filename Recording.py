import soundfile as sf
import sounddevice as sd
import time
import os

#ham ghi am
def sync_record(filename, duration, sr, channels):
    print('recording')
    my_rec = sd.rec(samplerate=sr, channels=channels, frames=int(duration*sr))
    sd.wait()
    
    sf.write(filename + '.wav', data=my_rec, samplerate=sr)
    print('done recording')


#đọc file "news.txt"
def readfile(news):
    f = open("./output/" + news + "/news.txt", "r", encoding="utf-8")
    sentences = f.read().replace("\n", " ").split(". ") #xóa xuống dòng và tách câu
    f.close()
    return sentences

#chọn chủ đề theo danh sách trong folder
def select_topic():
    topic = os.listdir("output")
    print("chon 1 chu de de ghi am: ")
    i = 0
    for news in topic:
        print(str(i) + '-' + news + ', ')
        i+=1
    num = input("chon chu de so: ")
    return topic[int(num)]

#hàm chính
def start_record():
    i=1
    print("Enter (y/n) to record")
    topic = select_topic()  #chọn chủ đề

    sentences = readfile(topic) #đọc bài báo theo chủ đề đã chọn
    print(topic)
    w = open("./output/" + topic + "/sentence_path.txt", "a", encoding='utf-8')

    for sentence in sentences:
        inp = input("you want to record: ")
        if inp == 'y':
            print('Record sentence: ' + sentence)
            filename = "./output/" + topic +"/wav" + str(i)

            w.write("\n"+sentence)  #ghi câu vào file
            w.write('\n'+"sentence_"+str(i)+ ".wav" )   #ghi tên file âm thanh

            second = len(sentence) / 15 #thời gian tính theo độ dài chuỗi
            print(str(second)+"s")

            sync_record(filename, second , 22050, 1)    #ghi âm
            i+=1
        elif inp == 'n' :
            break

    w.close()


start_record()