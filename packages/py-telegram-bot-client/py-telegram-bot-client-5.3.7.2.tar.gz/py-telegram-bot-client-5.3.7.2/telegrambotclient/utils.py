import pprint
from functools import wraps
from io import StringIO
from typing import Any, Dict, List, Pattern, Tuple, Union

from telegrambotclient.base import TelegramBotException

try:
    import ujson as json
except ImportError:
    import json


def exclude_none(**kwargs) -> Dict:
    return {key: value for key, value in kwargs.items() if value is not None}


_pp = pprint.PrettyPrinter(indent=2)


def pretty_print(data: Any):
    _pp.pprint(data)


def pretty_format(data: Dict) -> str:
    return _pp.pformat(data)


def regex_match(regex_patterns: Union[List[Pattern], Tuple[Pattern]]):
    def decorate(method):
        @wraps(method)
        def wrapper(bot, message, *args, **kwargs):
            if message.text:
                for pattern in regex_patterns:
                    match_result = pattern.match(message.text)
                    if match_result:
                        return method(bot, message, *args, match_result,
                                      **kwargs)
            return bot.next_call

        return wrapper

    return decorate


def i18n(default_lang_code: str = "en"):
    def decorate(method):
        @wraps(method)
        def wrapper(bot, data, *args, **kwargs):
            def _(text,
                  lang_code=data.from_user.language_code
                  if data.from_user else default_lang_code):
                return bot.get_text(lang_code, text)

            kwargs.update({"_": _})
            return method(bot, data, *args, **kwargs)

        return wrapper

    return decorate


def build_callback_data(name: str, *value) -> str:
    data = "{0}|{1}".format(name, json.dumps(value))
    bytes_len = len(data.encode("utf-8"))
    if bytes_len > 64:
        raise TelegramBotException(
            "callback_data must be 1-64 bytes. {0}/{1}".format(
                data, bytes_len))
    return data


def parse_callback_data(callback_data: str, name: str):
    callback_name_value = callback_data.split("|")
    if len(callback_name_value) == 2:
        callback_name, callback_value = tuple(callback_name_value)
        if callback_name == name:
            return tuple(json.loads(callback_value))
    return (None, )


def compose_message_entities(text_entities: Union[List, Tuple],
                             sep: str = " "):
    with StringIO() as buffer_:
        entities = []
        for text_entity in text_entities:
            if isinstance(text_entity, str):
                buffer_.write(text_entity)
                buffer_.write(sep)
                continue
            text, entity = tuple(text_entity)
            entity["offset"] = buffer_.tell()
            entities.append(entity)
            if isinstance(text, str):
                buffer_.write(text)
                buffer_.write(sep)
                entity["length"] = len(text)
            elif isinstance(text, (list, tuple)):
                inner_text, inner_entities = compose_message_entities(text)
                offset = buffer_.tell()
                for inner_entity in inner_entities:
                    inner_entity["offset"] += offset
                buffer_.write(inner_text)
                buffer_.write(sep)
                entities += inner_entities
                entity["length"] = len(inner_text)
        return buffer_.getvalue(), tuple(entities)
