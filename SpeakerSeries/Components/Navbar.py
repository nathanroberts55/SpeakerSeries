import pynecone as pc


def Navbar():
    return pc.box(
        pc.hstack(
            pc.image(src="favicon.ico"),
            pc.heading("NR Tech | Speaker Series", size="md"),
            pc.spacer(),
            pc.menu(
                pc.menu_button(
                    "Home",
                    font_size="18px",
                    font_weight="bold",
                    margin="0px 30px",
                ),
                pc.menu_button(
                    "About",
                    font_size="18px",
                    font_weight="bold",
                    margin="0px 30px",
                ),
                pc.menu_button(
                    "Past Speakers",
                    font_size="18px",
                    font_weight="bold",
                    margin="0px 30px",
                ),
                pc.menu_button(
                    "Q & A",
                    font_size="18px",
                    font_weight="bold",
                    margin="0px 30px",
                ),
                pc.menu_button(
                    "Register",
                    font_size="18px",
                    font_weight="bold",
                    margin="0px 30px",
                ),
            ),
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        background_color="white",
        padding="0px 15px",
    )
