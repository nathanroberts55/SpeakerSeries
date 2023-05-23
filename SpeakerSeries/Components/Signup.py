import pynecone as pc
from SpeakerSeries import styles

signup_section_style = {
    "background_color": f"{styles.DARK_GRAY + '50'}",
    "height": "40vh",
    "width": "100vw",
    "margin": "0rem",
}

signup_form_style = {
    "padding_top": ".5em",
    "width": "100%",
}


class Signup_State(pc.State):
    pass


def SignupForm() -> pc.Component:
    return pc.box(
        pc.vstack(
            pc.form_control(
                pc.hstack(
                    pc.input(
                        type_="text",
                        placeholder="Full Name",
                        is_required=True,
                        width="50%",
                        margin=["0.25em", "0.25em"],
                    ),
                    pc.input(
                        type_="email",
                        placeholder="Email",
                        is_required=True,
                        width="50%",
                        margin=["0.25em", "0.25em"],
                    ),
                )
            ),
            pc.button(
                "Sign Up", bg=styles.SKY_BLUE, color=styles.WHITE_SMOKE, size="lg"
            ),
        ),
        **signup_form_style,
        center_content=True,
    )


def Signup() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Want to Join the Conversation?", size="2xl"),
            pc.text(
                "Fill in the form below to join subscribe and never miss another insightful conversation!"
            ),
            SignupForm(),
        ),
        center_content=True,
        **signup_section_style,
    )
