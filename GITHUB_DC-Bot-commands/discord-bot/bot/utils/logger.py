class Logger:
    def __init__(self, stream):
        self.stream = stream
        self.bot_client = None
        self.log_channel_id = None

    def set_bot_client(self, bot_client, log_channel_id):
        self.bot_client = bot_client
        self.log_channel_id = log_channel_id

    def write(self, message):
        if message.strip():
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_message = f"{timestamp} || {message.strip()}"
            self.stream.write(formatted_message + "\n")

            if self.bot_client and self.log_channel_id:
                try:
                    asyncio.create_task(self.send_to_discord(formatted_message))
                except Exception as e:
                    self.stream.write(f"Error sending to log channel: {e}\n")

    def flush(self):
        self.stream.flush()

    async def send_to_discord(self, message):
        log_channel = self.bot_client.get_channel(self.log_channel_id)
        if log_channel:
            try:
                await log_channel.send(message)
            except Exception as e:
                self.stream.write(f"Error sending to log channel: {e}\n")
        else:
            self.stream.write(f"⚠️ Log channel with ID {self.log_channel_id} not found.\n")