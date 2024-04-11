import reflex as rx
import reflex_web.styles.styles as styles


def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag='arrow_right',
                ),
                rx.vstack(
                    rx.text(text),
                    rx.text(text)
                )
            )
        ),
        href=url,
        is_external=True,
        width='100%',
    )


'''
    return rx.link(
        rx.button(text, width='100%'),
        href=url,
        is_external=True,
        width='100%'
    )
'''