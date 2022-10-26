import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
  
# Necessary Vars
API_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "803b9bf62395f64a16a299fce45f3482")
SESSION = os.getenv("SESSION", "BQAhIHQAWbgUu4CNAyADUcc7HndXJrSZHOGm7e7hbuwyfdaNuFJOHw_AZwm9JG0XYyMAqLX99mMUMTmO-OMeU5wGiu-9AyJTmBeXske562ell7gnkQwkOdHkNS27Esw7n4lnss_HtUlwXCFFVhwcAmVqP0QYzg9c5b40frW8yhASRhB4YB0M8MWpbqPLfuih7dzZAogK0TSAu0xhQ3eNqTWy6J-RboWM46Mk_J4nzSZW-4V1uIkkqsFWg7dXMYjTfFyX4hHOA12XCCwAM_331cQWK_FZ8B5ooL-1w9kS5mIMyX1ViVYIrhcsfKVBGdTZ8hSqlVn0jl7MrSaro9xyWopfq_5s9gAAAAEqTn8OAA")
HNDLR = os.getenv("HNDLR", ".")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
  lambda _, __, message:
  (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
  grp = True
else:
  grp = False
  
GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)
