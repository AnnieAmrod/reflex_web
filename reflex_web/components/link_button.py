import reflex as rx
import reflex_web.styles.styles as styles


def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag='arrow_right',
                    width=styles.Size.DEFAULT.value
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items='start'
                ),
                align_items='center'
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