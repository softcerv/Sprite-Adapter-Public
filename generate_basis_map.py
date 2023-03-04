from PIL import Image
import colorsys
import argparse
import os
import sys

parser = argparse.ArgumentParser(description="Generates a map, that can be used as a basis for other maps, from the input image. The image used will need to be pure red (255, 0, 0).",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "src_img", help="The image that we want to convert into a texture map")

source_directory = "source images"
results_directory = "maps"

def generate_map(map_name):
    image1 = Image.open(fr"{source_directory}/{map_name}")

    min_y = image1.height + 1
    max_y = 0

    min_x = image1.width + 1
    max_x = 0

    for x in range(image1.width):
        for y in range(image1.height):
            pixel = image1.getpixel((x,y))
            if(pixel[3] == 255):
                if(x < min_x):
                    min_x = x
                
                if(x > max_x):
                    max_x = x

                if(y < min_y):
                    min_y = y 
                
                if(y > max_y):
                    max_y = y

    width = (max_x - min_x) + 1
    height = (max_y - min_y) + 1

    #How much is the hue being decreased by each x level?
    hue_step = (0.9 / width)
    #How much is the saturation being decreased by each y level?
    satuartion_step = (0.9 / height)
    
    current_hue = 1
    current_saturation = 1

    #Replaces the mask with actual color mappings
    for x in range(min_x, (max_x + 1)):
        for y in range(min_y, (max_y + 1)):
            pixel = image1.getpixel((x,y))
            if(pixel[0] == 255):
                r, g, b  = colorsys.hsv_to_rgb(current_hue, current_saturation, 1)
                
                r = int(r * 255)
                g = int(g * 255)
                b = int(b * 255)

                image1.putpixel((x,y), (r, g, b, 255))
            current_saturation -= satuartion_step

        current_hue -= hue_step
        current_saturation = 1             

    #Creates a reference image which contains all the colors we are going to use.

    ref_width = 0
    if(width > height):
        ref_width = width

    else:
        ref_width = height

    ref = Image.new("RGB",[ref_width,2])

    current_hue = 1
    for x in range(width):
        pixel = ref.getpixel((x,0))
        r, g, b  = colorsys.hsv_to_rgb(current_hue, 1, 1)
        
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        ref.putpixel((x,0), (r, g, b, 255))
        current_hue -= hue_step

    current_saturation = 1
    for x in range(height):
        pixel = ref.getpixel((x,1))
        r, g, b  = colorsys.hsv_to_rgb(1, current_saturation, 1)
        
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)

        ref.putpixel((x,1), (r, g, b, 255))
        current_saturation -= satuartion_step 

    if (os.path.exists(results_directory) == False):
        os.makedirs(results_directory)

    image1.save(fr"{results_directory}/{map_name}")
    ref.save(fr"{results_directory}/{map_name[:-4]}_ref.png")


#generate_map("base_template.png")
args = parser.parse_args()

source_file = fr"{source_directory}/{args.src_img}"

if os.path.exists(source_file) == False:
    print(fr"{args.src_img} does not exist inside of {source_directory}")
    sys.exit()

generate_map(fr"{args.src_img}")
