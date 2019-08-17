# this pipeline may be removed in the future as obj is not used to display 3D model on hololens
import pipelines.services.format_conversion
from pipelines.components import compNifti2numpy
from pipelines.services.format_conversion import convert_numpy_to_obj
import pathlib
import sys
import logging

logging.basicConfig(level=logging.INFO)


def main(inputNiftiPath, outputObjPath, threshold, flipNpy=False):
    generatedNumpyList = compNifti2numpy.main(str(pathlib.Path(inputNiftiPath)))
    generatedObjPath = convert_numpy_to_obj(
        generatedNumpyList, threshold, str(pathlib.Path(outputObjPath))
    )
    logging.info("nifti2obj: done, obj saved to {}".format(generatedObjPath))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
