# _*_ coding: utf-8 _*_

'''
util_funcs.py by ckm
'''

import re
import urllib.parse
from .util_config import CONFIG_URL_LEGAL_PATTERN, CONFIG_MESSAGE_PATTERN, CONFIG_HEADERS_SET

__all__ = [
    "check_url_legal",
    "get_string_num",
    "get_string_strip",
    "get_url_legal",
    "get_url_params",
    "get_dict_buildin",
    "parse_error_info",
    "parse_raw_request",
]


def check_url_legal(url):
    """
    check that a url is legal or not
    :param url:
    :return:
    """
    return True if re.match(CONFIG_MESSAGE_PATTERN, url, flags=re.IGNORECASE) else False


def get_string_num(string, ignore_sign=False):
    '''
    get a float number from a string
    :param string:
    :param ignore_sign:
    :return:
    '''
    string_re = re.search(r"(?P<sign>-?)(?P<num>\d+(\.\d+)?)", string.replace(",", ""), flags=re.IGNORECASE)
    return float((string_re.group("sign") if not ignore_sign else "") + string_re.group("num")) if string_re else None


def get_string_strip(string, replace_char=" "):
    """
    get a string which striped \t, \r, \n from a string, also change None to ""
    """
    return re.sub(r"\s+", replace_char, string, flags=re.IGNORECASE).strip() if string else ""