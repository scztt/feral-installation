import random
from re import M
import time

from typer import Typer
from supriya import Server, Options

from synthdefs import define_synthdefs, soundscape
from buffers import load_buffers, get_random_drone_buffer, get_random_asmr_buffer
from utility import run_and_wait


app = Typer()


def launch_server():
    server = Server(
        options=Options(
            sample_rate=44100,
            input_device="GIGAPORT eX",
            output_device="GIGAPORT eX",
            output_bus_channel_count=8,
            memory_size=8192 * 8,
        ),
    ).boot()
    server.sync()
    return server


def run_score(server):
    server.add_synth(
        synthdef=soundscape,
        buffer=get_random_drone_buffer(),
        duration=60,
        amplitude=0.2,
        rate=0.5,
        start_time=random.randrange(0, 60),
    )

    server.add_synth(
        synthdef=soundscape,
        buffer=get_random_asmr_buffer(),
        duration=20,
        amplitude=1.25,
        rate=1,
        start_time=random.randrange(0, 60),
    )

    time.sleep(5)


@app.command()
def run_installation():
    def run():
        server = launch_server()
        define_synthdefs(server)
        load_buffers(server)
        time.sleep(2)
        server.sync()

        while True:
            run_score(server)

    run_and_wait(run)


if __name__ == "__main__":
    print("Playing...")
    app()
    print("Finished")
