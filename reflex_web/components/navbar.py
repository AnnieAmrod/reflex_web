import reflex as rx
from reflex_web.styles.styles import Size as Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            'Miriam Durán'
        ),
        position='sticky',
        bg='#f0f8ff',
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top='0'
    )
