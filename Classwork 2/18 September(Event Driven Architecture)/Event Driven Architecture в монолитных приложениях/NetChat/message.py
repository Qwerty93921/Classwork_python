import json

class Message():
    time = 0
    text = ''
    type = 'public'
    senderName = ''  
    senderIP = ''
    receiverName = ''
    receiverIP = ''
    
    @staticmethod
    def fromText(text):
        msg = Message('{"text": "%s"}' % text)
        return msg

    @staticmethod
    def copy(msg):
        jsonstring = msg.toJson()
        new_message = Message(jsonstring)
        return new_message
    
    @classmethod
    def default_type(cls):
        return cls.type


    def __init__(self, jsonstring): # '{"time": "03-10-2023", ....}'
        data = json.loads(jsonstring)
        self.time = data.get('time', 0)
        if "senderIP" in data:
            self.senderIP = data['senderIP']
        if "senderName" in data:
            self.senderName = data['senderName']
        if "text" in data:
            self.text = data['text']
        if "receiverIP" in data:
            self.receiverIP = data['receiverIP']
        if "receiverName" in data:
            self.receiverName = data['receiverName']
        if "type" in data:
            self.type = data['type']
    
    def toJson(self):
        data = {}
        data['time'] = self.time
        data['text'] = self.text
        data['type'] = self.type
        data['senderIP'] = self.senderIP
        data['senderName'] = self.senderName
        data['receiverIP'] = self.receiverIP
        data['receiverName'] = self.receiverName
        return json.dumps(data)
    
    @property
    def json(self):
        string1 = self.toJson()
        return self.toJson()


if '__main__' == __name__:
    # msg = Message('{"text":"sender_name","time":50}')
    # print(msg.toJson())

    msg2 = Message.fromText("Hello Bekarys")
    print(msg2.json)

    msg3 = Message.copy(msg2)
    print(msg3.json)
