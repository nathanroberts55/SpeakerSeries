import pynecone as pc
from SpeakerSeries import styles
from .SpeakerCard import SpeakerCard


def UpcomingSpeakers() -> pc.Component:
    return pc.box(
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
        width="60vw",
        content_center=True,
    )
