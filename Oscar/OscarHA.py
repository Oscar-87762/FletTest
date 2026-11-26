from typing import Any

import flet as ft


@ft.component
def ColorSwitcher() -> ft.Container:
    is_black: bool
    set_is_black: Any
    is_black, set_is_black = ft.use_state(False)

    btn_text: str = "Wechsel zu Weiß" if not is_black else "Wechsel zu Grün"
    btn_color: str = ft.Colors.WHITE if is_black else ft.Colors.GREEN
    bg_color: str = ft.Colors.WHITE if is_black else ft.Colors.GREEN_900

    def toggle_color() -> None:
        set_is_black(not is_black)

    return ft.Container(
        content=ft.Stack(
            controls=[
                ft.Text(
                    "SPVGG Fürth",
                    size=48,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(
                    content=ft.Button(
                        btn_text,
                        bgcolor=btn_color,
                        color=ft.Colors.BLACK,
                        on_click=toggle_color,
                    ),
                    alignment=ft.Alignment.BOTTOM_CENTER,
                    padding=20,
                    expand=True,
                ),
            ],
            alignment=ft.Alignment.CENTER,
            expand=True,
        ),
        bgcolor=bg_color,
        padding=20,
        alignment=ft.Alignment.CENTER,
        expand=True,
    )


def main(page: ft.Page) -> None:
    page.title = "Flet 1.0.1 Modern & Typisiert"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.render(ColorSwitcher)

if __name__ == "__main__":
    ft.run(lambda page: main(page))
