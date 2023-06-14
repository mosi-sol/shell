// SPDX-License-Identifier: MIT

pragma solidity 0.8;

contract Bitwise {

    function and(uint256 a, uint256 b) public pure returns (uint256) {
        uint256 result;
        assembly {
            result := and(a, b)
        }
        return result;
    }

    function or(uint256 a, uint256 b) public pure returns (uint256) {
        uint256 result;
        assembly {
            result := or(a, b)
        }
        return result;
    }

    function xor(uint256 a, uint256 b) public pure returns (uint256) {
        uint256 result;
        assembly {
            result := xor(a, b)
        }
        return result;
    }

    function not(uint256 a) public pure returns (uint256) {
        uint256 result;
        assembly {
            result := not(a)
        }
        return result;
    }

    function mask(uint256 a, uint256 mask) public pure returns (uint256) {
        uint256 result;
        assembly {
            result := and(a, mask)
        }
        return result;
    }
}
