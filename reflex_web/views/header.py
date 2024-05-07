import reflex as rx
from reflex_web.components.link_icon import link_icon
from reflex_web.components.info_text import info_text
from reflex_web.styles.colors import TextColor as TextColor
from reflex_web.styles.colors import Color as Color
import reflex_web.constants as url


def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name='Miriam Durán',
                fallback='MD',
                size='7',
                src='/avatar.jpeg',
                #bg=Color.CONTENT.value,
                color_scheme='plum',
                #color=TextColor.BODY.value,
                radius='full',
                padding='2px',
                border='4px solid',
                border_color=Color.SECONDARY.value
            ),
            rx.vstack(
                rx.heading('Miriam Durán'),
                rx.text(
                    '@annieamod',
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        '/icons/instagram.svg',
                        url.INSTAGRAM_URL,
                        'Instagram'
                    ),
                    margin_top='var(--space-2)',
                    spacing='5'
                ),
                align_items='start',
                gap='0'
            ),
            align_items='center',
            spacing='5'
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text('+3', 'años de experiencia'),
                    # rx.spacer(),
                    # info_text('2', 'aplicaciones desplegadas'),
                    # rx.spacer(),
                    # info_text('+3', 'años de experiencia'),
                    width='100%',
                ),
                rx.text(
                    '''Apasionada de la programación y el diseño web.
                Soy perfeccionista, comprometida y creativa, con gran capacidad para el aprendizaje.
                Busco la excelencia en cada proyecto que realizo.''',
                    color=TextColor.BODY.value
                ),
                spacing='5'
            ),
        ),
        spacing='5',
    )
