"""Welcome to Reflex!."""

# from reflex_web import styles

# Import all the pages.
# from reflex_web.pages import *

import reflex as rx
import reflex_web.styles.styles as styles
from reflex_web.pages.index import index  # *NO QUITAR, SINO NO FUNCIONA
from reflex_web.pages.projects import projects  # *NO QUITAR, SINO NO FUNCIONA
from reflex_web.api.api import hello


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
# app = rx.App(style=styles.base_style)
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)





app.api.add_api_route('/hello', hello)