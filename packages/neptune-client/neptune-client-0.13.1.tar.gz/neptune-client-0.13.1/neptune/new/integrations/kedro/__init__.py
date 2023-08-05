#
# Copyright (c) 2021, Neptune Labs Sp. z o.o.
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
#

try:
    # pylint: disable=import-error
    from kedro_neptune import *
except ModuleNotFoundError as e:
    if e.name == 'kedro_neptune':
        from neptune.new.exceptions import NeptuneIntegrationNotInstalledException
        raise NeptuneIntegrationNotInstalledException(
            integration_package_name="kedro-neptune",
            framework_name="kedro"
        ) from None
    else:
        raise
