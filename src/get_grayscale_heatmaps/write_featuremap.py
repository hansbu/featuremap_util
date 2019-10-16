import json
import sys


# Write featuremap
def write_featuremap(im, dim, patch_size, filename):
    newlistX = []
    newlistY = []
    for x in range(0, im.shape[0]):
        for y in range(0, im.shape[1]):
            newlistX.append(x)
            newlistY.append(y)

    # newlistX = [x for x in range(im.shape[0])]
    # newlistY = [y for y in range(im.shape[1])]

    print('shape', im.shape)

    my_obj = {
        "metadata": {
            "img_width": dim[0],
            "img_height": dim[1],
            "png_w": im.shape[0],
            "png_h": im.shape[1],
            "patch_w": patch_size,
            "patch_h": patch_size
        },
        "data": {
            "locations": {
                "i": newlistX,
                "j": newlistY
            },
            "features": {
                'TIL': im[:, :, 0].tolist(),
                'Cancer': im[:, :, 1].tolist(),
                'Tissue': im[:, :, 2].tolist()
            }
        }
    }

    json_str = json.dumps(my_obj)
    try:
        ff = open(filename.replace('png', 'json'), "w")  # open file in write mode
        ff.write(json_str)  # write to file
        ff.close()
    except IOError as e:
        errno, strerror = e.args
        print("I/O error({0}): {1}".format(errno, strerror))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
