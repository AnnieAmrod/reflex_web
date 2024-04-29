import reflex as rx
from reflex_web.styles.styles import Size as Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value,
            alt=alt,
        ),
        href=url,
        is_external=True
    )


'''
def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag='link',
            stroke_width=1,
            size=15,
            color="indigo"
        ),
        href=url,
        is_external=True
    )
'''
