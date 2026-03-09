import flet as ft

@ft.component
def WorkmodeTabBar():
    icon_list = [
        "move.png",
        "scatter_chart.png",
        "lines_chart.png",
        "bars_chart.png",
        "stacked_bars_chart.png",
        "linear_correlation_chart.png",
        "transposed_linear_correlation_chart.png",
        "correlation_heatmap_chart.png",
        "transposed_correlation_heatmap_chart.png"
    ]

    return ft.TabBar(
        label_padding=5,
        tabs=[
            ft.Tab(label=ft.Image(src=f'/icons/{icon}', width=50, height=50), height=50)
            for icon in icon_list
        ]
    )