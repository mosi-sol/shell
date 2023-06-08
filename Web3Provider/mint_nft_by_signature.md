```js
import { web3Provider } from './web3Provider.js';
import { sendTransaction } from './sendTransaction.js';
import { callContractFunction } from './callContractFunction.js';

const contractAddress = '0x...';  // Replace with the address of your NFT contract
const contractAbi = [...];        // Replace with the ABI of your NFT contract
const privateKey = '0x...';       // Replace with your private key

async function approvePrice(price) {
  try {
    // Get the current nonce for the account
    const from = await web3Provider.provider.eth.getCoinbase();
    const nonce = await web3Provider.provider.eth.getTransactionCount(from);

    // Build the message to sign
    const message = `I approve the price of ${price} ETH for the NFT`;

    // Sign the message
    const signature = await web3Provider.provider.eth.personal.sign(message, from, '');

    // Return the signature and transaction nonce
    return { signature, nonce };
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to approve price: ${error.message}`);
  }
}

async function mintNFT(tokenURI, tokenId, signature, nonce) {
  try {
    // Get the contract instance
    const contractInstance = new web3Provider.provider.eth.Contract(contractAbi, contractAddress);

    // Verify the signature
    const from = await web3Provider.provider.eth.getCoinbase();
    const recoveredAddress = await web3Provider.provider.eth.personal.ecRecover(`I approve the price of ${tokenId} ETH for the NFT`, signature);
    if (from.toLowerCase() !== recoveredAddress.toLowerCase()) {
      throw new Error('Invalid signature');
    }

    // Build the transaction object
    const functionSignature = contractInstance.methods.mint(tokenURI, tokenId).encodeABI();
    const gasPrice = await web3Provider.provider.eth.getGasPrice();
    const gasLimit = await contractInstance.methods.mint(tokenURI, tokenId).estimateGas({ from });
    const transactionObject = {
      from,
      to: contractAddress,
      nonce,
      gasPrice,
      gasLimit,
      data: functionSignature,
    };

    // Send the transaction
    const transactionHash = await sendTransaction({ ...transactionObject, privateKey });

    // Return the transaction hash
    return transactionHash;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to mint NFT: ${error.message}`);
  }
}

async function init() {
  try {
    // Approve the price
    const price = 1;      // 1 ETH
    const { signature, nonce } = await approvePrice(price);

    // Mint the NFT
    const tokenURI = 'https://example.com/nft';
    const tokenId = 1;
    const transactionHash = await mintNFT(tokenURI, tokenId, signature, nonce);

    console.log(`Minted NFT with token ID ${tokenId} and transaction hash ${transactionHash}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```
