from supriya import Envelope, synthdef
from supriya.enums import EnvelopeShape, DoneAction
from supriya.ugens import (
    Out,
    SinOsc,
    Balance2,
    PlayBuf,
    EnvGen,
    SampleRate,
    BufRateScale,
    Pluck,
    HPF,
    ClipNoise,
    Decay,
    LinExp,
    Dust,
    LinLin,
    LFNoise2,
    BPF,
    FreqShift,
    PitchShift,
    Splay,
    Poll,
    Impulse,
    LFSaw,
)


@synthdef()
def soundscape(out=0, buffer=0, amplitude=1, pan=0, rate=1, start_time=1, duration=1):
    # Generate an amplitude envelope for a sound, e.g. to fade it in and out
    # https://doc.sccode.org/Classes/EnvGen.html
    envelope = EnvGen.kr(
        envelope=Envelope(
            amplitudes=[0, 1, 0],
            durations=[1 / 2, 1 / 2],
            curves=[EnvelopeShape.LINEAR, EnvelopeShape.LINEAR],
        ),
        time_scale=duration,
        done_action=DoneAction.FREE_SYNTH,
    )

    # Play a buffer
    # https://doc.sccode.org/Classes/PlayBuf.html
    mod = SinOsc.kr(
        frequency=SinOsc.kr(frequency=1 / 6) * 8,
    )  # -1, 1
    mod = LinLin.kr(
        source=mod,
        input_minimum=-1,
        input_maximum=1,
        output_minimum=0.2,
        output_maximum=2.0,
    )
    sound = PlayBuf.ar(
        buffer_id=buffer,
        channel_count=2,
        loop=True,
        rate=rate * BufRateScale.kr(buffer_id=buffer),
        start_position=start_time * SampleRate.ir(),
    )

    envelope_short = Envelope.percussive(
        attack_time=0.1,
        release_time=0.3,
    )
    envelope_short = EnvGen.ar(envelope=envelope_short, gate=Dust.ar(density=1))

    bpf_frequency = LFNoise2.kr(frequency=4)
    bpf_frequency = LinExp.kr(
        source=bpf_frequency,
        input_minimum=-1,
        input_maximum=1,
        output_minimum=200,
        output_maximum=16000,
    )

    # Modulate the sound by both the envelope and the overall `amplitude` parameter
    sound = sound * amplitude * envelope * envelope_short

    sound = sound + Pluck.ar(
        source=sound,
        trigger=ClipNoise.ar(),
        maximum_delay_time=4,
        decay_time=16,
        coefficient=0.92,
        delay_time=[3, 5, 6, 2],
    )
    sound = Splay.ar(source=sound)
    sound = PitchShift.ar(
        source=sound,
        pitch_ratio=pow(2, 0.6 * LFNoise2.kr(frequency=0.5)),
    )

    sound = sound - FreqShift.ar(
        source=sound,
        frequency=0.2 * LFNoise2.kr(frequency=0.17),
        # only a small shift, this sound cooler
    )
    # Pan the sound left or right according to the `pan` parameter
    # https://doc.sccode.org/Classes/Balance2.html
    sound = Balance2.ar(
        left=sound[0],
        right=sound[1],
        position=pan,
    )
    sound = [sound[0], sound[1], sound[0], sound]
    print(sound)

    # Play the sound to an output bus (e.g. speakers)
    # https://doc.sccode.org/Classes/Out.html
    Out.ar(bus=out, source=sound)


def define_synthdefs(context):
    context.add_synthdefs(soundscape)
