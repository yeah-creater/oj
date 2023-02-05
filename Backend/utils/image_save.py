from PIL import Image

def save(path):
    img = Image.open(path)
    width, height = img.size  # Get dimensions

    if width > 300 and height > 300:
        # keep ratio but shrink down
        img.thumbnail((width, height))

    # check which one is smaller
    if height < width:
        # make square by cutting off equal amounts left and right
        left = (width - height) / 2
        right = (width + height) / 2
        top = 0
        bottom = height
        img = img.crop((left, top, right, bottom))

    elif width < height:
        # make square by cutting off bottom
        left = 0
        right = width
        top = 0
        bottom = width
        img = img.crop((left, top, right, bottom))

    if width > 300 and height > 300:
        img.thumbnail((300, 300))

    img.save(path)