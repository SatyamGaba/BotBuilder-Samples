#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANTID = os.environ.get("MicrosoftAppTenantId", "")
    ENDPOINT = 'https://sampleangservice2.cognitiveservices.azure.com/'
    API_KEY = 'Fz5VK3EztRTFNBpQQemY7rT8k8bIirH3UjWER8KgqxSYuct6SpBsJQQJ99BEACYeBjFXJ3w3AAAaACOG3ge3'
