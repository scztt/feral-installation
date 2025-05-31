from threading import Thread


def make_player(server):
    def play_synth(*args, **kwargs):
        def play(clock):
            server.add_synth(*args, **kwargs)

        return play

    return play_synth


def run_and_wait(func):
    t = Thread(target=func)
    t.start()
    t.join()
