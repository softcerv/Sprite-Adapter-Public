# Sprite-Adapter-Public 

## What this project is.

This project is my attempt at (somewhat) automating the creation of clothing sprites for different body sizes and shapes for Space Station 13.
While this project is built with making Space Station 13 sprites in mind, this should work for any game that uses small 2D sprites.

## Getting started
Before running this project, you will need to have Python installed, along with an image editor of some kind.

In additon, you will need these libraries installed:

    - pillow 
    - argparse

### Creating a base map.
To get started, you will need to create a base map. This map is what all other maps after will be based on.

To do this, open your image editor of choice, and create a red (255, 0 ,0) mask over the pixels that you wish to have mapped.
Once this is done, save the image as a 32 Bit PNG and move the image to the `source images` folder

![image](https://user-images.githubusercontent.com/68373373/222924151-a81dc708-ded8-4d88-b482-6a9775cffb79.png)

This is a map that I made based off the normal SS13 human. This covers all of the areas that a jumpsuit would typically cover.

 Open up the base directory for this project in the terminal and type in the following command

```
    python generate_basis_map.py [YOUR FILE NAME HERE].png
```

Assuming the file is present and the program has successfully ran, there should be a new file with the same name as the source file inside of the `maps` folder.

![image](https://user-images.githubusercontent.com/68373373/222924299-2742ff5e-27fa-490d-a03c-241851f7090b.png)

This will also generate a reference PNG that contains all of the different hue and saturation values used by the map.
![image](https://user-images.githubusercontent.com/68373373/222924327-a9c44066-c2f5-49fb-9955-e491b30d9dc4.png)


### Making a new map.
Now that you have your base map finished, you can get to work on making a map to use with it. This will probably be the most time consuming part of this process.

For additonal maps, you will want to use the base map you created as a template that you can stretch to fit the other maps you want to make.

IMAGE HERE

After the new map is done, save it to the maps folder. It is likely that you will need to modify the map based on the results.

### Making a palette
Palettes are JSONs that represent the sprites that you want to transform, they are used when mapping sprites.

To create a palette, you will need a base map and a 32-bit PNG for the texture that you wish to use.

 Open up the base directory for this project in the terminal and type in the following command
 ```
    python generate_palette_json.py [YOUR SOURCE MAP] [THE SPRITE YOU WANT TO MAKE INTO A PALETTE]
 ```

 This will convert the sprite into a JSON file that can be applied to other maps.
 If you want to convert multiple sprites into palettes, you will need to add `-multi` to the end of the command and use a folder instead of a PNG for the sprites you want to convert.

The resulting files will end up inside of the `palettes` folder

 ### Creating the final images.
 After you have a palette and a map to use it with, you can begin the final step.

  Open up the base directory for this project in the terminal and type in the following command
 ```
    python map_palette.py [THE MAP THAT YOU WISH TO USE] [THE PALETTE YOU WANT TO USE]
 ```

 If you want to map multiple maps, you will need to add `-multi` to the end of the command and use a folder instead of a PNG for the maps you wish to use. 

IMAGE HERE

Assuming that everything has run correctly, the resulting files should be inside of the final results folder
