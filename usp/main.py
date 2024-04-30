import flet as ft


def main(page: ft.Page):
    page.title = "US Parameters"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = True
    page.appbar = ft.AppBar(
        title=ft.Text("US Parameters"),
        bgcolor=ft.colors.with_opacity(0.05, ft.cupertino_colors.SYSTEM_BACKGROUND),
    )

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    def calculate(e):
        value = 0.0
        i1.value = str(value)
        page.update()
    
    btn = ft.ElevatedButton("Calculate")
    i1 = ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100)
    i2 = ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100)

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        # ft.Checkbox(value=False, label="Continuous Wave Mode"),
                        ft.Row(
                            [
                                ft.Text("Wave Mode"),
                                ft.Dropdown(
                                    width=200,
                                    options=[
                                        ft.dropdown.Option("Pulse Wave Mode"),
                                        ft.dropdown.Option("Continuous Wave Mode"),
                                    ],
                                ),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Amplitude (MPa):"),
                                ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Center frequency (MHz):"),
                                ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Duty cycle (%):"),
                                ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("PRF (kHz):"),
                                ft.TextField(value="0", text_align=ft.TextAlign.LEFT, width=100),
                            ]
                        ),
                        btn,
                        ft.Row([
                            ft.Text("I_sppa (W/cm^2):"),
                            i1
                        ]),
                        ft.Row([
                            ft.Text("I_spta (W/cm^2):"),
                            i2
                        ])
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(main)
