# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RefreshIndexAdvancedInfoItem(Model):
    """RefreshIndexAdvancedInfoItem.

    :param key_one: Key parameter to describe advanced info.
    :type key_one: str
    :param key_two: Key parameter to describe advanced info.
    :type key_two: str
    """

    _attribute_map = {
        'key_one': {'key': 'key One', 'type': 'str'},
        'key_two': {'key': 'key Two', 'type': 'str'},
    }

    def __init__(self, key_one=None, key_two=None):
        self.key_one = key_one
        self.key_two = key_two
