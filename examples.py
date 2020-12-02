import audio_loopback_device as lbdevice

if __name__ == '__main__':
    device = lbdevice.get_loopback_device()  # gets current output device that supports audio loopback
    device_index = lbdevice.get_loopback_device_id()  # returns device id if you want to use it with PyAudio
    print(device_index)
    stream = lbdevice.get_loopback_stream()  # opens a PyAudio stream using the loopback device

    # the stream must be opened with "as_loopback=True" parameter so that you can get data coming from your speakers
    # it is recommended to use: stream = lbdevice.get_loopback_stream()
    # otherwise open a stream like the following
    # where audio_output_wasapi_device is the loopback device

    # stream = p.open(format=pyaudio.paInt16,
    #                 channels=audio_output_wasapi_device['maxOutputChannels'],
    #                 rate=int(audio_output_wasapi_device["defaultSampleRate"]),
    #                 input=True,
    #                 frames_per_buffer=2**11,
    #                 input_device_index=audio_output_wasapi_device["index"],
    #                 as_loopback=True)

    while 1:
        data = np.fromstring(stream.read(2 ** 11), dtype=np.int16)
        print(data)

    # after opening the stream you can capture data directly from your speakers
    # then you can plot graphs, analyze, use fourier transform etc. using audio coming from your system (without having to deal with microphone noise)
