 project name, "Bridge-TokenFlow":
 ## Vision
Experience hassle-free token movement across EVM compatible chains.

## 📊 Presentation

For a detailed presentation about the Bridge-TokenFlow project, click the link below:

[Bridge-TokenFlow Presentation]()

## 🎥 Demo

Check out our demo video to see how Bridge-TokenFlow works:

[![Watch the video]()]()

[Watch the video]()


 ## Sequence Diagram

Here is the sequence diagram illustrating the token movement across EVM-compatible chains for the "Bridge-TokenFlow" project:

![Token Movement Sequence Diagram](https://github.com/samarabdelhameed/pics/blob/main/diagram.png)

[View fullscreen diagram](https://github.com/samarabdelhameed/pics/blob/main/diagram.png)
s
[Download png](https://github.com/samarabdelhameed/pics/blob/main/diagram.png)



## Description
**Easily Move Your Tokens Across Different Chains**  
Bridge-TokenFlow allows you to seamlessly transfer supported tokens across various EVM-compatible chains. Here's how we make it happen:

### 1. Circle Payments & Transfers API
Currently, this method exclusively supports USDC transactions. It enables the movement of tokens between Ethereum and Polygon PoS networks, and vice versa.

### 2. Circle CCTP
With Circle CCTP, you can transfer USDC, DAI, USDT, and WETH tokens across Ethereum, Arbitrum, and Avalanche networks.

### 3. Polygon LxLy
Using Polygon LxLy, you can bridge USDC, DAI, and USDT tokens between Ethereum and Polygon zkEVM networks, ensuring smooth movement in both directions.

### Problem and Solution

#### Problem
In the current blockchain ecosystem, moving tokens across different EVM-compatible chains is a complex and often cumbersome process. Users face several challenges, including:

1. **Fragmentation of Networks:**
   - Different tokens and assets are locked within specific blockchain networks, making it difficult to transfer them across chains.

2. **High Transaction Fees:**
   - The cost of transferring tokens across networks can be prohibitively high, especially during periods of network congestion.

3. **Lack of Unified Solutions:**
   - Existing solutions are often fragmented, requiring users to navigate multiple platforms and services to achieve cross-chain transfers.

4. **Complex User Experience:**
   - Users must often manage multiple wallets, interfaces, and transaction steps, creating a complicated and time-consuming process.

5. **Limited Token Support:**
   - Many cross-chain solutions only support a limited number of tokens, restricting users' ability to move various assets freely.

#### Solution
Bridge-TokenFlow addresses these problems by providing a unified, cost-effective, and user-friendly platform for seamless token transfers across multiple EVM-compatible chains. Here’s how we solve the key issues:

1. **Seamless Integration of Networks:**
   - Bridge-TokenFlow supports a wide range of EVM-compatible chains, allowing users to transfer tokens effortlessly between networks such as Ethereum, Arbitrum, Avalanche, and Polygon zkEVM.

2. **Affordable Transaction Fees:**
   - We offer a transparent and competitive fee structure, with Circle API transactions capped at $20 and LxLy and CCTP transactions capped at 3% of the stablecoin amount, also capped at $20.

3. **Unified Platform:**
   - Our platform consolidates multiple cross-chain transfer mechanisms into a single interface, making it easier for users to manage and execute transactions.

4. **User-Friendly Experience:**
   - Bridge-TokenFlow simplifies the user experience by integrating with popular wallets and providing a straightforward interface for initiating and managing cross-chain transfers.

5. **Comprehensive Token Support:**
   - Our solution supports a variety of popular tokens, including USDT, USDC, DAI, and WETH, across multiple networks, providing users with greater flexibility in managing their assets.

6. **Future Enhancements:**
   - We are committed to continuous improvement, with plans to introduce multi-routing for greater flexibility, expand token support to include more assets, and offer fiat on & off-ramp capabilities to facilitate easier conversion between digital and fiat currencies.

By addressing these critical issues, Bridge-TokenFlow enhances the efficiency, affordability, and usability of cross-chain token transfers, empowering users to move their assets freely and with confidence across the blockchain ecosystem.


```markdown
<h1 align="center">
    <br>
    <a href="https://tokenflow.vercel.app">
        <img src="./.github/tokenflow.png" alt="Bridge-TokenFlow logo" />
    </a>
    <br>
</h1>

<h3 align="center">Experience hassle-free token movement across EVM compatible chains</h3>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.11+-1f425f.svg?style=for-the-badge&logo=python" alt="Python version">
    <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white" alt="Typescript version">
    <img src="https://img.shields.io/badge/built%20with-OpenZeppelin-3677FF?style=for-the-badge" alt="Built with Openzepellin">
    <img src="https://img.shields.io/github/contributors/prettyirrelevant/tokenflow?style=for-the-badge" alt="contributors">
</p>

<p align="center">
    <a href="#-demo">Demo</a> •
    <a href="#-features">Features</a> •
    <a href="#-folder-structure">Folder Structure</a> •
    <a href="#-api-documentation">API Documentation</a> •
    <a href="#-contributing">Contributing</a> •
    <a href="#-team">Team</a>
</p>




## 🎯 Features
<sup>[(Back to top)](#------------------------)</sup>

### Easily Move Your Tokens Across Different Chains

Our project allows you to seamlessly transfer supported tokens across various EVM-compatible chains.
Here's how we make it happen:

#### 1. Circle Payments & Transfers API

Currently, this method exclusively supports USDC transactions.
It enables the movement of tokens between Ethereum and Polygon PoS networks, and vice versa.

#### 2. Circle CCTP

With Circle CCTP, you can transfer USDC, DAI, USDT, and WETH tokens across Ethereum, Arbitrum, and Avalanche networks.

#### 3. Polygon LxLy

Using Polygon LxLy, you can bridge USDC, DAI, and USDT tokens between Ethereum and Polygon zkEVM networks,
ensuring smooth movement in both directions.

#### Supported Chains and Tokens

Here's an overview of the chains we currently support and the tokens they work with:

- Ethereum: USDT, USDC, DAI, WETH
- Ethereum Goerli: USDC
- Arbitrum One: USDT, USDC, DAI, WETH
- Arbitrum Goerli: USDC
- Avalanche: USDT, USDC, DAI, WETH
- Avalanche Fuji: USDC
- Polygon PoS: USDT, USDC, DAI, WETH
- Polygon Mumbai: USDC
- Polygon zkEVM: USDC, USDT, DAI
- Polygon zkEVM Testnet: USDC

### Affordable Transaction Fees

We believe in cost-effective solutions. Our platform offers a reasonable fee structure:

- Circle API: A 4% fee (capped at $20) for all transactions
- LxLy and CCTP: A 3% fee for stablecoins (capped at $20)

### Upcoming Enhancements

We're committed to continuous improvement. Here's what's in the pipeline:

- **Multi-Routing:** Soon, you'll have the flexibility to move across chains without limitations.
- **Expanded Token Support:** We're working to add more tokens to facilitate seamless transfers across different chains.
- **Fiat On & Off-Ramp:** We plan to introduce a feature that will allow you to easily convert between digital assets and fiat currency.

Stay tuned for these exciting enhancements!

### Important Information

Please note that due to gas implications,
we did not deploy contracts to interact with Polygon zkEVM Bridge & Circle's CCTP contracts on Ethereum mainnet.
However, all contracts are available on testnet networks for all supported EVM chains.
Please be aware that on testnet only USDC can be bridged, as the liquidity of other tokens cannot be determined,
and discovering router addresses for DEXes on the testnet posed difficulties.


## 🔄 Token Transfer Routes
<sup>[(Back to top)](#------------------------)</sup>

Our project provides convenient routes for transferring tokens across various EVM-compatible chains.
These routes specify the paths for moving tokens between source and destination chains:

#### Ethereum <-> Arbitrum

- Mainnet: **Circle CCTP** (not available)
- Testnet: **Circle CCTP**

#### Ethereum <-> Avalanche

- Mainnet: **Circle CCTP** (not available)
- Testnet: **Circle CCTP**

#### Ethereum <-> Polygon PoS

- Mainnet: **Circle Payments & Transfers API** (not available)
- Testnet: **Circle Payments & Transfers API**

#### Ethereum <-> Polygon zkEVM

- Mainnet: **Polygon LxLy Bridge** (not available)
- Testnet: **Polygon LxLy Bridge**

#### Polygon PoS <-> Ethereum

- Mainnet: **Circle Payments & Transfers API** (not available)
- Testnet: **Circle Payments & Transfers API**

#### Avalanche <-> Arbitrum

- Mainnet: **Circle CCTP**
- Testnet: **Circle CCTP**


## 🌵 Folder Structure
<sup>[(Back to top)](#------------------------)</sup>

```sh
.
├── backend   (Django Application)
├── contracts (Smart contracts)
└── frontend  (React SPA)
```


## 📜 API Documentation
<sup>[(Back to top)](#------------------------)</sup>

For in-depth API documentation, please refer to the following link:
- [Swagger Doc](https://tokenflow-api-eb9bd3c3ed18.herokuapp.com/api/docs)


## 🤖 Smart Contracts
<sup>[(Back to top)](#------------------------)</sup>

### Circle CCTP Contracts (CrossChainBridge)

Our smart contracts integrate Circle's CCTP contracts,
enabling seamless bridging of USDC across Ethereum, Arbitrum, and Avalanche networks.

- Ethereum Mainnet (Coming soon)
- Arbitrum Mainnet [0x8e326D9F79a9D944C920fC7aE899Dd181ecB0491](https://arbiscan.io/address/0x8e326D9F79a9D944C920fC7aE899Dd181ecB0491)
- Avalanche Mainnet [0x8e326D9F79a9D944C920fC7aE899Dd181ecB0491](https://snowtrace.io/address/0x8e326d9f79a9d944c920fc7ae899dd181ecb0491)
- Ethereum Goerli [0x354116A3BEFD3C2B9E98BC35127daCf735471AD8](https://goerli.etherscan.io/address/0x354116A3BEFD3C2B9E98BC35127daCf735471AD8)
- Arbitrum Goerli [0x354116A3BEFD3C2B9E98BC35127daCf735471AD8](https://goerli.arbiscan.io/address/0x354116A3BEFD3C2B9E98BC35127daCf735471AD8)
- Avalanche Fuji [0x7c1ba3e858e45fd789c86ec687b90d0f932679d0](https://testnet.snowtrace.io/address/0x7c1ba3e858e45fd789c86ec687b90d0f932679d0)

To learn more about CCTP, visit this [link](https://developers.circle.com/stablecoin/docs/cctp-getting-started)


### Polygon LxLy (RollupBridge)

This facilitates the bridging of assets between Ethereum and Polygon zkEVM networks through the Polygon zkEVM Bridge.

- Ethereum Mainnet (Coming soon)
- Polygon zkEVM (Coming soon)
- Ethereum Goerli [0xA7e800f51dFb9Fd8C09067d7fC5757e06e57F27b](https://goerli.etherscan.io/address/0xA7e800f51dFb9Fd8C09067d7fC5757e06e57F27b)
- Polygon zkEVM Testnet [0xA7e800f51dFb9Fd8C09067d7fC5757e06e57F27b](https://testnet-zkevm.polygonscan.com/address/0xA7e800f51dFb9Fd8C09067d7fC5757e06e57F27b)


## 👍 Contributing
<sup>[(Back to top)](#------------------------)</sup>

We believe in the power of collaboration and welcome contributions from all members of the community irrespective of your domain knowledge and level of expertise,
your input is valuable.
Here are a few ways you can get involved:

- **Spread the Word**: Help

 us reach more enthusiasts by sharing the project with your network. The more creators and collectors we bring together, the stronger our community becomes.
- **Feature Requests**: If you have ideas for new features or improvements, share them with us! We're excited to hear how we can enhance the marketplace to better serve the community.
- **Code Contributions**: Developers can contribute by submitting pull requests. Whether it's fixing bugs, optimizing code, or adding new functionalities, your code contributions are invaluable.
- **Bug Reports and Feedback**: If you encounter any issues or have suggestions for improvement, please open an issue on GitHub.


## 👥 Team
<sup>[(Back to top)](#------------------------)</sup>

Meet the creative minds who brought this project to life:

| **Name**            | **Role**                       | **GitHub**                                    |
|---------------------|--------------------------------|-----------------------------------------------|
| samar abdelhameed     | Smart Contract Engineer (LxLy) | [GitHub]()        |
| samar abdelhameed      | Designer & Frontend Engineer   | [GitHub]()         |

```

