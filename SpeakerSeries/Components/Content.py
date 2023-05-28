import pynecone as pc
from SpeakerSeries import styles


def Content(*children, **kwargs):
    kwargs = {
        "max_width": "80%",
        "padding_x": ["1em", "2em", "3em"],
        "align_items": "center",
        **kwargs,
    }
    return pc.box(
        *children,
        **kwargs,
    )
