# Line colors

```
this.colors = {
bus: 'red',
nachtbus: 'black',
eilbus: 'green',
XpressBus: 'green',
S1: 'green',
S11: 'green',
S2: 'darkred',
S21: 'darkred',
S3: 'violet',
S31: 'violet',
S32: 'blue',
S4: 'magenta',
U1: 'darkblue',
U2: 'red',
U3: 'yellow',
U4: 'turquoise',
akn: 'orange',
A1: 'orange',
A2: 'orange',
A3: 'orange',
A4: 'orange',
RE: 'transparent',
RB: 'transparent',
faehre: 'lightblue',
ferry: 'lightblue',
default:
'transparent'
},
this.realColors = {
darkblue: '#006AB3',
red: '#E2001A',
yellow: '#FFDD00',
turquoise: '#0098A1',
green: '#1A962B',
darkred: '#B51143',
violet: '#622181',
blue: '#0089BB',
magenta: '#be007c',
orange: '#F29400',
black: '#000000',
lightblue: '#009DD1',
grey: 'grey',
transparent: '#000000'
},
```

# BaseRequestType

```
language: String
version: int
UUID: String
filterType: FilterType
```


# BaseResponseType

```
UUID: String
```

# Response idea

```

class BaseResponse():
    def __init__(self, json):
        self.returnCode = json.get("returnCode")

class InitResponse(BaseResponse):
    def __init__(self, json):
        BaseResponse.__init__(json)
        self.beginOfService = json.get("beginOfService")
        self.endOfService = json.get("endOfService")
        self.id = json.get("id")
        self.dataId = json.get("dataId")
        self.buildDate = json.get("buildDate")
        self.buildTime = json.get("buildTime")
        self.buildText = json.get("buildText")

class CNResponse(BaseResponse):
    def __init__(self, json):
        BaseResponse.__init__(json)

```