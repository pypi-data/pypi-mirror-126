# python-dace-client #

This API provides code to call DACE backend with simple methods.
To install it do the following :

- ```pip install python-dace-client```

You can now use dace api

## Login to API ##
To log into the API, create a file .dacerc in your home directory with the following content :

```
[user]
key = apiKey:_Your api key_
```

To create an API Key, go on https://dace.unige.ch --> _profile_ --> _Generate a new API key_

Then copy the key and fill it into .dacerc file

If no file is found, you requests will be public