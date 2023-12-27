from PIL import Image

greys = (' ', '.', '-', '"', 'r', '/', '>', ')', '[', 'I', 'Y', 'Z', 'h', '#', '8', '@')


# in_place: Defines whether the function should just print the ascii art as its processed,
#           or if it should return the resultant string
def image_to_string(image_file_path, in_place=True, colours=greys):
    image = Image.open(image_file_path)
    loaded_image = image.load()

    # Checks if the image is greyscale or not,
    #   as processing will be done differently if it is
    greyscale = isinstance(loaded_image[0, 0], int)

    if not in_place:
        image_list = []

    # Iterate through every pixel in the image
    for y in range(image.height):
        for x in range(image.width):
            # Find the average colour of the pixel
            # If the image is greyscale, the average colour is just the value of the pixel
            average_colour = loaded_image[x, y] if greyscale else sum(loaded_image[x, y][:3])/3
            # Have the average colour end up between 0 and the length of the colours list minus 1
            normalised_colour = round(average_colour / (len(colours) + 1))

            # If you want the function to run in place...
            if in_place:
                # ...just print the pixel as its processed...
                print(colours[normalised_colour] * 2, end="")
            else:
                # ...otherwise add it to the final list

                # (This might throw a warning btw - don't worry,
                #   image_list will always exist if this else statement is reached)
                image_list.append(normalised_colour)

        if in_place:
            print()
        else:
            image_list.append("\n")

    # If you want the function to return a string:
    if not in_place:
        # If the pixel isn't a newline, convert it to its 'colours' equivalent, otherwise, keep it a newline
        # Finally, join the pixels together into one string
        return "".join(map(lambda px: (colours[px] * 2) if px != "\n" else "\n", image_list))
