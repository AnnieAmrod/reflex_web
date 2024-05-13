import reflex as rx
import datetime
from reflex_web.styles.styles import Size as Size
from reflex_web.styles.colors import TextColor as TextColor
import reflex_web.constants as url
from reflex_web.components.ant_components import float_button


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='/logo.png',
            margin_bottom='var(--space-2)',
            height=Size.BIGGER.value,
            width=Size.BIGGER.value,
            alt='Logotipo de AnnieAmrod. Una "o" con diéresis.'
        ),
        rx.link(
            rx.box(
                f'© 2024 ~ {datetime.date.today().year}',
                rx.chakra.span(' Miriam Durán', color=TextColor.HEADER.value),
                ' v1.',
                color=TextColor.FOOTER.value
            ),
            href=url.GITHUB_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src='/icons/github.svg',
                    height=Size.DEFAULT.value,
                    width=Size.DEFAULT.value,
                    alt='Logotipo de GitHub'
                ),
                rx.text(
                    'BUILDING SOFTWARE WITH ♥.',
                    font_size=Size.MEDIUM.value,
                ),
            ),
            href=url.GITHUB_REPO,
            is_external=True,
            color=TextColor.HEADER.value,
        ),
        float_button(
            icon=rx.image(src='/icons/paper-plane-solid.svg'),
            href=url.TELEGRAM
        ),
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        gap='0',
        spacing='5',
        color=TextColor.FOOTER.value,
        align_items='center'
    )
