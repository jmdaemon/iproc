from PIL import Image

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def merge(imagefp1, imagefp2, outputfp, attach='h'):
    im1 = Image.open(imagefp1)
    im2 = Image.open(imagefp2)
    match attach:
        case 'h': get_concat_h(im1, im2).save(outputfp)
        case 'v': get_concat_v(im1, im2).save(outputfp)
