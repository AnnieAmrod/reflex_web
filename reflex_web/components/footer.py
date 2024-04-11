import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.link(
            f'© {datetime.date.today().year} Miriam Durán v1.',
            href='https://github.com/AnnieAmrod',
            is_external=True
        ),
        rx.text('BUILDING SOFTWARE WITH ♥.')
    )
