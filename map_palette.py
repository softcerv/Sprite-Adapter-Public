from PIL import Image
import json
import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Generates mapped sprites using map(s) and a palette JSON.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("src_map", help="The map(s) that we want to apply the palette to")
parser.add_argument("src_json", help="The JSON palette that we want to use to generate the sprite(s).")
parser.add_argument("-multi", action="store_true",  help="Are we converting multiple files at once? If so, please use a folder for src_map")

maps_folder = "maps"
palettes_folder = "palettes"
results_folder = "final results"

def map_palette(map_to_use, palette_to_use, export_path):
    color_map = Image.open(f"{maps_folder}/{map_to_use}")
    export_map = Image.new("RGBA", (color_map.width, color_map.height))

    with open(f"{palettes_folder}/{palette_to_use}") as json_file:
        palette = json.load(json_file)

    for x in range(color_map.width):
        for y in range(color_map.height):
            pixel = color_map.getpixel((x,y))
            if str(pixel) not in palette:
                continue

            color_string = (palette[str(pixel)])
            rgb = color_string.strip('][)(').split(', ')
            rgb = tuple(map(int, rgb))
            export_map.putpixel((x,y),(rgb))

    export_directory = f"{results_folder}/{palette_to_use[:-5]}"
    if not os.path.exists(export_directory):
        os.makedirs(export_directory)

    export_map.save(f"{export_directory}/{export_path}")

#map_palette("maps/thicc_boobs.png", "palettes/janitor", "janitor")
args = parser.parse_args()

if os.path.exists(fr"{maps_folder}/{args.src_map}") == False:
    print(fr"{args.src_map} does not exist inside of {maps_folder}")
    sys.exit()

if os.path.exists(fr"{palettes_folder}/{args.src_json}") == False:
    print(fr"{args.src_json} does not exist inside of {palettes_folder}.")
    sys.exit()

if not args.src_json.endswith(".json")or (not args.src_map.endswith(".png") and not args.multi):
    print("You are not using the right format for this file.")
    sys.exit()

if args.multi == True:
    file_list = os.listdir(fr"{maps_folder}/{args.src_map}")
    for file in file_list:
        if file.endswith(".json"):
            continue

        map_palette(fr"{args.src_map}/{file}", fr"{args.src_json}", fr"{file}")
else:
        map_palette(fr"{args.src_map}", fr"{args.src_json}", fr"{args.src_map}")
