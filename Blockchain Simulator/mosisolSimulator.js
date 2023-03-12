/* ===== Blockchain simulation                  ===== */
/* ===== Expermential code                      ===== */
/* ===== How to blockchain transactions work    ===== */
/* ===== Automate: run-and-log.bat              ===== */

//include secure hash algorithm
const SHA256 = require("crypto-js/sha256");

/* ====================
	assistant
==================== */
function timeHandler() {
	let t = Date.now();
	t = Math.round(t / 1000);
	return t;
}

function counterId(count) {
	return count + 1;
}

function randomness() {
	return Math.floor(Math.random() * 101);
}

/* ====================
	virtual!
==================== */
class Block{
  constructor(index, timestamp, data, previousHash){
    this.index = index;
    this.timestamp = timestamp;
    this.data = data;
    this.previousHash = previousHash;
    this.hash = this.generateHash();
  }

  generateHash(){
    return SHA256(this.index + this.timestamp + this.previousHash + JSON.stringify(this.data)).toString()
  }
}

/* ====================
	simulate
==================== */
class Blockchain{
    constructor(){
        this.blockchain = [this.createGenesisBlock()];
    }
    createGenesisBlock(){
        return new Block(0, timeHandler(), walletGen(), "0");
    }
    getTheLatestBlock(){
        return this.blockchain[this.blockchain.length - 1];
    }
    addNewBlock(newBlock){
        newBlock.previousHash = this.getTheLatestBlock().hash;
        newBlock.hash = newBlock.generateHash();
        this.blockchain.push(newBlock);
    }

    
    validateChainIntegrity(){
        for(let i = 1; i<this.blockchain.length; i++){
            const currentBlock = this.blockchain[i];
            const previousBlock = this.blockchain[i-1];
            if(currentBlock.hash !== currentBlock.generateHash()){
                return false;
            }
            if(currentBlock.previousHash !== previousBlock.hash){
                return false;
            }
            return true;

        }
    }
}


/* ====================
	wallet generator
==================== */
function walletGen() {
	var ethers = require('ethers');  
	var crypto = require('crypto');
	var id = crypto.randomBytes(32).toString('hex');
	var privateKey = "0x"+id;
	var wallet = new ethers.Wallet(privateKey);
	return wallet.address;
}


/* ====================
	mining
==================== */
async function run(j) {
	let mosiSolSimulator = new Blockchain();
	for(i = 0; i < j; i++){
		await mosiSolSimulator.addNewBlock(
			new Block(counterId(i), timeHandler(), {
				sender: walletGen(),
				recipient: walletGen(),
				quantity: randomness()
			})
		);
	}
	console.log(JSON.stringify(mosiSolSimulator, null, 5))
}
run(4); // simulating: genesis block + 4 next transaction block. 