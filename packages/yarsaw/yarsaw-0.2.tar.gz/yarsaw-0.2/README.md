# Yet Another Random Stuff API Wrapper - YARSAW

YARSAW is an Async Python API Wrapper for the [Random Stuff API](https://api-info.pgamerx.com). This module makes it simpler for you to interact with the API and is easy to implement into your application.

**Make sure to get an API Key from [here](https://api-info.pgamerx.com/register.html) before trying to access this module.**

This is an example of how a simple async request to the API would look like with and without using the module - just to get a simple joke (basic lines filtered out, eg. async function, imports, etc.

#### Without YARSAW

```Python
async with aiohttp.ClientSession() as session:
    async with session.get('https://api.pgamerx.com/v5/joke', params={'type' : 'any'}, headers={'Authorization':'API KEY'}) as response: # need to pass these things again and again
        if response['type'] == 'twopart': # format the joke manually
            print(response['setup'], '\n', response['delivery'])
        else:
            print(response['joke'])
```

#### With YARSAW

```Python
client = yarsaw.Client('hPED3sb7Wkge') # need to pass the API Key ONCE and for all!
joke = await client.joke(joke_type='any') # simpler customization
print(await yarsaw.Utils().format_joke(joke)) # format the joke automatically!
```

And it's reusable! No need to pass your API key again and again. The module saves you multiple lines of code just in this simple example to get a joke - imagine how many more lines and characters it could save you in the long run - not having to pass your API key again and again, simpler usage, safe and fast, and with much more! **Automate the boring stuff.**

Docs and examples coming soon.