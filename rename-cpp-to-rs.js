const fs = require('fs');
const path = require('path');

function renameCppToRs(dir) {
  fs.readdirSync(dir).forEach(file => {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);

    if (stat.isDirectory()) {
      renameCppToRs(fullPath); // 🔁 dive into subdirectories
    } else if (path.extname(fullPath) === '.rs') {
      const newPath = fullPath.replace(/\.rs$/, '.ts');
      fs.renameSync(fullPath, newPath);
      console.log(`Renamed: ${fullPath} → ${newPath}`);
    }
  });
}

// Use the provided directory or default to current
const startDir = process.argv[2] || '.';
renameCppToRs(path.resolve(startDir));
