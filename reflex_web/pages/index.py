"""The home page of the app."""

import reflex as rx
import reflex_web.utils as utils
from reflex_web.components.navbar import navbar
from reflex_web.components.footer import footer

from reflex_web.views.header import header
from reflex_web.views.index_links import index_links
from reflex_web.views.sponsors import sponsors

from reflex_web.styles.styles import Size as Size
import reflex_web.styles.styles as styles


@rx.page(
    # route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    # return rx.text('Hola Mundo', color='blue')
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width='100%',
                margin_y=Size.BIG.value,
                margin_x=Size.BIG.value,
            )
        ),
        footer()
    )
