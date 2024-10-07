import reflex as rx


class State(rx.State):
    """The app state."""

    ...


@rx.page(route="/")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.heading("Footstats ⚽")
    )
