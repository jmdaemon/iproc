import argparse
import numpy as np
from PIL import Image

brailles = ['⠀', '⠁', '⠂', '⠃'  , '⠄', '⠅', '⠆', '⠇'    , '⠈', '⠉', '⠊', '⠋'    , '⠌', '⠍', '⠎', '⠏',
            '⠐', '⠑', '⠒', '⠓'  , '⠔', '⠕', '⠖', '⠗'    , '⠘', '⠙', '⠚', '⠛'    , '⠜', '⠝', '⠞', '⠟',
            '⠠', '⠡', '⠢', '⠣'  , '⠤', '⠥', '⠦', '⠧'    , '⠨', '⠩', '⠪', '⠫'    , '⠬', '⠭', '⠮', '⠯',
            '⠰', '⠱', '⠲', '⠳'  , '⠴', '⠵', '⠶', '⠷'    , '⠸', '⠹', '⠺', '⠻'    , '⠼', '⠽', '⠾', '⠿',
            '⡀', '⡁', '⡂', '⡃'  , '⡄', '⡅', '⡆', '⡇'    , '⡈', '⡉', '⡊', '⡋'    , '⡌', '⡍', '⡎', '⡏',
            '⡐', '⡑', '⡒', '⡓'  , '⡔', '⡕', '⡖', '⡗'    , '⡘', '⡙', '⡚', '⡛'    , '⡜', '⡝', '⡞', '⡟',
            '⡠', '⡡', '⡢', '⡣'  , '⡤', '⡥', '⡦', '⡧'    , '⡨', '⡩', '⡪', '⡫'    , '⡬', '⡭', '⡮', '⡯',
            '⡰', '⡱', '⡲', '⡳'  , '⡴', '⡵', '⡶', '⡷'    , '⡸', '⡹', '⡺', '⡻'    , '⡼', '⡽', '⡾', '⡿',
            '⢀', '⢁', '⢂', '⢃'  , '⢄', '⢅', '⢆', '⢇'    , '⢈', '⢉', '⢊', '⢋'    , '⢌', '⢍', '⢎', '⢏',
            '⢐', '⢑', '⢒', '⢓'  , '⢔', '⢕', '⢖', '⢗'    , '⢘', '⢙', '⢚', '⢛'    , '⢜', '⢝', '⢞', '⢟',
            '⢠', '⢡', '⢢', '⢣'  , '⢤', '⢥', '⢦', '⢧'    , '⢨', '⢩', '⢪', '⢫'    , '⢬', '⢭', '⢮', '⢯',
            '⢰', '⢱', '⢲', '⢳'  , '⢴', '⢵', '⢶', '⢷'    , '⢸', '⢹', '⢺', '⢻'    , '⢼', '⢽', '⢾', '⢿',
            '⣀', '⣁', '⣂', '⣃'  , '⣄', '⣅', '⣆', '⣇'    , '⣈', '⣉', '⣊', '⣋'    , '⣌', '⣍', '⣎', '⣏',
            '⣐', '⣑', '⣒', '⣓'  , '⣔', '⣕', '⣖', '⣗'    , '⣘', '⣙', '⣚', '⣛'    , '⣜', '⣝', '⣞', '⣟',
            '⣠', '⣡', '⣢', '⣣'  , '⣤', '⣥', '⣦', '⣧'    , '⣨', '⣩', '⣪', '⣫'    , '⣬', '⣭', '⣮', '⣯',
            '⣰', '⣱', '⣲', '⣳'  , '⣴', '⣵', '⣶', '⣷'    , '⣸', '⣹', '⣺', '⣻'    , '⣼', '⣽', '⣾', '⣿']

def preprocess(fp):
    image = Image.open(fp, 'r')
    # Greyscale the image (L == Luminance)
    image.convert('L')
    image = image.convert(mode="1")
    return image

def braillify(image: Image, brailles: list):
    pix = np.array(image)
    mat = np.array([[0, 3],
                    [1, 4],
                    [2, 5],
                    [6, 7]])
    mat = 2**mat
    out = ""
    for i in range(0, pix.shape[0], 4):
        for j in range(0, pix.shape[1], 2):
            window: np.array = pix[i:i+4, j:j+2] # 4 x 2
            window = window * mat
            out += brailles[window.sum()]
        out += "\n"
    return out

def main():
    parser = argparse.ArgumentParser(description='Executable file for Labs')
    parser.add_argument('image'     , type=str, help='File path to the current lab directory')

    args = parser.parse_args()

    imagefp = args.image
    image = preprocess(imagefp)

    print(braillify(image, brailles))
