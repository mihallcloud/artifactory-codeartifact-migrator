# Copyright 2022 Shawn Qureshi and individual contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, List, Tuple
from . import replicator
from . import argprocess

def dispatch(argv: List[str]) -> Any:
  """
  dispatch does the official cli functions.

  :param argv: List of arguments passed to cli command
  """

  args = argprocess.getArgs()
  replicator.replicate(args)
