class dateFormat():
    def getMessages(messages):
        for message in messages:
            message["created_at"] = message["created_at"].strftime("%Y/%m/%d %H:%M")
            message["updated_at"] = message["updated_at"].strftime("%Y/%m/%d %H:%M")
        return messages
