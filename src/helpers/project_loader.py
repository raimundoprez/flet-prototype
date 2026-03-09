import flet as ft
import io
import csv

from common.app_globals import refs, _
from common.utils import pretty_exception
from helpers.experiment import Experiment, ElementData

class ProjectLoader:
    @staticmethod
    async def load_project(set_image_file, set_experiment):
        file_picker = ft.FilePicker()

        image_files = await file_picker.pick_files(
            dialog_title=_("IMAGE_PICKER_TITLE"),
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["png"],
            allow_multiple=False,
            with_data=True
        )

        if len(image_files) == 1 and image_files[0].bytes:
            image_file = image_files[0]

            experiment_files = await file_picker.pick_files(
                dialog_title=_("EXPERIMENT_PICKER_TITLE"),
                file_type=ft.FilePickerFileType.CUSTOM,
                allowed_extensions=["csv"],
                allow_multiple=False,
                with_data=True
            )

            if len(experiment_files) == 1 and experiment_files[0].bytes:
                experiment_file = experiment_files[0]

                try:
                    experiment = ProjectLoader.parse_experiment(experiment_file.bytes)
                except Exception as e:
                    refs["logger"].error(pretty_exception("Error parsing a project data file", e))

                    ft.context.page.show_dialog(ft.AlertDialog(
                        title=_("PROJECT_LOADER_FAILED_TITLE"),
                        shape=ft.RoundedRectangleBorder(radius=0),
                        content=ft.Text(_("PROJECT_LOADER_FAILED_DESCRIPTION")),
                        actions=[ft.TextButton(_("PROJECT_LOADER_FAILED_DISMISS"), on_click=lambda _: ft.context.page.pop_dialog())]
                    ))

                    return
                
                refs["logger"].info(f'Project image loaded: {image_file.name=}, {image_file.size=}')
                refs["logger"].info(f'Project data loaded: {len(experiment.positions)=}, {len(experiment.elements_data)=}')
                
                set_image_file(image_file)
                set_experiment(experiment)
    
    @staticmethod
    def parse_experiment(bytes: bytes) -> Experiment:
        text = bytes.decode("utf-8") # decode the bytes array into a utf-8 string
        file = io.StringIO(text) # create an in-memory file with the former string
        reader = csv.reader(file, delimiter=";") # parse the in-memory csv file and fetch its rows

        # skip the first 14 rows
        for _ in range(14):
            next(reader, None)
        
        # store the remaining rows in a standard list
        rows = []

        for row in reader:
            rows.append(row)

        positions = []
        elements_data = []

        if len(rows):
            # get all the positions of the experiment (row 0)
            for i in range(2, len(rows[0])):
                position = int(rows[0][i])
                positions.append(position)
            
            # get all elements and its measurements (each element must have at least as many measurements as positions exist)
            # rows 1 and 2 are skipped
            for i in range(3, len(rows)):
                if len(rows[i]) >= (2 + len(positions)):
                    name = rows[i][0].strip() + " - " + rows[i][1].strip()
                    measurements = []

                    for j in range(2, 2 + len(positions)):
                        measurement = float(rows[i][j])
                        measurements.append(measurement)
                    
                    element_data = ElementData(name, measurements)
                    elements_data.append(element_data)
        
        return Experiment(positions=positions, elements_data=elements_data)