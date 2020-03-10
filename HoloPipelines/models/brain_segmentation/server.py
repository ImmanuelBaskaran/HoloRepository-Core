import os
import subprocess
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

from model import brain_model

# The directory paths are given by the original model in the container
UPLOAD_FOLDER = "./data"
OUTPUT_FOLDER = "./prediction"

ALLOWED_EXTENSION = "nii.gz"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


def file_format_is_allowed(filename):
    return "." in filename and filename.split(".", 1)[1].lower() == ALLOWED_EXTENSION

def filename_without_extension(filename):
    return filename.rsplit(".")[0]

import sys

@app.route("/model", methods=["POST"])
def seg_file():
    files = request.files.getlist("files[]")
    if len(files) != 3:
        return "Wrong number of files uploaded", 400
    for file in files:
        if file and file_format_is_allowed(file.filename):
            # save files in folder called upload
            filename = secure_filename(file.filename)
            # TODO check each file is uploaded once exactly
            if filename in ["FLAIR.nii.gz", "IR.nii.gz", "T1.nii.gz"]:
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                print("-"*50, file=sys.stderr)
                print("saving file", file=sys.stderr)
            else:
                return "Unknown filename uploaded", 400
        else:
            return "file does not have required extension", 400

    # predict using model
    # TODO where to store model in global app state?
    brain_model.predict(app.config["UPLOAD_FOLDER"], app.config["OUTPUT_FOLDER"])
    # segmentation can now be found in output folder titled segmentation.nii.gz
    return send_file(os.path.join(app.config["OUTPUT_FOLDER"], "segmentation.nii.gz")), 200


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1")