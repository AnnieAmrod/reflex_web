import reflex as rx
from reflex_web.components.link_icon import link_icon
from reflex_web.components.info_text import info_text
from reflex_web.styles.styles import Size as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name='Miriam Durán',
                fallback='MD',
                size='7',
                color_scheme='indigo',
                radius='full'
            ),
            rx.vstack(
                rx.heading(
                    'Miriam Durán',
                    size='6'
                ),
                rx.text(
                    '@annieamod',
                ),
                rx.hstack(
                    link_icon('https://www.instagram.com/annieamrod/'),
                    margin_top='var(--space-2)'
                ),
                align_items='start',
                gap='0'
            ),
            align_items='center',
            spacing='5'
        ),
        rx.flex(
            info_text('+3', 'años de experiencia'),
            rx.spacer(),
            info_text('+3', 'años de experiencia'),
            rx.spacer(),
            info_text('+3', 'años de experiencia'),
            width='100%'
        ),
        rx.text('''Apasionada de la programación y el diseño web.
        Soy perfeccionista, comprometida y creativa, con gran capacidad para el aprendizaje.
        Busco la excelencia en cada proyecto que realizo.'''),
        spacing='5'
    )
