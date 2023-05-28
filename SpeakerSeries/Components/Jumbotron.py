import pynecone as pc

jumbotron_style = {
    "width": "100%",
    "min_height": "50vh",
    "height": "fit-content",
    "color": "white",
    "background": "rgb(2,0,36)",
    "background": "linear-gradient(324deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%)",
    "border_radius": "2em",
    "box_shadow": "0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)",
}


class Jumbrotron_State(pc.State):
    pass


def Jumbotron() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Tech Speaker Series", size="4xl"),
            pc.heading("Presented By Nate Roberts and Friends", size="md"),
            pc.text(
                "Welcome to Speaker Series, a website that hosts engaging, informative, inspiring conversations with professionals from the technology sector. Here you can ask questions, listen to their stories, insights, and advice on how they prepared for, entered, survived, and thrived in their careers. Whether you are young or old, a beginner or an expert, a student or a teacher, you will find something valuable and motivating in these presentations. Join us and discover how you can pursue your dreams in the field of technology.",
                text_align="center",
            ),
            width="60%",
        ),
        style=jumbotron_style,
        center_content=True,
    )
