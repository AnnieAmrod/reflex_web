"""Welcome to Reflex!."""

# from reflex_web import styles

# Import all the pages.
# from reflex_web.pages import *

import reflex as rx
from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer

from reflex_web.views.header.header import header
from reflex_web.views.links.links import links

import reflex_web.styles.styles as styles
from reflex_web.styles.styles import Size as Size


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


def index() -> rx.Component:
    # return rx.text('Hola Mundo', color='blue')
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.BIG.value
            )
        ),
        footer()
    )


# Create the app.
# app = rx.App(style=styles.base_style)
app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
# !app.compile() # DEPRECATED
