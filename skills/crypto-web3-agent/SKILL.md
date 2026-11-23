---
name: crypto-web3-agent
description: 'Design and build Web3 apps: ERC-20 sale, constant-product AMM and royalty NFT contracts on OpenZeppelin 5, plus ethers wallet integration and multi-chain switching. Use when prototyping smart contracts or a dApp front end.'
license: MIT
---

# Crypto & Web3 Agent

> **Note:** Some code here is an architecture sketch: classes may call helpers that aren't defined in this file. Treat those as outlines to implement, not drop-in code. Any `grok --agent ...` commands come from the source repo; check your CLI's docs before relying on them.

> **Security:** The contracts below are unaudited teaching examples. Test on a testnet, add tests and fuzzing, and get an audit before deploying anything that holds real funds.

## Overview
Grok, you'll act as a blockchain and cryptocurrency expert that designs and implements Web3 solutions. This agent specializes in smart contracts, DeFi protocols, NFT marketplaces, and decentralized applications.

## Agent Capabilities

### 1. Smart Contract Development
- Solidity contract development
- Security audit patterns
- Gas optimization
- Upgradeable contracts
- Testing and verification
- Contract interaction patterns

### 2. DeFi Protocol Design
- Automated market makers
- Lending and borrowing
- Yield farming
- Liquidity pools
- Tokenomics design
- Governance mechanisms

### 3. NFT Implementation
- ERC-721 and ERC-1155 contracts
- Metadata standards
- Marketplace development
- Royalty structures
- Lazy minting
- Cross-chain NFTs

### 4. Web3 Integration
- Wallet connection
- Transaction signing
- DApp frontend integration
- Web3 provider management
- Chain abstraction
- Multi-chain support

## Blockchain Framework

### 1. Smart Contract Template
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20; // OpenZeppelin 5 requires >=0.8.20

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

contract DeFiToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18;
    uint256 public constant PRESALE_SUPPLY = 100_000_000 * 10**18;
    
    uint256 public presalePrice = 0.0001 ether;
    uint256 public publicPrice = 0.0002 ether;
    
    bool public presaleActive = false;
    bool public publicSaleActive = false;
    
    mapping(address => uint256) public presalePurchased;
    uint256 public constant PRESALE_LIMIT = 1000 * 10**18;
    
    event PresaleStarted();
    event PublicSaleStarted();
    event TokensPurchased(address indexed buyer, uint256 amount);
    
    constructor() ERC20("DeFi Token", "DFT") Ownable(msg.sender) {
        _mint(address(this), MAX_SUPPLY);
    }
    
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleActive = true;
        emit PresaleStarted();
    }
    
    function endPresale() external onlyOwner {
        presaleActive = false;
    }
    
    function startPublicSale() external onlyOwner {
        require(!publicSaleActive, "Public sale already active");
        require(!presaleActive, "Presale still active");
        publicSaleActive = true;
        emit PublicSaleStarted();
    }
    
    function buyPresale(uint256 amount) external payable nonReentrant {
        require(presaleActive, "Presale not active");
        require(amount > 0, "Amount must be greater than 0");
        // amount is in base units (18 decimals); price is per whole token
        require(msg.value >= (amount * presalePrice) / 1e18, "Insufficient payment");
        require(presalePurchased[msg.sender] + amount <= PRESALE_LIMIT, "Exceeds presale limit");
        
        presalePurchased[msg.sender] += amount;
        _transfer(address(this), msg.sender, amount);
        
        emit TokensPurchased(msg.sender, amount);
    }
    
    function buyPublic(uint256 amount) external payable nonReentrant {
        require(publicSaleActive, "Public sale not active");
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value >= (amount * publicPrice) / 1e18, "Insufficient payment");
        require(balanceOf(address(this)) >= amount, "Insufficient tokens available");
        
        _transfer(address(this), msg.sender, amount);
        emit TokensPurchased(msg.sender, amount);
    }
    
    function withdrawFunds() external onlyOwner nonReentrant {
        (bool ok, ) = payable(owner()).call{value: address(this).balance}("");
        require(ok, "Withdraw failed");
    }
    
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsold = balanceOf(address(this));
        _transfer(address(this), owner(), unsold);
    }
}
```

### 2. DeFi AMM Contract
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20; // OpenZeppelin 5 requires >=0.8.20

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";

// LP shares are this contract's own ERC20. No swap fee, for clarity.
contract AMMPool is ERC20 {
    using SafeERC20 for IERC20;
    
    IERC20 public tokenA;
    IERC20 public tokenB;
    
    uint256 public reserveA;
    uint256 public reserveB;
    
    uint256 public constant MINIMUM_LIQUIDITY = 1000;
    
    event Mint(address indexed provider, uint256 amountA, uint256 amountB);
    event Burn(address indexed provider, uint256 amountA, uint256 amountB);
    event Swap(address indexed trader, uint256 amountIn, uint256 amountOut);
    
    constructor(address _tokenA, address _tokenB) ERC20("AMM LP", "ALP") {
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }
    
    function addLiquidity(uint256 amountA, uint256 amountB) external returns (uint256) {
        tokenA.safeTransferFrom(msg.sender, address(this), amountA);
        tokenB.safeTransferFrom(msg.sender, address(this), amountB);
        
        uint256 liquidity;
        if (reserveA == 0 && reserveB == 0) {
            liquidity = Math.sqrt(amountA * amountB) - MINIMUM_LIQUIDITY;
            _mint(address(0xdead), MINIMUM_LIQUIDITY); // lock minimum liquidity forever
        } else {
            liquidity = Math.min(
                (amountA * totalSupply()) / reserveA,
                (amountB * totalSupply()) / reserveB
            );
        }
        
        require(liquidity > 0, "Insufficient liquidity minted");
        
        reserveA = tokenA.balanceOf(address(this));
        reserveB = tokenB.balanceOf(address(this));
        
        _mint(msg.sender, liquidity);
        emit Mint(msg.sender, amountA, amountB);
        
        return liquidity;
    }
    
    function removeLiquidity(uint256 liquidity) external returns (uint256 amountA, uint256 amountB) {
        uint256 balanceA = tokenA.balanceOf(address(this));
        uint256 balanceB = tokenB.balanceOf(address(this));
        
        amountA = (liquidity * balanceA) / totalSupply();
        amountB = (liquidity * balanceB) / totalSupply();
        
        require(amountA > 0 && amountB > 0, "Insufficient liquidity burned");
        
        _burn(msg.sender, liquidity);
        tokenA.safeTransfer(msg.sender, amountA);
        tokenB.safeTransfer(msg.sender, amountB);
        
        reserveA = balanceA - amountA;
        reserveB = balanceB - amountB;
        
        emit Burn(msg.sender, amountA, amountB);
    }
    
    function swapAForB(uint256 amountIn, uint256 minAmountOut) external returns (uint256 amountOut) {
        require(amountIn > 0, "Amount must be greater than 0");
        
        uint256 balanceA = tokenA.balanceOf(address(this));
        uint256 balanceB = tokenB.balanceOf(address(this));
        
        amountOut = (amountIn * reserveB) / (reserveA + amountIn);
        require(amountOut > 0, "Insufficient output amount");
        require(amountOut < reserveB, "Insufficient reserve");
        require(amountOut >= minAmountOut, "Slippage"); // protects against sandwich attacks
        
        tokenA.safeTransferFrom(msg.sender, address(this), amountIn);
        tokenB.safeTransfer(msg.sender, amountOut);
        
        reserveA = balanceA + amountIn;
        reserveB = balanceB - amountOut;
        
        emit Swap(msg.sender, amountIn, amountOut);
        return amountOut;
    }
    
    function getAmountOut(uint256 amountIn, uint256 reserveIn, uint256 reserveOut) external pure returns (uint256) {
        require(amountIn > 0 && reserveIn > 0 && reserveOut > 0, "Invalid amounts");
        return (amountIn * reserveOut) / (reserveIn + amountIn);
    }
}
```

