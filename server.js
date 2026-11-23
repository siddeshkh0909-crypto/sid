const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 3000;
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml'
};

const server = http.createServer((req, res) => {
  let reqPath = req.url.split('?')[0];
  if (reqPath === '/' || reqPath === '') reqPath = '/index.html';
  if (reqPath === '/kit.html') reqPath = '/frontend/public/kit.html';

  let filePath = path.join(__dirname, reqPath);
  if (!fs.existsSync(filePath)) {
    // Try in frontend/public
    const altPath = path.join(__dirname, 'frontend', 'public', reqPath);
    if (fs.existsSync(altPath)) filePath = altPath;
  }

  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME_TYPES[ext] || 'text/plain',
      'Access-Control-Allow-Origin': '*'
    });
    fs.createReadStream(filePath).pipe(res);
  } else {
    // Default to index.html for SPA
    const fallback = path.join(__dirname, 'index.html');
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    fs.createReadStream(fallback).pipe(res);
  }
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`KIT SMART server running at http://localhost:${PORT}/`);
  console.log(`Also serving kit.html at http://localhost:${PORT}/kit.html`);
});
