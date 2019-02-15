# **StockScrutiny-Emulator**

A stock market simulator is a webapp where users buy and sell real life stocks using virtual money. Users have to pay the actual market price and all the other charges to buy the stocks.

## Requirements

TBD

The following technologies will be used:
- Python
- Django Framework

## Action Plan

### Backend

1. CLIENT

- [ ] Make the protocols for connection between MDU & CLIENT and CLIENT & BOOK.
- [ ] Send a TCP request to MDU with CLIENT IP address to start receiving data from MDU.
- [ ] Make the Backend functions of the CLIENT.
     - [ ] Reading the data from .json file which was received from MDU.
     - [ ] Encrypting the buy/sell order to sent it to BOOK server.
     - [ ] Sending the Encrypted data to BOOK and receiving the acknowledgment from BOOK server.
     - [ ] Storing the list of stocks available in cache.

2. BOOK  

- [ ] Make the protocols for connection between MDU & BOOK and BOOK & CLIENT.
- [ ] Make the Database schema for BOOK.
- [ ] Make the Backend functions of the BOOK.
     - [ ] Decrypting the data received from CLIENT.
     - [ ] Reading the data from .json file which was received from MDU.
     - [ ] Updating the database with the data received from CLIENT and MDU.
     - [ ] Sending the acknowledgment to the CLIENT.

3. MDU

- [ ] Make the protocols for connection between MDU and CLIENT.
- [ ] Establish TCP connection with client, get its IP address and terminate the session.
- [ ] Load the CSV file. (Should be a separate function because we may replace it with an API) 
- [ ] Multicast data every second to the CLIENT(s) according to the Stock Market timings.

### Frontend

TBD

<!---
1. There will be a dashboard. Users will only get access to this once they signup for login. This page will also be separated into several components.

- [ ] A component which will show the stock that the user currently holds. It will only be visible when the user click on the show stock button. This component will be situated in the the left side of the webpage.
- [ ] A component of searchbar. User can enter the name of the stock in this searchbar and information of that particular will be retrieved from the API. It will also include a "Add to the watchlist" button. This component will go in the upper middle portion of the page.
- [ ] A component of watchlist. This will show the real time data of stocks that the user currently does not own but wants to buy. The real time data include stock name, current market price, OHLC for that day and volume. We will also include a buy and sell button. The Sell button will be grayed out until the user own that stock. This component will go in the lower middle portion of the page.
- [ ] A box that shows the amount of money the user currently has will also be included. It will be situated the top right corner. A button to logout will also be included. It will be situated in the lower right corner.
- [ ] Assemble all the above component in a single webpage.

2. There will be a signup page where users have to input their details to get access to the website. The signup page will be divided into several components.

- [ ] Make a component of login (for registered user)
- [ ] Make a component of signup (for unregistered user)
- [ ] Make a component of component (button) to switch between login and signup
- [ ] Assemble all of them into a single webpage.
-->

## Running The Test

TBD

## Working (Internal):

TBD

## Contribution 

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

In general, we follow the "fork-and-pull" Git workflow.
1. Fork the repo on GitHub.
2. Clone the project to your own machine.
3. Work on your fork.
    1. Make your changes and additions.
    2. Change or add tests if needed.
    3. Run tests and make sure they pass.
    4. Add changes to README.md if needed.
4. Commit changes to your own branch.
5. Make sure you merge the latest from "upstream" and resolve conflicts if there is any.
6. Repeat step 3 above.
7. Push your work back up to your fork.
8. Submit a Pull request so that we can review your changes.


## Maintainers

- [supragya](https://github.com/supragya) - **Supragya Raj** (author)
- [DeboDevelop](https://github.com/DeboDevelop) - **Debajyoti Dutta**

## List of Contributors

TBD
