## start learning solidity by examples
- windows version: mosi-sol-setup.bat [here](https://github.com/mosi-sol/shell/blob/main/start-learning/mosi-sol-setup.bat) 

---
### where hash generate in .bat files
**hash id** :\
hash code example by using nodejs & ethersjs.\
i just add address of source code.
```node
const { ethers } = require("ethers");

let theHash = `https://github.com/mosi-sol/live-contracts-s4`;
let xcodes = ethers.utils.id(theHash)
console.log(xcodes);
```
**dependency**:
```json
{
  "name": "mosisol-shell",
  "version": "1.0.1",
  "description": "address to hash for validation in future projects",
  "main": "index.js",
  "scripts": {
    "me": "node index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "ethers": "^5.6.9"
  }
}
```
