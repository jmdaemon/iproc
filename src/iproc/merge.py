from PIL import Image

def cat(im1: Image, im2: Image, dim: tuple, append_on: tuple):
    '''
    Concatenates two images together
    im1         : PIL.Image of the first image
    im2         : PIL.Image of the second image
    dim         : Dimensions of the output image
    append_on   : Dimensions on where to paste the second image to the first image
    '''
    dst = Image.new('RGB', dim)
    dst.paste(im1, (0, 0))
    dst.paste(im2, append_on)
    return dst

def merge(imagefp1, imagefp2, outputfp, attach='h'):
    '''
    Merges two images together
    imagefp1: File path to the first image
    imagefp2: File path to the second image
    outputfp: File path to the output image
    attach:   Attach images horizontally (landscape) or vertically (portrait) mode
    '''
    im1 = Image.open(imagefp1)
    im2 = Image.open(imagefp2)

    dim         = (0,0)
    append_on   = (0,0)
    match attach:
        case 'h':
            dim = (im1.width + im2.width, im1.height)
            append_on = (im1.width, 0)
        case 'v':
            dim = (im1.width, im1.height + im2.height)
            append_on = (0, im1.height)
    cat(im1, im2, dim, append_on)
