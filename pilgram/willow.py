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
from PIL import ImageEnhance

from pilgram import css
from pilgram import util


def willow(im):
    cb = im.convert('RGB')

    cs = util.radial_gradient(
            cb.size,
            [212, 169, 175], [0, 0, 0],
            length=.55, scale=1.5)
    cs = Image4Layer.overlay(cb, cs)

    cs_ = util.fill(cb.size, [216, 205, 203])
    cr = Image4Layer.color(cs, cs_)

    cr = css.grayscale(cr, .5)
    cr = ImageEnhance.Contrast(cr).enhance(.95)
    cr = ImageEnhance.Brightness(cr).enhance(.9)

    return cr.convert(im.mode)