# Simple Social Media Directory

A very simple way to get the names and details of popular social media networks, even if they change their names.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Details](#api-details)
  - [Get Social Networks](#get-social-networks)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

You can clone this repo and pull down any changes over time to get the latest updates to names and logos, or you can call the API. Whilst the API is free this will only be possible for as long as I can afford it. 

### Access the API

The API will be running at: 

## API Details

### Get Social Networks
- Endpoint: `/api/social-networks`
- Method: `GET`
- Description: Retrieves a list of popular social media networks with their details.
- Request: No parameters required
- Response
  - Content-Type: `application/json`
  - Status Code: `200 OK`


### Example Usage with curl

```
curl http://localhost:5000/api/social-networks
```

## Project Structure
- `main.py`: The main Flask application that serves the API.
- `social_networks.json`: Contains the data for the social media networks.

## License
This project is licensed under the MIT License. See the `LICENSE.md` file for details.