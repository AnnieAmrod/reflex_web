import reflex as rx
from reflex_web.components.link_button import link_button
from reflex_web.components.title import title
import reflex_web.constants as url


def links() -> rx.Component:
    return rx.vstack(
        title('Conóceme'),
        link_button(
            'GitHub',
            'Innovación: Explora mis proyectos',
            'icons/github.svg',
            url.GITHUB_URL
        ),
        link_button(
            'LinkedIn',
            'Aptitud: Descubre mi perfil profesional',
            'icons/linkedin-in.svg',
            url.LINKEDIN_URL
        ),
        link_button(
            'Behance',
            'Creatividad e inspiración: Accede a mi portfolio',
            'icons/behance.svg',
            url.BEHANCE_URL
        ),
        link_button(
            'CV',
            'Mi trayectoria: Conoce mi experiencia',
            'icons/address-card-regular.svg',
            url.CV_URL
        ),

        title('Mis proyectos'),
        link_button(
            'KAT: Encuentra a tu mascota',
            '''Desarrollado en Django, con MySQL y
                    desplegado de forma directa en Clouding con
                    servidor Ubuntu y servidor web nginx''',
            'icons/paw-solid.svg',
            url.KAT_URL
        ),

        title('Contacto'),
        link_button(
            'Email',
            url.EMAIL,
            'icons/envelope-regular.svg',
            f'mailto:{url.EMAIL}'
        ),
        width='100%',
        spacing='3'
    )
