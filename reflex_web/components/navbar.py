import reflex as rx
from reflex_web.routes import Route
import reflex_web.constants as url
import reflex_web.styles.styles as styles
from reflex_web.styles.styles import Size as Size
from reflex_web.styles.colors import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.chakra.box(
                rx.chakra.span('Ànnië', color=Color.PRIMARY.value),
                rx.chakra.span('Amröd', color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value,
        ),
        position='sticky',
        bg=Color.CONTENT.value,
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0'
    )
