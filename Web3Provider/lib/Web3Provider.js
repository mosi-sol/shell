class Web3Provider {
  constructor(provider) {
    this.provider = provider;
    this.requestId = 1;
  }

  async sendAsync(payload) {
    const id = this.requestId++;
    const message = {
      id,
      jsonrpc: '2.0',
      ...payload,
    };

    return new Promise((resolve, reject) => {
      this.provider.sendAsync(message, (err, response) => {
        if (err) {
          reject(err);
        } else {
          resolve(response.result);
        }
      });
    });
  }

  async send(method, params) {
    const payload = {
      method,
      params,
    };

    return this.sendAsync(payload);
  }

  async requestAccounts() {
    return this.send('eth_requestAccounts', []);
  }

  async getChainId() {
    return this.send('eth_chainId', []);
  }

  async getBlockNumber() {
    return this.send('eth_blockNumber', []);
  }

  async getBalance(address, blockNumber = 'latest') {
    return this.send('eth_getBalance', [address, blockNumber]);
  }

  async getTransactionCount(address, blockNumber = 'latest') {
    return this.send('eth_getTransactionCount', [address, blockNumber]);
  }

  async sendTransaction(tx) {
    return this.send('eth_sendTransaction', [tx]);
  }

  async getTransactionReceipt(txHash) {
    return this.send('eth_getTransactionReceipt', [txHash]);
  }

  async call(tx) {
    return this.send('eth_call', [tx]);
  }
}

const web3Provider = new Web3Provider(window.ethereum);
