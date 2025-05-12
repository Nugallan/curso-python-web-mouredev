import reflex as rx

config = rx.Config(
    app_name="link_bio",
    cors_allowed_origins=[ # Permitimos que otros dominios accedan a nuestra app
        "https://localhost:3000",
        
    ]
)