import reflex as rx
from reflex_web.routes import Route
from reflex_web.components.link_button import link_button
from reflex_web.components.title import title
import reflex_web.constants as url


def projects_links() -> rx.Component:
    return rx.vstack(
        title('Todos mis proyectos'),
        link_button(
            'Horario para clases',
            '''Proyecto colaborativo desarrollado con HTML, JavaScript y desplegado en surge.sh''',
            '/icons/calendar-days-solid.svg',
            url.DAW_SCHEDULE
        ),
        link_button(
            'KAT: Encuentra a tu mascota',
            '''Desarrollado en Django, con MySQL y
                    desplegado de forma directa en Clouding con
                    servidor Ubuntu y servidor web nginx''',
            '/icons/paw-solid.svg',
            url.KAT_URL
        ),
        link_button(
            'Sistema de control de stock',
            '''Desarrollado en Django, con MySQL/SQLite''',
            '/icons/clipboard-list-solid.svg',
            url.STOCK_MANAGEMENT_URL
        ),
        link_button(
            'Proyectos reales',
            '''Desarrollos realizados con las herramientas Elementor y Divi de WordPress''',
            '/icons/wordpress.svg',
            url.WP_DIVI
        ),
        width='100%',
        spacing='3'
    )
