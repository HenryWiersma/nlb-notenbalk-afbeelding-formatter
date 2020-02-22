"""
File:         nlb-notenbalk-afbeelding-formatter.py
Created:      2020-02-14
Last Changed: 2020-02-22
Author(s):    H.H.Wiersma

Code to create distribution plot and a mask image used in the research plan
Copyright (C) 2019 H.H.Wiersma

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A copy of the GNU General Public License can be found in the LICENSE file in the
root directory of this source tree. If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import os
import glob
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def main():
    args = parse_arguments()
    print(args)
    formatter(args.input, args.font)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Format the NLB notebalk afbeeldingen naar '
                    'full-HD formaat (1920 / 1080px)')

    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='an integer for the accumulator')
    parser.add_argument('-i', '--input',
                        required=True,
                        type=str,
                        help='Geef het path naar de map met de afbeeldingen')
    parser.add_argument('-f', '--font',
                        required=True,
                        type=str,
                        help='Geef het path naar de font ttf bestand')
    return parser.parse_args()


def formatter(image_path, font_file_path, image_size=None):
    if image_size is None:
        image_size = [1920, 1080]

    # rgb color of the title and shadow
    text_color = (220, 220, 0)
    shadow_color = (10, 10, 10)

    song_paths = glob.glob(os.path.join(image_path, "*.png"))

    # create output dir
    output_dir = os.path.join(image_path, "output/")
    if os.path.isdir(output_dir) is False:
        os.mkdir(output_dir)

    for song_path in song_paths:
        # parse image name
        song_file_name = os.path.basename(song_path)
        print("process: {}".format(song_file_name))
        song_name = ".".join(song_file_name.split(".")[:-1])
        name_items = song_name.split("-")
        song_number = name_items[1]
        if name_items[3] == "couplet":
            couplet_number = name_items[4]
        elif name_items[3] == "nl":
            couplet_number = "1"
        else:
            couplet_number = "1 ({})".format(name_items[3])

        if couplet_number == "0":
            couplet_number = "refrein"

        # read the orginal image
        org_img = np.array(Image.open(song_path))
        org_img = org_img[:, :, :3]

        # create new image
        new_img = np.ones((image_size[1],
                           image_size[0], 3), dtype=np.uint8) * 255

        # Place the original image in the new image
        org_img_cut = org_img[140:-140, 70:-70, :]
        nh, nw, _ = new_img.shape
        h, w, _ = org_img_cut.shape
        new_img[140:140+h, 70:70+w, :] = org_img_cut

        # add text to image
        img_pil = Image.fromarray(new_img)
        draw = ImageDraw.Draw(img_pil)

        font = ImageFont.truetype(font_file_path, 66)
        text = "NLB {song_number} : {couplet_number}".format(
            song_number=song_number,
            couplet_number=couplet_number
        )
        x = 70
        y = 50

        # create the dark border
        draw.text((x - 2, y - 2), text, font=font, fill=shadow_color)
        draw.text((x + 2, y - 2), text, font=font, fill=shadow_color)
        draw.text((x - 2, y + 2), text, font=font, fill=shadow_color)
        draw.text((x + 2, y + 2), text, font=font, fill=shadow_color)

        # now draw the text over it
        draw.text((x, y), text, font=font, fill=text_color)

        # Save the image
        img_pil.save(os.path.join(output_dir, song_file_name))
        print("Image created: {}".format(text))


if __name__ == '__main__':
    main()
