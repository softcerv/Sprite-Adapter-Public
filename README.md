# Sprite-Adapter-Public 

## What this project is.

This project is my attempt at (somewhat) automating the creation of clothing sprites for different body sizes and shapes for Space Station 13.
While this project is built with making Space Station 13 sprites in mind, this should work for any game that uses small 2D sprites.

## Workflow

### Creating a base map.
To get started, you will need to create a base map. This map is what all other maps after will be based on.

To do this, open your image editor of choice, and create a red (255, 0 ,0) mask over the pixels that you wish to have mapped.
Once this is done, save the image as a 32 Bit PNG and move the image to the `source images` folder

IMAGE HERE

 Open up the base directory for this project in the terminal and type in the following command

```
    python generate_basis_map.py [YOUR FILE NAME HERE].png
```

Assuming the file is present and the program has successfully ran, there should be a new file with the same name as the source file inside of the maps folder.
