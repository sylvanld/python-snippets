from snippet.config import Config

# create a config instance with environment implementation
conf = Config.create("environment")

# user config to get value of key: username
value = conf.get("username")

# show result retrieved from env var
print(value)
