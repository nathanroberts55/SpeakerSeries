"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config
from .Components.Navbar import Navbar
from .Components.SpeakerCard import SpeakerCard
from .Components.Jumbotron import Jumbotron
import pynecone as pc


class State(pc.State):
    title: str = "Speaker Series"


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            Navbar(),
            Jumbotron(),
            pc.center(
                pc.vstack(
                    pc.heading("Upcoming Speakers", size="lg"),
                    SpeakerCard(
                        "stock_headshot_1.jpg",
                        "John Smith",
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    ),
                    SpeakerCard(
                        "stock_headshot_1.jpg",
                        "Wayne Johnson",
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    ),
                    SpeakerCard(
                        "stock_headshot_1.jpg",
                        "Allan White",
                        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    ),
                ),
                width="60vw",
            ),
        ),
        content_center=True,
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
