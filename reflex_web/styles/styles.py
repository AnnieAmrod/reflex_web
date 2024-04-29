from enum import Enum
import reflex as rx
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from .fonts import FontWeight as FontWeight


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Arimo&display=swap"
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
]


# Constants
MAX_WIDTH = '560px'


# Sizes
class Size(Enum):
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    DEFAULT = '1em'
    LARGE = '1.5em'
    BIG = '2em'
    BIGGER = '4em'


# Styles

BASE_STYLE = {
    'font_family': Font.DEFAULT.value,
    'font_weight': FontWeight.LIGHT.value,
    # 'font_size': Size.DEFAULT.value,
    'background_color': Color.BACKGROUND.value,
    rx.heading: {
        'size': '6',
        'color': TextColor.HEADER.value,
        'font_family': Font.TITLE.value,
        'font_weight': FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        # "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        'color': TextColor.HEADER.value,
        'background_color': Color.CONTENT.value,
        'white_space': 'normal',
        'justify_content': 'start',
        '_hover': {
            'background_color': Color.SECONDARY.value,
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width='100%',
    padding_top=Size.LARGE.value,
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.LARGE.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.BODY.value
)
