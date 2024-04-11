import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name='Miriam Durán', fallback='MD', size='7'),
        rx.text('@annieamod'),
        rx.text('HOLA 👋🏻 MI NOMBRE ES MIRIAM DURÁN'),
        rx.text('''Apasionada de la programación y el diseño web.
        Soy perfeccionista, comprometida y creativa, con gran capacidad para el aprendizaje.
        Busco la excelencia en cada proyecto que realizo.''')
    )
