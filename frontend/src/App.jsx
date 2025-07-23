import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [videoURL, setVideoURL] = useState("");
  const [fastForward, setFastForward] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a video.");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("fast_forward", fastForward);

    setProcessing(true);
    const response = await axios.post("https://smart-video-processor.onrender.com/process/", formData, {
      responseType: "blob",
    });

    const blob = new Blob([response.data], { type: "video/mp4" });
    setVideoURL(URL.createObjectURL(blob));
    setProcessing(false);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Smart Video Processor</h1>
      <input type="file" accept="video/*" onChange={(e) => setFile(e.target.files[0])} />
      <div className="my-2">
        <label>
          <input
            type="checkbox"
            checked={fastForward}
            onChange={(e) => setFastForward(e.target.checked)}
          />
          <span className="ml-2">Fast Forward Entire Video</span>
        </label>
      </div>
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded"
        disabled={processing}
      >
        {processing ? "Processing..." : "Upload & Process"}
      </button>

      {videoURL && (
        <div className="mt-6">
          <h2 className="text-lg font-semibold">Processed Video:</h2>
          <video src={videoURL} controls className="w-full mt-2" />
          <a href={videoURL} download="processed_video.mp4" className="text-blue-700 underline">
            Download
          </a>
        </div>
      )}
    </div>
  );
}

export default App;
