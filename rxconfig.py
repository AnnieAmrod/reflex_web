import reflex as rx

config = rx.Config(
    app_name="reflex_web",
    api_url="https://reflex-web.onrender.com",
    cors_allowed_origins=[
        'http://localhost:3000'
        'https://about-me.reflex.run/'
    ]
)
