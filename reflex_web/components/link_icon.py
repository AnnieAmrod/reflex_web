import reflex as rx
import reflex_web.styles.styles as styles


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
