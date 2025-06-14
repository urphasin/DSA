import * as fs from 'fs';
import * as readline from 'readline';

const inputFile = 'input.txt';

async function readInputFile() {
  const fileStream = fs.createReadStream(inputFile);

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  for await (const line of rl) {
    // Process each line here
    console.log(line);
  }
}

readInputFile().catch(err => {
  console.error(`Error reading file: ${err}`);
});