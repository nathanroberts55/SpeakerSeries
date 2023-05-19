"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    title: str = "Speaker Series"


def SpeakerCard(image_src, name, desc) -> pc.Component:
    return pc.hstack(
        # Speaker Image
        pc.image(src=image_src, width="10em"),
        # Speaker Details (Vertical Stack):
        pc.vstack(  # Speaker Name
            pc.heading(name, size="md"),
            # Speaker Description
            pc.text(desc),
            padding="2.5em",
        ),
        width="60%",
        margin="5em",
    )


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading(State.title, font_size="2em"),
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
            padding_top="10%",
        )
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
