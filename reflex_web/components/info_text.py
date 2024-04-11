import reflex as rx
from reflex_web.styles.styles import Size as Size


def info_text(title: str, body: str) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.span(title, font_weight='bold', color='indigo'),
        f' {body}', font_size=Size.MEDIUM.value
    )
