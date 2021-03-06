############################################################################
# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############################################################################
# pylint: disable=locally-disabled, invalid-name, missing-docstring
"""g++ compiler configuration for size
"""
from parts.config import ConfigValues, configuration


def map_default_version(env):
    return env['GCC_VERSION']


config = configuration(map_default_version)

config.VersionRange(
    "3-*",
    append=ConfigValues(
        CCFLAGS=[
            '',
            # size optimization
            '-Os',
            '-fdata-sections',
            '-ffunction-sections',
            # treat warnings as errors
            '-Werror',
            # enable all warnings
            '-Wall',
            # extra warnings
            '-Wextra',
            '-Wformat',
            '-Wformat-security',
            '-fstack-protector',
        ],
        CXXFLAGS=[
            '',
            # modern C++ features support
            '-std=gnu++11'
        ],
        CPPDEFINES=['NDEBUG', '_FORTIFY_SOURCE=2', '__int64=long long'],
        LINKFLAGS=[
            '-fstack-protector',
            # link only what is used
            '-Xlinker',
            '--gc-sections'
        ], ))
