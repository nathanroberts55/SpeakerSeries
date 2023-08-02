"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import pynecone as pc
from pcconfig import config
from SpeakerSeries import styles
from .Components.Navbar import Navbar
from .Components.Jumbotron import Jumbotron
from .Components.UpcomingSpeakers import UpcomingSpeakers
from .Components.Signup import Signup
from .Components.PastSpeakers import PastSpeakers
from .Components.Footer import Footer
from .models import Attendee


class State(pc.State):
    attendee_name: str = ""
    attendee_email: str = ""

    def add_attendee(self):
        """
        Add a Attendee
        """

        with pc.session() as session:
            if session.query(Attendee).filter_by(email=self.attendee_email).first():
                return pc.window_alert("This email has already signed up!")
            session.add(Attendee(name=self.attendee_name, email=self.attendee_email))
            session.commit()

        return pc.window_alert(
            f"Thanks {self.attendee_name} you have been added to the attendee mail list!"
        )


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            Navbar(),
            Jumbotron(),
            UpcomingSpeakers(),
            Signup(),
            PastSpeakers(),
            Footer(),
        ),
        content_center=True,
        background_color=styles.WHITE_SMOKE,
    )


# Add state and page to the app.
app = pc.App(state=State, style=styles.BASE_STYLE, stylesheets=styles.STYLESHEETS)
app.add_page(
    index,
    title="NR Tech | Speaker Series",
)
app.compile()