### 3. NFT Contract with Royalties
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20; // OpenZeppelin 5 requires >=0.8.20

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Royalty.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollection is ERC721, ERC721Royalty, Ownable {
    uint256 private _tokenIdCounter;
    string private _baseTokenURI;
    uint256 public maxSupply;
    uint256 public maxMintPerTx;
    uint256 public price;
    bool public mintingActive;
    
    struct NFTMetadata {
        string name;
        string description;
        string image;
    }
    
    mapping(uint256 => NFTMetadata) public metadata;
    
    event Minted(address indexed minter, uint256 indexed tokenId);
    event MintingStatusChanged(bool active);
    
    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        uint256 _maxSupply,
        uint256 _maxMintPerTx,
        uint256 _price
    ) ERC721(name, symbol) Ownable(msg.sender) {
        _baseTokenURI = baseURI;
        maxSupply = _maxSupply;
        maxMintPerTx = _maxMintPerTx;
        price = _price;
    }
    
    function mint(uint256 quantity) external payable {
        require(mintingActive, "Minting not active");
        require(quantity > 0 && quantity <= maxMintPerTx, "Invalid quantity");
        require(msg.value >= quantity * price, "Insufficient payment");
        require(_tokenIdCounter + quantity <= maxSupply, "Exceeds max supply");
        
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter;
            _safeMint(msg.sender, tokenId);
            emit Minted(msg.sender, tokenId);
            _tokenIdCounter++;
        }
    }
    
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
    
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
    
    function setDefaultRoyalty(address receiver, uint96 feeNumerator) external onlyOwner {
        _setDefaultRoyalty(receiver, feeNumerator);
    }
    
    function toggleMinting() external onlyOwner {
        mintingActive = !mintingActive;
        emit MintingStatusChanged(mintingActive);
    }
    
    function setPrice(uint256 newPrice) external onlyOwner {
        price = newPrice;
    }
    
    function supportsInterface(bytes4 interfaceId)
        public view override(ERC721, ERC721Royalty) returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
    
    function withdraw() external onlyOwner {
        (bool ok, ) = payable(owner()).call{value: address(this).balance}("");
        require(ok, "Withdraw failed");
    }
}
```

## Quick Start Examples

### 1. Web3 Frontend Integration
```javascript
// ethers v5 API. In ethers v6: new ethers.BrowserProvider(window.ethereum),
// await provider.getSigner(), ethers.formatEther(), and native BigInt math.
import { ethers } from 'ethers';

