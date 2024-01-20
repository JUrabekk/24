#Мы очень любим мультфильм «Чип и Дейл». А вы?
#Давайте попробуем написать функцию chip_and_dale(number), которая сможет
#монозвуковой файл с любой речью переделать так, чтобы казалось, что слова
#произносит герой любимого нами мультфильма Чип.
#Для этого надо ускорить воспроизведение.
#В функцию передаётся натуральное число i из диапазона [2..5].
#Необходимо прочитать файл in.wav, оставить каждый i-ый фрейм и сохранить
#результат в файле out.wav

def chip_and_dale(number):
    import wave
    import struct
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")
    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = data[:: number]
    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)
    dest.writeframes(newframes)
    source.close()
    dest.close()

chip_and_dale(3)