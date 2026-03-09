import flet as ft

from common.app_globals import _
from helpers.experiment import Experiment

@ft.component
def ElementsSelector(experiment: Experiment):
    items = []
    selected = set()

    for i in range(len(experiment.elements_data)):
        id = i + 1

        items.append({
            "id": id,
            "name": experiment.elements_data[i].name
        })

        if experiment.elements_data[i].active:
            selected.add(id)

    sort_column_index, set_sort_column_index = ft.use_state(0)
    sort_ascending, set_sort_ascending = ft.use_state(True)
    
    sorting_funcs = {
        0: lambda item: item["id"],
        1: lambda item: item["name"].lower()
    }

    items.sort(key=sorting_funcs[sort_column_index], reverse=not sort_ascending)
    
    def handle_row_selection_change(e):
        row = e.control
        id = row.data
        selected = e.data
        experiment.toggle_element(id, selected)
    
    def handle_select_all(e):
        selected = e.data
        experiment.toggle_elements(selected)

    def handle_column_sort(e: ft.DataColumnSortEvent):
        set_sort_column_index(e.column_index)
        set_sort_ascending(e.ascending)

    return ft.Container(
        expand=True,
        bgcolor="#F2F2F2",
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=ft.DataTable(
                heading_row_color="#E2E2E2",
                heading_row_height=50,
                divider_thickness=1,
                vertical_lines=ft.border.BorderSide(1, ft.Colors.OUTLINE_VARIANT),
                horizontal_lines=ft.border.BorderSide(1, ft.Colors.OUTLINE_VARIANT),
                show_checkbox_column=True,
                show_bottom_border=True,
                sort_column_index=sort_column_index,
                sort_ascending=sort_ascending,
                on_select_all=handle_select_all,
                columns=[
                    ft.DataColumn(
                        label=ft.Text(_("ELEMENTS_TAB_ID"), color=ft.Colors.BLACK),
                        on_sort=handle_column_sort
                    ),
                    ft.DataColumn(
                        label=ft.Text(_("ELEMENTS_TAB_ELEMENT"), color=ft.Colors.BLACK),
                        on_sort=handle_column_sort
                    )
                ],
                rows=[
                    ft.DataRow(
                        selected=item["id"] in selected,
                        data=item["id"] - 1,
                        on_select_change=handle_row_selection_change,
                        cells=[
                            ft.DataCell(ft.Text(item["id"], color=ft.Colors.BLACK)),
                            ft.DataCell(ft.Text(item["name"], color=ft.Colors.BLACK))
                        ]
                    )
                    for item in items
                ],
                data_row_color={
                    ft.ControlState.HOVERED: ft.Colors.with_opacity(0.13, ft.Colors.PRIMARY),
                    ft.ControlState.SELECTED: ft.Colors.with_opacity(0.40, ft.Colors.PRIMARY)
                }
            )
        )
    )