class Web3Service {
  constructor(provider, contractABI, contractAddress) {
    this.provider = provider;
    this.contract = new ethers.Contract(contractAddress, contractABI, provider);
  }
  
  async connectWallet() {
    if (typeof window.ethereum !== 'undefined') {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      await provider.send('eth_requestAccounts', []);
      const signer = provider.getSigner();
      this.contract = this.contract.connect(signer);
      return signer.getAddress();
    }
    throw new Error('No wallet detected');
  }
  
  async getTokenBalance(tokenAddress, walletAddress) {
    const tokenContract = new ethers.Contract(
      tokenAddress,
      ['function balanceOf(address) view returns (uint256)'],
      this.provider
    );
    const balance = await tokenContract.balanceOf(walletAddress);
    return ethers.utils.formatEther(balance);
  }
  
  async buyTokens(amount) {
    const price = await this.contract.publicPrice();
    const value = amount.mul(price);
    const tx = await this.contract.buyPublic(amount, { value });
    return tx.wait();
  }
  
  async addLiquidity(amountA, amountB) {
    const tokenA = await this.contract.tokenA();
    const tokenB = await this.contract.tokenB();
    
    const tokenAContract = new ethers.Contract(
      tokenA,
      ['function approve(address, uint256) returns (bool)'],
      this.provider.getSigner()
    );
    const tokenBContract = new ethers.Contract(
      tokenB,
      ['function approve(address, uint256) returns (bool)'],
      this.provider.getSigner()
    );
    
    await tokenAContract.approve(this.contract.address, amountA);
    await tokenBContract.approve(this.contract.address, amountB);
    
    const tx = await this.contract.addLiquidity(amountA, amountB);
    return tx.wait();
  }
}
```

### 2. Gas Optimization
```javascript
// Gas optimization strategies
const gasOptimizations = {
  // Batch multiple operations
  batchTransactions: async (operations) => {
    const tx = await contract.batch(operations);
    return tx.wait();
  },
  
  // Use optimal gas price
  getOptimalGasPrice: async () => {
    const gasPrice = await provider.getGasPrice();
    const fastGasPrice = gasPrice.mul(120).div(100); // 20% higher for faster inclusion
    return fastGasPrice;
  },
  
  // Use minimal data types
  optimizedTypes: {
    useUint8: 'for small numbers (0-255)',
    useUint16: 'for numbers (0-65535)',
    useUint256: 'only for large numbers',
    useBool: 'for true/false values',
    useBytes32: 'for fixed-size data'
  },
  
  // Storage vs Memory
  memoryUsage: {
    storage: 'expensive, persistent',
    memory: 'cheaper, temporary',
    calldata: 'cheapest, read-only input'
  }
};
```

### 3. Multi-Chain Support
```javascript
const chainConfig = {
  ethereum: {
    chainId: '0x1',
    rpcUrl: 'https://mainnet.infura.io/v3/YOUR_KEY',
    nativeCurrency: { name: 'Ether', symbol: 'ETH', decimals: 18 }
  },
  polygon: {
    chainId: '0x89',
    rpcUrl: 'https://polygon-rpc.com',
    nativeCurrency: { name: 'POL', symbol: 'POL', decimals: 18 } // MATIC was renamed POL in 2024
  },
  binance: {
    chainId: '0x38',
    rpcUrl: 'https://bsc-dataseed.binance.org',
    nativeCurrency: { name: 'BNB', symbol: 'BNB', decimals: 18 }
  }
};

async function switchChain(targetChain) {
  const config = chainConfig[targetChain];
  await window.ethereum.request({
    method: 'wallet_switchEthereumChain',
    params: [{ chainId: config.chainId }]
  });
}
```

## Best Practices

1. **Security First**: Always audit smart contracts and follow security best practices
2. **Gas Optimization**: Write gas-efficient code to reduce transaction costs
3. **Test Thoroughly**: Use testnets and test extensively before mainnet deployment
4. **Upgradeability**: Consider upgradeable patterns for long-lived contracts
5. **User Experience**: Provide clear feedback and error messages for users

## Integration with Other Skills

- **security**: For smart contract security audits
- **backend**: For backend API integration with Web3
- **devops**: For blockchain infrastructure management

Remember: In Web3, transactions are irreversible. Test extensively, audit thoroughly, and proceed with caution. Security is not optional.

---

_Imported from [Awesome Grok Skills](https://github.com/LifeJiggy/Awesome-Grok-Skills) and adapted for this catalog (format and code fixes). Copyright (c) 2024 Awesome Grok Skills. MIT License._
