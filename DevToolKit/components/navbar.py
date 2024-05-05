import reflex as rx

def navbar(sidebar: rx.Component = None) -> rx.Component:
    return rx.flex(
        rx.link(
            rx.box(
                rx.image(
                    src="/logos/dark/reflex.svg",
                    alt="Reflex Logo",
                    height="20px",
                    justify="start",
                ),
            ),
            href="/",
        ),
        navigation_section(),
        rx.box(
            flex_grow="1",
        ),
        blur_background(),
        rx.flex(
            search_bar(),
            github(),
            rx.box(
                discord(),
                display=["none", "none", "none", "none", "flex", "flex"],
            ),
            rx.box(
                sidebar_button(sidebar),
                display=["flex", "flex", "flex", "none", "none", "none"],
            ),
            spacing="3",
            align_items="center",
        ),
        id="navbar",
        position="fixed",
        width="100%",
        top="0px",
        z_index="5",
        align_items="center",
        spacing="5",
        padding="15px",
    )
   