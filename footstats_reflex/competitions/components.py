import reflex as rx

from typing import Dict



def competition_card(competition: Dict[str, str]) -> rx.Component:
    return rx.box(
        rx.image(
            src={competition.logo},
            width="100%",
            height="100%",
            class_name="transition-transform hover:scale-110 duration-200"
        ),
        rx.box(
            rx.text(
                competition.name,
                class_name="p-4 text-lg font-semibold text-white"
            ),
            class_name="""absolute inset-0 flex items-end bg-gradient-to-t
            from-black/90 to-transparent
            """
        ),
        class_name="""
        relative max-w-xs overflow-hidden rounded-xl
        transition-all duration-300 ease-in-out transform hover:shadow-xl
        hover:-translate-y-1 hover:cursor-pointer
        """,
    )

