#Напишите функцию break_the_silence(), которая будет убирать тишину из файла
#in.wav и сохранять полученный результат в файле out.wav
#Обратите внимание, что даже если мы не слышим звука в аудио-файле и не видим
#колебания звукового спектра на спектрограмме, это не значит, что в файле находится
#абсолютная тишина.
#В реальности во фреймах участка музыкального файла будут небольшие колебания в
#диапазоне [-5; 5]. Именно такие фреймы ваша функция и должна считать
#содержащими только тишину.

import wave
import struct


def break_the_silence():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h",
                         source.readframes(frames_count))
    newdata = list(filter(lambda x: abs(x) > 5, data))
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()

break_the_silence()