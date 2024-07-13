document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    const formData = new FormData();
    const audioFile = document.getElementById('audio').files[0];
    formData.append('audio', audioFile);

    const response = await fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const statusDiv = document.getElementById('status');
    if (result.success) {
        statusDiv.textContent = 'File uploaded and noise reduced successfully';
        const downloadLink = document.createElement('a');
        downloadLink.href = `http://localhost:5000/download/${result.filename}`;
        downloadLink.textContent = 'Download Cleaned Audio File';
        downloadLink.download = result.filename;
        statusDiv.appendChild(downloadLink);
    } else {
        statusDiv.textContent = 'Upload failed';
    }
});
