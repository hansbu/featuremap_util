import json
import sys


# Write featuremap
def write_featuremap(im, dim, patch_size, x_arr, y_arr, filename):
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
                "i": x_arr.astype(int).tolist(),
                "j": y_arr.astype(int).tolist()
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
