const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function createWindow () {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile('index.html');
}

app.on('ready', () => {
  createWindow();

  // Start the Flask server
  const pythonProcess = spawn('python', ['./backend/app.py']);
  pythonProcess.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });
  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
