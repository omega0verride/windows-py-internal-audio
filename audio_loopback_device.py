import numpy as np
import pyaudio
import threading
from difflib import SequenceMatcher

default_CHUNK = 2 ** 11


def check_if_output_device(device):
    if device['maxInputChannels'] < 1 and device['maxOutputChannels'] > 0:
        return 1
    else:
        return 0


def check_api(device):
    if device["hostApi"] == 1:  # index 1 = Windows WASAPI, only WASAPI output devices support loopback
        return 1
    else:
        return 0


def check_device_name_similarity(a, b):
    similarity = SequenceMatcher(None, a,
                                 b).ratio()  # sometimes output device name is slightly-different from device that supports loopback that's why you need to check for similarities
    print("Device - Default Device Name Similarity: ", similarity)
    if similarity > 0.5:
        return 1
    else:
        return 0


def get_loopback_device():
    p = pyaudio.PyAudio()
    loopback_devices = []

    for i in range(0, p.get_device_count()):
        audio_device = p.get_device_info_by_index(i)
        if check_if_output_device(audio_device):
            if check_api(audio_device):
                print(audio_device)
                # print(p.get_host_api_info_by_index(audio_device["hostApi"]))
                print(128 * '-')
                loopback_devices.append(audio_device)

    if len(
            loopback_devices) > 1:  # if there are 2 or more devices that support loopback, choose the device that is current output
        default_device = p.get_default_output_device_info()
        print("Default Device: ", default_device)
        for i in range(len(loopback_devices)):
            if check_device_name_similarity(loopback_devices[i]["name"], default_device["name"]):
                # sometimes output device name is slightly-different from device that supports loopback that's why you need to check for similarities
                loopback_devices = [loopback_devices[i]]
                print("Selected Device: ", loopback_devices[0])
                break
    p.terminate()
    return loopback_devices[0]


def get_loopback_device_id():
    return get_loopback_device()["index"]


def get_loopback_stream(CHUNK=default_CHUNK, custom_loopback_device_index=None):
    if custom_loopback_device_index is not None:
        audio_output_wasapi_device = custom_loopback_device_index
    else:
        audio_output_wasapi_device = get_loopback_device()
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=audio_output_wasapi_device['maxOutputChannels'],
                    rate=int(audio_output_wasapi_device["defaultSampleRate"]),
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=audio_output_wasapi_device["index"],
                    as_loopback=True)
    return stream


def get_audio_loopback_data(stream, CHUNK=default_CHUNK):
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    return data  # optional example of data collecting using the stream
