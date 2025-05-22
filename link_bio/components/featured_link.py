import reflex as rx
from link_bio.model.Featured import Featured

def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.image(
            src=featured.image
        ),
        rx.text(
            featured.title
        ),
        href=featured.url,
        is_external=True
    )