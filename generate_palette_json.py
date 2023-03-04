from PIL import Image
import json
import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Generates a  palette JSON using the inputed source map and target sprite", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("src_map", help="The original map that the sprites were designed to fit")
parser.add_argument("target_sprite", help="The sprite that we are attempting to create a palette JSON for.")
parser.add_argument("-multi", action="store_true",  help="Are we converting multiple files at once? If so, please use a folder for target_sprite")

maps_folder = "maps"
sprites_folder = "sprites to convert"
export_folder = "palettes"

def generate_pallete(map_file, source_file, export_json):
    source_image = Image.open(source_file)
    source_map = Image.open(map_file)

    if(source_image.width != source_map.width or source_image.height != source_map.height):
        return False

    color_dict = {}

    for x in range(source_image.width):
        for y in range(source_image.height):
            source_pixel = source_image.getpixel((x,y))
            if(source_pixel[3] == 0):
                continue

            map_pixel = source_map.getpixel((x,y))

            color_dict[str(map_pixel)] = str(source_pixel)

    with open(f"{export_json}.json", "w") as outfile:
        json.dump(color_dict, outfile)


#generate_pallete("source images/janitor.png","results/test.png", "janitor-front")
args = parser.parse_args()

map_file = fr"{maps_folder}/{args.src_map}"
sprite_file = fr"{sprites_folder}/{args.target_sprite}"

if os.path.exists(map_file) == False:
    print(fr"{args.src_map} does not exist inside of {maps_folder}")
    sys.exit()

if os.path.exists(sprite_file) == False:
    print(fr"{args.target_sprite} does not exist inside of {sprites_folder}.")
    sys.exit()

if not args.src_map.endswith(".png")or (not args.target_sprite.endswith(".png") and not args.multi):
    print("You need to use a PNG for this file.")
    sys.exit()

if args.multi == True:
    file_list = os.listdir(sprite_file)
    for file in file_list:
        generate_pallete(fr"{maps_folder}/{args.src_map}", fr"{sprites_folder}/{args.target_sprite}/{file}", fr"palettes/{file[:-4]}")
else:
    generate_pallete(fr"{maps_folder}/{args.src_map}", fr"{sprites_folder}/{args.target_sprite}", fr"palettes/{args.target_sprite[:-4]}")
