# load environment variables on start so that they are available across all the project files
from dotenv import load_dotenv
load_dotenv()

# disable marshmallow dump_default warning
import warnings
warnings.filterwarnings("ignore", message="The 'default' argument to fields is deprecated. Use 'dump_default' instead.")

import flet as ft
import os

from common.app_globals import refs
from common.logger_factory import LoggerFactory
from common.translator import Translator
from common.utils import pretty_exception
from components.app import App

try:
    error_message = None

    logger_name = os.getenv("LOGGER_NAME")
    logger_level = int(os.getenv("LOGGER_LEVEL"))
    logger_trace_screen = os.getenv("LOGGER_TRACE_SCREEN") == "true"
    logger_trace_file = os.getenv("LOGGER_TRACE_FILE") == "true"
    logger_file_path = logger_trace_file and os.getenv("LOGGER_FILE_PATH") or None

    logger = LoggerFactory.create(logger_name, logger_level, logger_trace_screen, logger_file_path)
    refs["logger"] = logger

    translator_domain = os.getenv("TRANSLATOR_DOMAIN")
    translator_locale_dir = os.getenv("TRANSLATOR_LOCALE_DIR")
    translator_default_lang = os.getenv("TRANSLATOR_DEFAULT_LANG")

    translator = Translator(translator_domain, translator_locale_dir, translator_default_lang, logger)
    refs["translator"] = translator
    
    logger.info("Flet application started successfully.")
except Exception as e:
    error_message = pretty_exception("Error trying to initialize the application", e)

if error_message:
    ft.run(lambda page: page.add(ft.Text(error_message)))
else:
    ft.run(lambda page: page.render(App))