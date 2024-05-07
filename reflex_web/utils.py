import reflex as rx

# Común


def lang() -> rx.Component:
    return rx.script('document.documentElement.lang="es"'),


preview = 'https://about-me.reflex.run/preview.jpg'

_meta = [
        {'name': 'og:type', 'content': 'website'},
        {'name': 'og.image', 'content': preview}
]

# Index

index_title = 'Miriam Durán | Conoce mi perfil profesional'
index_description = 'Soy desarrolladora especializada en Python y Django, apasionada de la programación y el diseño web.'

index_meta = [
    {'name': 'og.title', 'content': index_title},
    {'name': 'og.description', 'content': index_description},
]
index_meta.extend(_meta)

'''app.add_page(
    index,
    title=title,
    description=description,
    image=preview,

)
# !app.compile() # DEPRECATED'''

# Proyectos

projects_title = 'Miriam Durán | Mis Proyectos'
projects_description = 'Este es un listado con algunos de los proyectos que he realizado.'

projects_meta = [
    {'name': 'og.title', 'content': projects_title},
    {'name': 'og.description', 'content': projects_description},
]
projects_meta.extend(_meta)
