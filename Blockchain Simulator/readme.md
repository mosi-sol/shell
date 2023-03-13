# Blockchain simulator
Nodejs blockchain simulator

run:
- run `npm i`
- node version > 18.7
- first way:`npm run me` or `node mosisolSimulator` (don't have log file)
- alternative way: using `run-and-log.bat` to run project mock & save json as "log"
- look at `block-scan.html` is/as block explorer (mock data)

Enjoy!

---

## explain by another example:

Simulating a blockchain in **Node.js** can be done by creating a class for the blocks and another class for the blockchain itself. Here's an example implementation:

```node
const SHA256 = require('crypto-js/sha256');

// Block class
class Block {
  constructor(index, timestamp, data, previousHash = '') {
    this.index = index;
    this.timestamp = timestamp;
    this.data = data;
    this.previousHash = previousHash;
    this.hash = this.calculateHash();
    this.nonce = 0;
  }

  calculateHash() {
    return SHA256(this.index + this.previousHash + this.timestamp + JSON.stringify(this.data) + this.nonce).toString();
  }

  mineBlock(difficulty) {
    while (this.hash.substring(0, difficulty) !== Array(difficulty + 1).join('0')) {
      this.nonce++;
      this.hash = this.calculateHash();
    }

    console.log(`Block mined: ${this.hash}`);
  }
}

// Blockchain class
class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
    this.difficulty = 3;
  }

  createGenesisBlock() {
    return new Block(0, new Date().toString(), 'Genesis block', '0');
  }

  getLatestBlock() {
    return this.chain[this.chain.length - 1];
  }

  addBlock(newBlock) {
    newBlock.previousHash = this.getLatestBlock().hash;
    newBlock.mineBlock(this.difficulty);
    this.chain.push(newBlock);
  }

  isChainValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];

      if (currentBlock.hash !== currentBlock.calculateHash()) {
        return false;
      }

      if (currentBlock.previousHash !== previousBlock.hash) {
        return false;
      }
    }

    return true;
  }
}

// Usage
let myCoin = new Blockchain();
myCoin.addBlock(new Block(1, new Date().toString(), {amount: 4}));
myCoin.addBlock(new Block(2, new Date().toString(), {amount: 10}));

console.log(JSON.stringify(myCoin, null, 4));
console.log(`Is blockchain valid? ${myCoin.isChainValid()}`);

myCoin.chain[1].data = {amount: 100};
myCoin.chain[1].hash = myCoin.chain[1].calculateHash();

console.log(JSON.stringify(myCoin, null, 4));
console.log(`Is blockchain valid? ${myCoin.isChainValid()}`);
```

#### dependency of this example: `npm i crypto-js` (ver ^4.1.1)


This code simulates a blockchain containing two blocks. The `Block` class represents a single block, while the `Blockchain` class represents the chain of blocks. 


The `Block` class has properties such as the block's index, timestamp, data, previous hash, current hash, and nonce (a random number added to the block to make it unique). 


The `Blockchain` class has methods to create the genesis block, get the latest block, add a new block to the chain, and verify the validity of the chain. 


The code creates a new blockchain and adds two blocks to it. It then prints the blockchain and checks if it's valid. Finally, it modifies the data in the first block and recalculates its hash, which makes the blockchain invalid. The code prints the blockchain again and checks if it's valid again, which should return **false**. 


Note that this is a simplified implementation for demonstration purposes and does not include features such as transaction validation, mining rewards, or peer-to-peer networking.


output:
```js
Block mined: 000b3efee99abdcd25c255bfde634d07a27af187a174dbfdfc0bd3d340b5ec88
Block mined: 00085ffcb46f4aea8195dfe2c5e361312bea746d535d6db1ac4fb154bfe54746
{
    "chain": [
        {
            "index": 0,
            "timestamp": "Mon Mar 13 2023 03:18:39 GMT+0330 (وقت عادی ایران)",
            "data": "Genesis block",
            "previousHash": "0",
            "hash": "a0c9c889c1d540a7e426f1c889c51750c7bc369320413f1a81c9aa2aa63b89f3",
            "nonce": 0
        },
        {
            "index": 1,
            "timestamp": "Mon Mar 13 2023 03:18:39 GMT+0330 (وقت عادی ایران)",
            "data": {
                "amount": 4
            },
            "previousHash": "a0c9c889c1d540a7e426f1c889c51750c7bc369320413f1a81c9aa2aa63b89f3",
            "hash": "000b3efee99abdcd25c255bfde634d07a27af187a174dbfdfc0bd3d340b5ec88",
            "nonce": 1391
        },
        {
            "index": 2,
            "timestamp": "Mon Mar 13 2023 03:18:39 GMT+0330 (وقت عادی ایران)",
            "data": {
                "amount": 10
            },
            "previousHash": "000b3efee99abdcd25c255bfde634d07a27af187a174dbfdfc0bd3d340b5ec88",
            "hash": "00085ffcb46f4aea8195dfe2c5e361312bea746d535d6db1ac4fb154bfe54746",
            "nonce": 437
        }
    ],
    "difficulty": 3
}
Is blockchain valid? true
{
    "chain": [
        {
            "index": 0,
            "timestamp": "Mon Mar 13 2023 03:18:39 GMT+0330 (وقت عادی ایران)",
            "data": "Genesis block",
            "previousHash": "0",
            "hash": "a0c9c889c1d540a7e426f1c889c51750c7bc369320413f1a81c9aa2aa63b89f3",
            "nonce": 0
        },
        {
            "index": 1,
            "timestamp": "Mon Mar 13 2023 03:18:39 GMT+0330 (وقت عادی ایران)",
            "data": {
                "amount": 100
            },
            "previousHash": "a0c9c889c1d540a7e426f1c889c51750c7bc369320413f1a81c9aa2aa63b89f3",
            "hash": "7980ecf6c8014a448f671e9705ad27d7305a740716d4186225afd4d72f30bfd9",
            "nonce": 1391
        },
        {
            "index": 2,
            "timestamp": "Mon Mar 13 2023 03:18:39 GMT+0330 (وقت عادی ایران)",
            "data": {
                "amount": 10
            },
            "previousHash": "000b3efee99abdcd25c255bfde634d07a27af187a174dbfdfc0bd3d340b5ec88",
            "hash": "00085ffcb46f4aea8195dfe2c5e361312bea746d535d6db1ac4fb154bfe54746",
            "nonce": 437
        }
    ],
    "difficulty": 3
}
Is blockchain valid? false

```
