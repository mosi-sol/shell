// SPDX-License-Identifier: MIT
pragma solidity 0.8;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenVault is Ownable {
    using SafeERC20 for IERC20;

    mapping (address => uint256) private _balances;

    event TokensDeposited(address indexed from, uint256 amount);
    event TokensWithdrawn(address indexed to, uint256 amount);

    // Allow anyone to deposit tokens into the vault
    receive() external payable {
        revert("TokenVault: does not support ETH deposits");
    }

    function deposit(address tokenAddress, uint256 amount) external {
        IERC20(tokenAddress).safeTransferFrom(msg.sender, address(this), amount);
        _balances[tokenAddress] += amount;
        emit TokensDeposited(msg.sender, amount);
    }

    function withdraw(address tokenAddress, uint256 amount) external onlyOwner {
        _balances[tokenAddress] -= amount;
        IERC20(tokenAddress).safeTransfer(msg.sender, amount);
        emit TokensWithdrawn(msg.sender, amount);
    }

    function balance(address tokenAddress) external view returns (uint256) {
        return _balances[tokenAddress];
    }
}
