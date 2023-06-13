// SPDX-License-Identifier: MIT
pragma solidity 0.8;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract NFTVault is IERC721Receiver {
    using Address for address;

    address private _owner;
    mapping (address => mapping (uint256 => bool)) private _deposits;

    event NFTDeposited(address indexed from, uint256 indexed tokenId);
    event NFTWithdrawn(address indexed to, uint256 indexed tokenId);

    constructor() {
        _owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "NFTVault: caller is not the owner");
        _;
    }

    function deposit(address tokenAddress, uint256 tokenId) external {
        require(IERC721(tokenAddress).ownerOf(tokenId) == msg.sender, "NFTVault: caller is not the owner of the NFT");
        require(!_deposits[tokenAddress][tokenId], "NFTVault: NFT already deposited");
        IERC721(tokenAddress).safeTransferFrom(msg.sender, address(this), tokenId);
        _deposits[tokenAddress][tokenId] = true;
        emit NFTDeposited(msg.sender, tokenId);
    }

    function withdraw(address tokenAddress, uint256 tokenId) external onlyOwner {
        require(_deposits[tokenAddress][tokenId], "NFTVault: NFT not deposited");
        IERC721(tokenAddress).safeTransferFrom(address(this), msg.sender, tokenId);
        _deposits[tokenAddress][tokenId] = false;
        emit NFTWithdrawn(msg.sender, tokenId);
    }

    function onERC721Received(address, address, uint256, bytes memory) public virtual override returns (bytes4) {
        return this.onERC721Received.selector;
    }
}
