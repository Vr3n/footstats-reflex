import reflex as rx

from footstats_reflex.competitions.state import CompetitionState
from footstats_reflex.competitions.components import competition_card


@rx.page(route="/", on_load=CompetitionState.all_competitions)
def index() -> rx.Component:
    return rx.container(
        rx.heading("Footstats", class_name="mb-4 text-2xl text-teal-700 font-bold"),
        rx.box(
            rx.flex(
                rx.flex(
                    rx.heading("Competitions", class_name="text-xl font-semibold"),
                    rx.divider(class_name="my-4"),
                    class_name="gap-2"
                ),
                rx.box(
                    rx.foreach(
                        CompetitionState.competitions,
                        competition_card,
                    ),
                    class_name="""
                        grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4
                        auto-rows-[200px]
                    """
                ),
                direction="column",
            ),
            class_name="py-4"
        ),
    )
