import reflex as rx
from reflex_web.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        link_button('GitHub', 'https://github.com/AnnieAmrod'),
        link_button('LinkedIn', 'https://www.linkedin.com/in/miriam-duran-garcia/'),
        link_button('Behance', 'https://www.behance.net/miriandurang'),
        link_button('CV', 'https://drive.google.com/file/d/1FCx9B7ULWssIg2NEb95oGjFJAv68uwiO/view?usp=sharing'),
        width='100%'
    )
