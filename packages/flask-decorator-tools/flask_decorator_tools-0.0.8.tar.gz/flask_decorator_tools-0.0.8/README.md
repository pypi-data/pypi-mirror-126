# Flask Tools

This is a library that provides some simple tools for making an API with flask.

## Installation 
```
pip install flask-decorator-tools
```

## Usage

### Serialise and Deserialise
Decorators for flask routes are available for serialisation and deserialisation. To serialise return an object and a response code and the response will be serialised to JSON. If no response code is given a response code of 200 is assumed.
```
@app.route('/test', methods = ['POST'])
@serialise
@authenticate()
def post_form_entry():
    testOutputClass = TestOutputClass()
    return testOutputClass, 200
```
To deserialise a class must be passed to the decorator, the incoming JSON body will then be deserialised to an object that is passed to the route as a parameter. The same applys for deserialising the args for a request. 
```
@app.route('/test', methods = ['POST'])
@deserialise(TestInputClass)
@serialise
@authenticate()
def post_form_entry(testInputClass : TestInputClass):
    print(testInputClass)
    testOutputClass = TestOutputClass()
    return TestOutputClass, 200

@app.route('/test', methods = ['POST'])
@deserialise_args(FormEntryArgs)
@serialise
@authenticate()
def post_form_entry(args : TestInputClass):
    print(args)
    testOutputClass = TestOutputClass()
    return TestOutputClass, 200
```
The python classes that are deserialised to must accept a dictionary in their constructor. It is recommened that the pip package **json-schema-to-class** is used to generate the classes from json schemas.

### Configs
A tool is provided to pass configs from a JSON config file. The configs can be read from a json file like below.
```
{
    "tokens":{
        "token1":100,
        "token2":"2"
    }
    "database":{
        "keys":{
            "first_key":"first",
            "second_key":"second"
        },
        "codes":{
            "first_code":"first",
            "first_code":"second"
        }
    }
}
```
This json object can then have configs read as follows.
```
@parse("configs/config.json","tokens")
@dataclass
class TokensConfig:
  token1: int
  token2: str
tokensConfig = TokensConfig()

@parse("configs/config.json","database.keys")
@dataclass
class DataBaseKeyConfig:
  first_key: str
  second_key: str
dataBaseKeyConfig = DataBaseKeyConfig()

@parse("configs/config.json","database.codes")
@dataclass
class DataBaseKeyConfig:
  first_key: str
  second_key: str
dataBaseKeyConfig = DataBaseKeyConfig()
```
The parse decorator is used in conjunction with the **dataclass** decorator. The parse decorator takes two parameters, the first is the route to the config file to read from and the second is the route through the json config object to the object to fill the class from. It is expected that an instance of the class will be created once.