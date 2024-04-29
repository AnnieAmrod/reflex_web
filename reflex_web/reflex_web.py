"""Welcome to Reflex!."""

# from reflex_web import styles

# Import all the pages.
# from reflex_web.pages import *

import reflex as rx
from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer

from reflex_web.views.header.header import header
from reflex_web.views.links.links import links
from reflex_web.views.sponsors.sponsors import sponsors

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
                sponsors(),
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
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title='Miriam Durán | Conoce mi perfil profesional',
    description='Soy desarrolladora especializada en Python y Django, apasionada de la programación y el diseño web.',
    image='avatar.jpeg'
)
# !app.compile() # DEPRECATED
