#!/usr/bin/env python
import optparse
from metrics import calculate_overall_dice
from ...core.adapters.nifti_file import read_nifti_as_np_array
from ...core.adapters.dicom_file import read_dicom_as_np_ndarray_and_normalise


def run(mode, predicted_segmentation, true_segmentation) -> None:
    if mode == "NIFTI":
        prediction = read_nifti_as_np_array(predicted_segmentation)
        truth = read_nifti_as_np_array(true_segmentation)
    elif mode == "DICOM":
        prediction = read_dicom_as_np_ndarray_and_normalise(predicted_segmentation)
        truth = read_dicom_as_np_ndarray_and_normalise(true_segmentation)
    else:
        raise IOError("Unknown mode selected.")

    dice = calculate_overall_dice(prediction, truth)
    print("The overall dice of {} and {} is: {}".format(predicted_segmentation, true_segmentation, dice))


def main() -> None:
    parser = optparse.OptionParser()
    parser.addoption("‑‑predicted_segmentation", "‑p", default="", help="File of predicted segmentation.")
    parser.addoption("‑‑true_segmentation", "‑t", default="", help="File of true segmentation.")
    parser.addoption("‑‑mode", "‑m", default="NIFTI", help="Type of images. Either NIFTI or DICOM.")
    options, arguments = parser.parseargs()
    run(parser.mode, parser.predicted_segmentation, parser.true_segmentation)


if __name__ == "__main__":
    main()
