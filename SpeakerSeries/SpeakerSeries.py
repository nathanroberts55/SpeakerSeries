"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
from pcconfig import config
from SpeakerSeries import styles
from .Components.Navbar import Navbar
from .Components.Jumbotron import Jumbotron
from .Components.UpcomingSpeakers import UpcomingSpeakers
from .Components.Signup import Signup
from .Components.Footer import Footer


class State(pc.State):
    title: str = "Speaker Series"


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            Navbar(),
            Jumbotron(),
            UpcomingSpeakers(),
            Signup(),
            Footer(),
        ),
        content_center=True,
        background_color=styles.WHITE_SMOKE,
    )


# Add state and page to the app.
app = pc.App(
    state=State,
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS,
)
app.add_page(
    index,
    title="NR Tech | Speaker Series",
)
app.compile()
