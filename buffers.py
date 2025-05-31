import os
import random

# import get_from_freesound
# paths = get_from_freesound.fetch()

asmr_files = [
    "sounds/47723__jovica__wind-16.flac",
    "sounds/705344__girlwithsoundrecorder__cats-purring-asmr.wav",
    "sounds/790475__greasyplastic__female-whisper-you-better-run-run-for-your-life-do-not-stop.wav",
    # "sounds/ASMR for White Liberals.mp3",
    "sounds/bassAI.wav",
    # "sounds/Cardi B Explores #ASMR _ W Magazine.mp3",
    "sounds/Karu4Kurz.wav",
    # "sounds/Lady Gaga Explores #ASMR _ W Magazine.mp3",
    "sounds/Learn.wav",
    "sounds/radiator.flac",
    "sounds/swing-long.WAV",
    "sounds/water-tunnel-rocks.wav",
    "sounds/689813__philip_goddard__half-speed-extraordinary-quintet-of-wind-chimes-gypsy-olympos-polaris-mercury.flac",
]

drone_files = [
    "sounds/Rhythmus MASTER.wav",
    "sounds/808032__deadrobotmusic__ambient-f-sharp-minor-ethereal-choir-pad-1.wav",
    "sounds/807413__lynxmoth__florescent-loud.wav",
]

asmr_buffers = []
drone_buffers = []

buffers = {}

current_path = os.getcwd()


def load_buffers(server):
    current_path = str(os.getcwd())

    for file_path in asmr_files:
        buffer = server.add_buffer(
            file_path=os.path.join(current_path, file_path),
        )
        asmr_buffers.append(buffer)

    for file_path in drone_files:
        buffer = server.add_buffer(
            file_path=os.path.join(current_path, file_path),
        )
        drone_buffers.append(buffer)

    return buffers


def get_random_drone_buffer():
    print(drone_buffers)
    return random.choice(drone_buffers)


def get_random_asmr_buffer():
    print(asmr_buffers)
    return random.choice(asmr_buffers)


def get_shuffle_drone_buffer():
    return random.shuffle.choice(drone_buffers)
