import flet as ft
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def main(page: ft.Page):
    page.title = "USP"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    # page.adaptive = True
    page.scroll = True
    page.appbar = ft.AppBar(
        title=ft.Text("Ultrasound Parameters"),
        center_title=True,
        bgcolor=ft.colors.with_opacity(0.05, ft.cupertino_colors.SYSTEM_BACKGROUND),
    )

    def calculate(e):
        tbd = (float(dc.value) / 100) / (float(prf.value) * 1e3)
        z = float(rho.value) * float(c.value)
        a = float(amplitude.value) * 1e6
        f = float(frequency.value) * 1e6
        t = np.arange(0, tbd, tbd/1e6)
        p = a * np.sin(2 * np.pi * f * t)
        pii = integrate.cumtrapz((p ** 2) / z, t, initial=0)
        if dd.value == "Pulse Wave Mode":
            value1 = pii[-1] / t[-1]  # in W/m^2
            value1 *= 1e-4  # in W/cm^2
            value2 = value1 * (float(dc.value) / 100)
        else:
            value1 = pii[-1] / tbd  # in W/m^2
            value1 *= 1e-4  # in W/cm^2
            value2 = value1
        i1text.value = "{:.2f}".format(value1)
        i2text.value = "{:.2f}".format(value2)
        page.update()
    
    btn = ft.ElevatedButton(text="Calculate", on_click=calculate, width=400, height=50)

    # Input parameters
    dd = ft.Dropdown(
                width=200,
                options=[
                    ft.dropdown.Option("Pulse Wave Mode"),
                    ft.dropdown.Option("Continuous Wave Mode"),
                ],
            )
    amplitude = ft.TextField(value="0.1", text_align=ft.TextAlign.LEFT, width=100)
    frequency = ft.TextField(value="0.5", text_align=ft.TextAlign.LEFT, width=100)
    dc = ft.TextField(value="50", text_align=ft.TextAlign.LEFT, width=100)
    prf = ft.TextField(value="1", text_align=ft.TextAlign.LEFT, width=100)
    rho = ft.TextField(value="1000", text_align=ft.TextAlign.LEFT, width=100)
    c = ft.TextField(value="1480", text_align=ft.TextAlign.LEFT, width=100)

    # Output parameters
    i1text = ft.Text(value="", text_align=ft.TextAlign.LEFT)
    i2text = ft.Text(value="", text_align=ft.TextAlign.LEFT)

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Text("Wave Mode", width=100),
                                dd,
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Amplitude (MPa):"),
                                amplitude,
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Center frequency (MHz):"),
                                frequency,
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Duty cycle (%):"),
                                dc,
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("PRF (kHz):"),
                                prf,
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Density (kg/m^3):"),
                                rho,
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Text("Speed of sound (m/s):"),
                                c,
                            ]
                        ),
                        btn,
                        ft.Row([
                            ft.Text("Spatial-peak pulse-average intensity: "),
                            i1text,
                            ft.Text(f" (W/cm^2)"),
                        ]),
                        ft.Row([
                            ft.Text("Spatial-peak temporal-average intensity: "),
                            i2text,
                            ft.Text(f" (W/cm^2)"),
                        ])
                    ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(main)
