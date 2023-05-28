import pynecone as pc
from SpeakerSeries import styles


class PastSpeakers_State(pc.State):
    pass


def PastSpeakerVideo(src) -> pc.Component:
    return pc.box(
        pc.html(
            f"<iframe height='100%' width='100%' src={src} title='YouTube video player' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share' allowfullscreen></iframe>",
            height="65vh",
            width="100%",
        ),
        width="100%",
    )


def PastSpeakers() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Past Conversations", size="2xl", margin=["0.5em", "0.5em"]),
            pc.text(
                "Have a look at past conversations that we have had with our remarkable colleagues and others.",
                font_size="1.25em",
            ),
            pc.spacer(),
            PastSpeakerVideo("https://www.youtube.com/embed/LYl-kxYUnCc"),
            margin_bottom="1em",
            width="80%",
        ),
        center_content=True,
    )
