# Simple Social Media Directory

A very simple way to get the names and details of popular social media networks, even if they change their names.

The idea came as a way to provide developers to 'insert social media networks here' in your code. Let's say you're building a website and there's social media buttons in the footer. As the developer, you don't care what networks they are, you just need to show the links in the footer to keep your client happy. Well, here you go! And what's more you don't even have to pay attention to whatever the social networks are calling themselves. Let's say if Twitter becomes X, it doesn't matter - your code just runs a loop over the collection. If a social media network changes its name or logo we (that is, I) will update this app and the API so you start getting the latest name/logo. 

**For example**

Create a new React component:

```javascript
// src/SocialMediaFooter.js

import React, { useEffect, useState } from 'react';
import './SocialMediaFooter.css';

const SocialMediaFooter = () => {
    const [networks, setNetworks] = useState([]);

    useEffect(() => {
        fetch('https://mikes-simple-social-media-directory.replit.app/api/social-networks')
            .then(response => response.json())
            .then(data => setNetworks(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <footer className="social-media-footer">
            <h2>Connect with Us</h2>
            <ul>
                {networks.map(network => (
                    <li key={network.id}>
                        <a href={network.website} target="_blank" rel="noopener noreferrer">
                            <img src={network.logos.icon} alt={`${network.current_name} Icon`} />
                            {network.current_name}
                        </a>
                    </li>
                ))}
            </ul>
        </footer>
    );
};

export default SocialMediaFooter;
```

Add some styling:

```css
/* src/SocialMediaFooter.css */

.social-media-footer {
    background-color: #f8f9fa;
    padding: 20px;
    text-align: center;
}

.social-media-footer h2 {
    margin-bottom: 15px;
}

.social-media-footer ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 15px;
}

.social-media-footer li {
    display: flex;
    align-items: center;
}

.social-media-footer a {
    text-decoration: none;
    color: #333;
    display: flex;
    align-items: center;
    gap: 8px;
}

.social-media-footer img {
    width: 24px;
    height: 24px;
}
```

Import and use the `SocialMediaFooter` component in your main application file.

```javascript
// src/App.js

import React from 'react';
import './App.css';
import SocialMediaFooter from './SocialMediaFooter';

function App() {
    return (
        <div className="App">
            {/* Your main application content */}
            
            {/* Social Media Footer */}
            <SocialMediaFooter />
        </div>
    );
}

export default App;
```


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

The API will be running at: `https://mikes-simple-social-media-directory.replit.app/api/social-networks`

I will keep this running for as long as I can, if it's useful. If nobody uses it I'll turn it off. You're welcome to deploy the code and run (and pay for) your own API if the above URL stops working.

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

## Example Response JSON

```json 
[
    {
        "current_name": "Facebook",
        "id": 1,
        "logos": {
            "icon": "static/logos/1/icon.png",
            "official": "static/logos/1/official.png"
        },
        "popularity": 1,
        "previous_name": "Facebook",
        "website": "https://facebook.com"
    },
    {
        "current_name": "X",
        "id": 2,
        "logos": {
            "icon": "static/logos/2/icon.png",
            "official": "static/logos/2/official.png"
        },
        "popularity": 2,
        "previous_name": "Twitter",
        "website": "https://x.com"
    },
    {
        "current_name": "Instagram",
        "id": 3,
        "logos": {
            "icon": "static/logos/3/icon.png",
            "official": "static/logos/3/official.png"
        },
        "popularity": 3,
        "previous_name": "Instagram",
        "website": "https://instagram.com"
    }
]
```

## Project Structure
- `main.py`: The main Flask application that serves the API.
- `social_networks.json`: Contains the data for the social media networks.

## License
This project is licensed under the MIT License. See the `LICENSE.md` file for details.