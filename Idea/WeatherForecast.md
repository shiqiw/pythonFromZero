# Features and functionalities

- Send information via SMS.
- Use secret store to store credential information, such as phone number. Right now, just read from JSON formatted text file.
- Get weather forecast for certain area. In future, bind forecast location with cell phone's current location. 
- The information includes: weather, temperature (high and low, feels like), chance of rain, UV index, and other special warning. Data store in MongoDB(?).
- In future, try run service on Azure. [Python App on Azure](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-web-get-started-python)
- Daily message in the morning (when sunrise) about today's weather, high and low temperature, umbrella recommendation, sunscreen recommendation. Send message when: feels like temperature differs by 10 degree, chance of rain increase by 30% (and suggest when it drops), UV index reach 5 and drop below 5.