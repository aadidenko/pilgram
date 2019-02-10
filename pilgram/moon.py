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

from image4layer import Image4Layer
from PIL import ImageEnhance, ImageChops

from pilgram import css
from pilgram import util


def moon(im):
    cb = im.convert('RGB')

    cs1 = util.fill(cb.size, [160, 160, 160])
    cs = Image4Layer.soft_light(cb, cs1)

    cs2 = util.fill(cb.size, [56, 56, 56])
    cr = ImageChops.lighter(cs, cs2)

    cr = css.grayscale(cr)
    cr = ImageEnhance.Contrast(cr).enhance(1.1)
    cr = ImageEnhance.Brightness(cr).enhance(1.1)

    return cr.convert(im.mode)