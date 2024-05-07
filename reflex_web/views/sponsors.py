import reflex as rx
import reflex_web.constants as url
from reflex_web.components.title import title
from reflex_web.components.link_sponsor import link_sponsor
from reflex_web.styles.styles import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title('Colaboradores'),
        rx.chakra.responsive_grid(
            link_sponsor(
                '/josemoradev.jpeg',
                url.JMD_URL,
                'Logotipo de JoseMoraDev'
            ),
            link_sponsor(
                '/gabrielcrackpro.png',
                url.GCP_URL,
                'Logotipo de GabrielCrackPro'
            ),
            spacing='5',
            columns=[3, 6]
        ),
        width='100%',
        align_items='start'
    )


'''
def sponsors() -> rx.Component:
    return rx.vstack(
        title('Colaboradores'),
        rx.hstack(
            link_sponsor(
                'josemoradev.jpeg',
                url.JMD_URL
            ),
            link_sponsor(
                'gabrielcrackpro.png',
                url.GCP_URL
            ),
            spacing='5'
        ),
        width='100%',
        align_items='start'
    )
'''
