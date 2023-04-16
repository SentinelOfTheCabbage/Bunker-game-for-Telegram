class Update:

    def __init__(self, message=None, callback=None) -> None:
        self._from_message(message)
        self._from_callback(callback)

    def _from_message(self, message) -> None:
        if not message:
            return
        self.user_id = message.from_user.id
        self.content = message.text
        self.update_id = message.message_id
        self.update_type = 'message'
        print(self.user_id,self.content,self.update_id,self.update_type)

    def _from_callback(self, callback) -> None:
        if not callback:
            return
        self.user_id = callback.from_user.id
        self.content = callback.data
        self.update_id = callback.id
        self.update_type = 'callback'
        print(self.user_id,self.content,self.update_id,self.update_type)
