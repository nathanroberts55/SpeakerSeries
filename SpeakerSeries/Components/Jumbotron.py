import pynecone as pc

jumbotron_style = {
    "width": "100vw",
    "height": "50vh",
    "color": "white",
    "background": "rgb(2,0,36)",
    "background": "linear-gradient(324deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%)",
}


class Jumbrotron_State(pc.State):
    pass


def Jumbotron() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Tech Speaker Series", size="4xl"),
            pc.heading("Presented By Nate Roberts and Friends", size="md"),
            pc.text(
                "This is an area to see a Series of Presentation by Tech Professionals from varying backgrounds, countries, and careers."
            ),
            width="90%",
        ),
        style=jumbotron_style,
        center_content=True,
    )
