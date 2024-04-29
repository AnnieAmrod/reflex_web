import reflex as rx
from reflex_web.styles.styles import Size as Size
from reflex_web.styles.colors import Color as Color
from reflex_web.styles.colors import TextColor as TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(
            title,
            font_weight='bold',
            color=TextColor.HEADER.value
        ),
        f' {body}',
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )
