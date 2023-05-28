import pynecone as pc
from SpeakerSeries import styles

card_style = {
    "width": "80%",
    "min_height": "30vh",
    "height": "fit-content",
    "background_color": f"{styles.DARK_GRAY + '15'}",
    "margin": "15px 0px",
    "box_shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)",
}

date_style = {"font_size": "0.85em", "font_weight": styles.LIGHT_WEIGHT}


class SpeakerCard_State(pc.State):
    pass


def SpeakerCard(image_src, name, desc, date="TBD") -> pc.Component:
    return pc.center(
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


def UpcomingSpeakers() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading(
                "Upcoming Speakers",
                size="2xl",
                margin=styles.HEADER_MARGIN,
            ),
            SpeakerCard(
                "images/stock_headshot_1.jpg",
                "John Smith",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
            ),
            SpeakerCard(
                "images/stock_headshot_1.jpg",
                "Wayne Johnson",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                "Jun. 15, 2024",
            ),
            SpeakerCard(
                "images/stock_headshot_1.jpg",
                "Allan White",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                "Sept. 24, 2024",
            ),
        ),
        content_center=True,
    )
