# Copyright 2019 Akiomi Kamakura
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

from pilgram.util.fill import fill
from pilgram.util.invert import invert
from pilgram.util.or_convert import or_convert
from pilgram.util.linear_gradient import linear_gradient, linear_gradient_mask
from pilgram.util.radial_gradient import radial_gradient, radial_gradient_mask


__all__ = [
    'fill', 'invert', 'or_convert',
    'linear_gradient', 'linear_gradient_mask',
    'radial_gradient', 'radial_gradient_mask',
]
