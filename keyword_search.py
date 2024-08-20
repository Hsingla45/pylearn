messages = [
    {"sender": "99155 71177",
    "receiver": "99999 11111",
    "conversation":["Hello","How are you", "Its Friday here","Lets Party. No Code today"]
    },
    {"sender": "99155 71177",
    "receiver": "99999 22222",
    "conversation":["Hello","Kaisa hai bhai","Aj Friday hai","lets party here."]
    },
    {"sender": "98765 12345",
    "receiver": "99155 71177",
    "conversation":["Beta","Bahut Kaam Hai", "Sabji leni hai","jaldio aa jana. mummy here"]
    }
]  # type: ignore


   
keyword = input("Enter keyword to search: ") 
    
idx1 = 0
for idx in range(0, len(messages)):
    for element in list(messages[idx1]["conversation"]):
        if keyword in element:
            print("Sender:", messages[idx1]["sender"], " | " "Receiver", messages[idx1]["receiver"],"\n"
                  "Message:", element)
            message_convert = list(element)
            input_conversion = list(keyword)
            for i in message_convert:
                if i == input_conversion[0]:
                    print("Index number:", message_convert.index(i))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    idx1 += 1


"""
for elment in list(messages[0]["conversation"]):
    if keyword in elment:
       print("yes there:",elment)
       id = list(elment)
       conv = list(keyword)
       for i in id:
            if i == keyword[0]:
                print(id.index(i))
"""       
