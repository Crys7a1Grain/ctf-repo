const path = require('path');

let solution = "//flag";

if (solution.includes("../") || solution === "/flag") {
  throw new Error(
      "You CANNOT ACCESS the flag!!! You are UNAUTHORIZED!!! 🤖🤖🤖🤖🤖"
  );
}

let solutionPath = path.join('/', solution);

console.log(solutionPath);