// SPDX-License-Identifier: MIT
pragma solidity 0.8;

import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/token/ERC1155/IERC1155Receiver.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract NFTVault is IERC1155Receiver {
    using Address for address;

    address private _owner;
    mapping (address => mapping (uint256 => uint256)) private _deposits;

    event NFTDeposited(address indexed from, uint256 indexed tokenId, uint256 quantity);
    event NFTWithdrawn(address indexed to, uint256 indexed tokenId, uint256 quantity);

    constructor() {
        _owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "NFTVault: caller is not the owner");
        _;
    }

    function deposit(address tokenAddress, uint256 tokenId, uint256 quantity) external {
        require(IERC1155(tokenAddress).balanceOf(msg.sender, tokenId) >= quantity, "NFTVault: caller does not own enough of the NFT");
        _deposits[tokenAddress][tokenId] += quantity;
        IERC1155(tokenAddress).safeTransferFrom(msg.sender, address(this), tokenId, quantity, "");
        emit NFTDeposited(msg.sender, tokenId, quantity);
    }

    function withdraw(address tokenAddress, uint256 tokenId, uint256 quantity) external onlyOwner {
        require(_deposits[tokenAddress][tokenId] >= quantity, "NFTVault: NFT quantity not deposited");
        _deposits[tokenAddress][tokenId] -= quantity;
        IERC1155(tokenAddress).safeTransferFrom(address(this), msg.sender, tokenId, quantity, "");
        emit NFTWithdrawn(msg.sender, tokenId, quantity);
    }

    function onERC1155Received(address, address, uint256, uint256, bytes memory) public virtual override returns (bytes4) {
        return this.onERC1155Received.selector;
    }

    function depositedBalance(address tokenAddress, uint256 tokenId) public view returns (uint256) {
        return _deposits[tokenAddress][tokenId];
    }
}
