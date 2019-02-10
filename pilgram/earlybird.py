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
from PIL import Image, ImageEnhance

from pilgram import css
from pilgram import util


def earlybird(im):
    cb = im.convert('RGB')

    cs = util.radial_gradient(cb.size, [208, 186, 142], [54, 3, 9], length=.2)

    gradient_mask = util.radial_gradient_mask(cb.size, length=.85)
    cs_ = util.fill(cb.size, [29, 2, 16])
    cs = Image.composite(cs, cs_, gradient_mask)
    cr = Image4Layer.overlay(cb, cs)

    cr = ImageEnhance.Contrast(cr).enhance(.9)
    cr = css.sepia(cr, .2)

    return cr.convert(im.mode)