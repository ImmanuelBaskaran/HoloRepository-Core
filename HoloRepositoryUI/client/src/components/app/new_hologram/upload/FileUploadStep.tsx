import React, { Component } from "react";
import FileUploadInput from "./inputs/FileUploadInput";

class FileUploadStep extends Component {
  render() {
    return (
      <div>
        <FileUploadInput name="hologramFile" maxFileSizeInMb={50} required />
      </div>
    );
  }
}

export default FileUploadStep;
