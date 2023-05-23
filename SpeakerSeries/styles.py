""" App Styling """
import pynecone as pc

# Main Style Colors
NAVY_BLUE = "#090979"
SKY_BLUE = "#00D4FF"
WHITE_SMOKE = "#F5F5F4"
LIGHT_GRAY = "#696D7D"
DARK_GRAY = "#474747"

# FONT STYLES
TEXT_BOLD_WEIGHT = 700
HEADER_BOLD_WEIGHT = 900
LIGHT_WEIGHT = 300
TEXT_FONT_FAMILY = "Titillium Web"
HEADER_FONT_FAMILY = "Rajdhani"


HERO_FONT_SIZE = ["2em", "3em", "3em", "4em"]
H1_FONT_SIZE = ["2.2em", "2.4em", "2.5em"]
H2_FONT_SIZE = ["1.8em", "1.9em", "2em"]
H3_FONT_SIZE = "1.35em"
H4_FONT_SIZE = "1.1em"
TEXT_FONT_SIZE = "1em"
HEADER_MARGIN = ["1em", "1em"]


LINK_STYLE = {"color": SKY_BLUE, "text_descoration": "underline"}

# BASE APPLICATION STYLE
BASE_STYLE = {
    pc.Text: {
        "font_family": TEXT_FONT_FAMILY,
        "font_size": 16,
    },
    pc.Heading: {"font_family": HEADER_FONT_FAMILY},
}

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Titillium+Web:wght@200;300;400;900&display=swap",
    "https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;700&display=swap",
]
