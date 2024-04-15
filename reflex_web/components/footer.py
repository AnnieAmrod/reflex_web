import reflex as rx
import datetime
from reflex_web.styles.styles import Size as Size
from reflex_web.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='favicon.ico',
            margin_bottom='var(--space-2)'
        ),
        rx.link(
            f'© {datetime.date.today().year} Miriam Durán v1.',
            href='https://github.com/AnnieAmrod',
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            'BUILDING SOFTWARE WITH ♥.',
            font_size=Size.MEDIUM.value,
        ),
        padding_bottom=Size.BIG.value,
        gap='0',
        color=TextColor.FOOTER.value
    )
