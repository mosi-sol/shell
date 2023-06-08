### use the our web3provider lib to build a nft mint dapp
```js
import { web3Provider } from './web3Provider.js';
import { sendTransaction } from './sendTransaction.js';
import { callContractFunction } from './callContractFunction.js';

const contractAddress = '0x...'; // Replace with the address of your NFT contract
const contractAbi = [...]; // Replace with the ABI of your NFT contract

async function mintNFT(tokenURI, privateKey) {
  try {
    // Get the contract instance
    const contractInstance = new web3Provider.provider.eth.Contract(contractAbi, contractAddress);

    // Get the current nonce for the account
    const from = await web3Provider.provider.eth.getCoinbase();
    const nonce = await web3Provider.provider.eth.getTransactionCount(from);

    // Build the transaction object
    const functionSignature = contractInstance.methods.mint(tokenURI).encodeABI();
    const gasPrice = await web3Provider.provider.eth.getGasPrice();
    const gasLimit = await contractInstance.methods.mint(tokenURI).estimateGas({ from });
    const transactionObject = {
      from,
      to: contractAddress,
      nonce,
      gasPrice,
      gasLimit,
      data: functionSignature,
    };

    // Sign and send the transaction
    const transactionHash = await sendTransaction({ ...transactionObject, privateKey });

    // Get the token ID of the newly minted token
    const tokenId = await callContractFunction(contractAddress, 'tokenIdCounter');

    // Return the token ID and transaction hash
    return { tokenId, transactionHash };
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to mint NFT: ${error.message}`);
  }
}

async function init() {
  try {
    // Mint an NFT
    const tokenURI = 'https://example.com/nft';
    const privateKey = '0x...'; // Replace with your private key
    const { tokenId, transactionHash } = await mintNFT(tokenURI, privateKey);
    console.log(`Minted NFT with token ID ${tokenId} and transaction hash ${transactionHash}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```
