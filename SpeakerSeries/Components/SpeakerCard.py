import pynecone as pc

card_style = {
    "width": "100%",
    "background_color": "gray",
    "margin": "15px 0px",
}


class SpeakerCard_State(pc.State):
    pass


def SpeakerCard(image_src, name, desc) -> pc.Component:
    return pc.box(
        pc.hstack(
            # Speaker Image
            pc.image(src=image_src, width="10em"),
            # Speaker Details (Vertical Stack):
            pc.vstack(
                # Speaker Name
                pc.heading(name, size="md"),
                # Speaker Description
                pc.text(desc),
                padding_left="2.5em",
                padding_right="2.5em",
                align_items="left",
            ),
            style=card_style,
        )
    )
