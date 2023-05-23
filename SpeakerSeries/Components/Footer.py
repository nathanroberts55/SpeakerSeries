import pynecone as pc
from SpeakerSeries import styles
from datetime import datetime

curr_year = datetime.now().year

footer_style = {
    "position": "relative",
    "width": "100vw",
    "height": "20vh",
    "bottom": "0px",
    "z_index": "5",
    "background_color": styles.DARK_GRAY,
    "color": styles.WHITE_SMOKE,
    "padding": "50px 15px",
    "margin": "0px",
}


def Footer() -> pc.Component:
    return pc.center(
        pc.hstack(
            pc.text(
                f"Copyright © {curr_year} NR Tech",
                color=styles.WHITE_SMOKE,
                font_size="1.5em",
            ),
            pc.spacer(),
            pc.link(
                pc.image(src="images/twitter.png"),
                href="http://twitter.com/nateroberstech",
            ),
            pc.spacer(),
            pc.link(
                pc.image(src="images/github.png"),
                href="https://github.com/nathanroberts55/SpeakerSeries",
            ),
        ),
        center_content=True,
        **footer_style,
    )
