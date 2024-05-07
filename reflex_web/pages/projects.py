"""The home page of the app."""

import reflex as rx
import reflex_web.utils as utils
from reflex_web.routes import Route
from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer

from reflex_web.views.header import header
from reflex_web.views.projects_links import projects_links
from reflex_web.views.sponsors import sponsors

from reflex_web.styles.styles import Size as Size
import reflex_web.styles.styles as styles


@rx.page(
    route=Route.PROJECTS.value,
    title=utils.projects_title,
    description=utils.projects_description,
    image=utils.preview,
    meta=utils.projects_meta
)
def projects() -> rx.Component:
    # return rx.text('Hola Mundo', color='blue')
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                projects_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.BIG.value,
                margin_x=Size.BIG.value,
            )
        ),
        footer()
    )
