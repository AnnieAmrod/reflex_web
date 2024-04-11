import reflex as rx
from reflex_web.components.link_button import link_button
from reflex_web.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title('Conóceme'),
        link_button(
            'GitHub',
            'Innovación: Explora mis proyectos',
            'https://github.com/AnnieAmrod'
        ),
        link_button(
            'LinkedIn',
            'Aptitud: Descubre mi perfil profesional',
            'https://www.linkedin.com/in/miriam-duran-garcia/'
        ),
        link_button(
            'Behance',
            'Creatividad e inspiración: Accede a mi portfolio',
            'https://www.behance.net/miriandurang'
        ),
        link_button(
            'CV',
            'Mi trayectoria: Conoce mi experiencia',
            'https://drive.google.com/file/d/1FCx9B7ULWssIg2NEb95oGjFJAv68uwiO/view?usp=sharing'
        ),

        title('Mis proyectos'),
        link_button(
            'KAT: Encuentra a tu mascota',
            'Desarrollado en Django, con MySQL y desplegado de forma directa en Clouding con servidor Ubuntu y servidor web nginx',
            'https://kat-mascotas.online/'
        ),
        width='100%',
        spacing='3'
    )
