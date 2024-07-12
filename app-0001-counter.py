# run : flet run app-0001-counter.py


import flet as ft


display1_style = ft.TextStyle(
    size=34, weight=ft.FontWeight.NORMAL, color=ft.colors.BLACK
)


def main(page: ft.Page) -> None:
    count = 0
    text_ref = ft.Ref[ft.Text]()

    def increment():
        nonlocal count
        count += 1
        text_ref.current.value = f"{count}"
        text_ref.current.update()

    page.title = "Flet Demo"
    page.theme = ft.Theme(primary_swatch=ft.colors.BLUE)
    page.appbar = ft.AppBar(title=ft.Text("Flet Demo"))
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, tooltip="Increment", on_click=lambda e: increment()
    )

    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Column(
                [
                    ft.Text(
                        "You have pushed the button this many times:",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        ref=text_ref,
                        value=f"{count}",
                        style=display1_style,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )


ft.app(main)
