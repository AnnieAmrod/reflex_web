import reflex as rx
import reflex_web.styles.styles as styles
from reflex_web.styles.styles import Size as Size


def link_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,
                    alt=title

                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing='0',
                    align_items='start',
                    margin='0px !important',
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                ),
                align_items='center',
                width='100%'
            ),
        ),
        href=url,
        is_external=is_external,
        width='100%',
    )


'''
def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag='arrow_right',
                    width=Size.BIG.value,
                    height=Size.BIG.value,
                    margin=Size.MEDIUM.value,

                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing='3',
                    align_items='start',
                    margin='0px !important'
                ),
                align_items='center',
            ),
        ),
        href=url,
        is_external=True,
        width='100%',
    )
'''

'''
    return rx.link(
        rx.button(text, width='100%'),
        href=url,
        is_external=True,
        width='100%'
    )
'''