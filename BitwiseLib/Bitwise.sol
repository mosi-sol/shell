// SPDX-License-Identifier: MIT

pragma solidity 0.8;

library Bitwise {

    function and(uint256 a, uint256 b) internal pure returns (uint256) {
        return a & b;
    }

    function or(uint256 a, uint256 b) internal pure returns (uint256) {
        return a | b;
    }

    function xor(uint256 a, uint256 b) internal pure returns (uint256) {
        return a ^ b;
    }

    function not(uint256 a) internal pure returns (uint256) {
        return ~a;
    }

    function mask(uint256 a, uint256 mask) internal pure returns (uint256) {
        return a & mask;
    }
}
