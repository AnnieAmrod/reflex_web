import reflex as rx
from reflex_web.styles.styles import Size as Size


def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height=Size.BIGGER.value,
            width='auto',
            border_radius='40px'
        ),
        href=url,
        is_external=True
    )
