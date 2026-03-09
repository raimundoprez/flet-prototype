from os import scandir
from gettext import translation
from logging import Logger
from typing import List, Optional

from common.utils import pretty_exception

class Translator:
    def __init__(self, domain: str, locale_dir: str, default_lang: str, logger: Logger):
        """
        Initializes a Translator instance with the parameters given.

        Args:
            domain (str): The selected name for .po files (all the languages used should share the same name for their .po file).
            locale_dir (str): The directory where the language directories are located (example: resource/locale).
            default_lang (str): The default language used for translations when no language is provided.
            logger (Logger): A logger object to which error messages will be sent.
        
        Raises:
            FileNotFoundError: If the default language couldn't be registered.
            Exception: If scandir, is_dir, translation or install fail with the parameters given.
        """

        self.default_lang = default_lang
        self.logger = logger

        self.languages = {}

        for entry in scandir(locale_dir):
            if entry.is_dir():
                self.languages[entry.name] = translation(domain, localedir=locale_dir, languages=[entry.name])
                self.languages[entry.name].install()
        
        if self.default_lang not in self.languages:
            raise FileNotFoundError(
                f'The default language {default_lang=} using .po filename {domain=} could not be located in folder {locale_dir=}'
            )
    
    def translate(self, msg_id: str, language: Optional[str], *args, **kwargs) -> str:
        selected_lang = self.validate(language)
        msg_handler = self.languages[selected_lang]
        msg = msg_handler.gettext(msg_id)

        if msg_id in getattr(msg_handler, "_catalog", {}):
            try:
                msg = msg.format(*args, **kwargs)
            except (IndexError, KeyError) as e:
                self.logger.error(pretty_exception(f'Invalid arguments for {msg_id=} and {selected_lang=}: {args=}, {kwargs=}', e))
            except (Exception) as e:
                self.logger.error(pretty_exception(f'Unexpected error for {msg_id=} and {selected_lang=}: {args=}, {kwargs=}', e))
        else:
            self.logger.error(f'{msg_id=} not found in {selected_lang=} translations')
        
        return msg

    def validate(self, language: Optional[str]) -> str:
        if language is not None and language in self.languages:
            return language

        return self.default_lang
    
    def get_default(self) -> str:
        return self.default_lang
    
    def set_default(self, language: str):
        if language in self.languages:
            self.default_lang = language
    
    def get_languages(self) -> List[str]:
        return list(self.languages.keys())