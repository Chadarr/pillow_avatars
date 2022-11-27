from PIL import Image

CROP_SIZE = 25  # in px
IN_IMAGE_NAME = 'monro.jpg'
OUT_IMAGE_NAME = 'out.jpg'
OUT_THUMB_IMAGE_NAME = 'out_thumbnail.jpg'

image = Image.open(IN_IMAGE_NAME)
red_image, blue_image, green_image = image.split()

left_crop_coordinates = (CROP_SIZE * 2, 0, image.width, image.height)
mid_crop_coordinates = (CROP_SIZE, 0, image.width - CROP_SIZE, image.height)
right_crop_coordinates = (0, 0, image.width - CROP_SIZE * 2, image.height)

red_image_left = red_image.crop(left_crop_coordinates)
red_image_mid = red_image.crop(mid_crop_coordinates)
red_image_blend = Image.blend(red_image_left, red_image_mid, 0.5)

blue_image_right = blue_image.crop(right_crop_coordinates)
blue_image_mid = blue_image.crop(mid_crop_coordinates)
blue_image_blend = Image.blend(blue_image_right, blue_image_mid, 0.5)

green_image_mid = green_image.crop(mid_crop_coordinates)

image_merge_band = (red_image_blend, green_image_mid, blue_image_blend)
new_image = Image.merge('RGB', image_merge_band)
new_image.save(OUT_IMAGE_NAME)

new_image.thumbnail((80, 80))
new_image.save(OUT_THUMB_IMAGE_NAME)
