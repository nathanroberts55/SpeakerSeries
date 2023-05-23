import pynecone as pc
from SpeakerSeries import styles

card_style = {
    "width": "100%",
    "height": "30vh",
    "background_color": f"{styles.DARK_GRAY + '15'}",
    "margin": "15px 0px",
}

date_style = {"font_size": "0.85em", "font_weight": styles.LIGHT_WEIGHT}


class SpeakerCard_State(pc.State):
    pass


def SpeakerCard(image_src, name, desc, date="TBD") -> pc.Component:
    return pc.box(
        pc.hstack(
            # Speaker Image
            pc.image(src=image_src, width="10em", margin="1.25em"),
            # Speaker Details (Vertical Stack):
            pc.vstack(
                # Date of Presentation
                pc.text(f"Date: {date}", **date_style),
                # Speaker Name
                pc.heading(name, size="lg"),
                # Speaker Description
                pc.text(desc),
                padding_left="2.5em",
                padding_right="2.5em",
                align_items="left",
            ),
            style=card_style,
        )
    )
