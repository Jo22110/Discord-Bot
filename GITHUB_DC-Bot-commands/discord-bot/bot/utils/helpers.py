def format_message(content: str, user: str) -> str:
    return f"{user}: {content}"

def handle_error(error: Exception) -> str:
    return f"An error occurred: {str(error)}"

def is_valid_channel(channel) -> bool:
    return channel is not None and channel.permissions_for(channel.guild.me).send_messages

def extract_args(message: str) -> list:
    return message.split()[1:] if message else []