import argparse
from iproc.braillify import preprocess, braillify
from iproc.merge import merge

def main():
    parser = argparse.ArgumentParser(description='Executable file for Labs')
    parser.add_argument('cmd' , type=str, help='File path to the current lab directory')
    parser.add_argument('opts', help='Apply string manipulation', nargs=argparse.REMAINDER, default=None)
    args = parser.parse_args()

    cmd     = args.cmd
    opts    = args.opts

    match cmd:
        case 'braillify':
            fp = opts[0]
            braillify(preprocess(fp))
        case 'merge':
            imfp1   = opts[0]
            imfp2   = opts[1]
            output  = opts[2]
            attach  = opts[3] if len(opts) > 3 else 'h'
            merge(imfp1, imfp2, output, attach)
