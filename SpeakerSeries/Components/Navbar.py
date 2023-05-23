import pynecone as pc
from SpeakerSeries import styles

menu_button_style = {
    "font_size": "18px",
    "font_weight": "normal",
    "margin": "0px 30px",
    ":hover": {"background_color": "light grey", "color": "light blue"},
}


def Navbar():
    return pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading("NR Tech | Speaker Series", size="md"),
            pc.spacer(),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        background_color=styles.WHITE_SMOKE,
        padding="5px 15px",
    )
