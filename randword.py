from .. import loader, utils
from random import choice
import ssl
import urllib.request

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

__version__ = (1,0,0)
@loader.tds
class RandWordMod(loader.Module):
  strings = {
    "name": "RandWord",
  }
  @loader.command()
  async def randword(self, message):
    await utils.answer(message, '<code>Загрузка...</code>')
    url = "https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt"
    response = urllib.request.urlopen(url, context=context)
    words_list = [line.decode('windows-1251').strip() for line in response.readlines()]
    await utils.answer(message, f'Рандомное слово: <code>{choice(words_list)}</code>')