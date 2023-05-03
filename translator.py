from telethon.tl.types import Message
from .. import loader, utils
import requests
version = (1, 0, 0)
@loader.tds
class TranslatorMod(loader.Module):
  strings = {
    "name": "Translator",
    "error": "🚫 Error: {}",
    "process": "🌘<code>Translating...</code>",
    "translated": "✅Message translated: <code>{}</code>"
  }
  strings_ru = {
    "error": "🚫 Ошибка: {}",
    "process": "🌘<code>Переводим...</code>",
    "translated": "✅Сообщение переведено: <code>{}</code>"
  }
  @loader.command(
    ru_doc="<язык для перевода> <текст> - Перевести текст с помощью Microsoft API",
    eu_doc="<language to translate> <text> - Translate text using Microsoft API",
  )
  async def translate(self, message: Message):
    args = utils.get_args_raw(message)
    args = args.split(maxsplit=2)
    if not args or len(args) < 2:
      await utils.answer(
        message,
        self.strings("error").format(
          "Usage: .translate &lt;language to translate&gt; &lt;text&gt;"
          "Example: .translate en Привет мир!"
        ),
      )
      return
    message = await utils.answer(message, self.strings("process"))
    target_lang, text = args[0], args[1:]
    text = ' '.join(text)
    accepted_lang=["af", "sq", "ar", "hy", "az", "bs", "bg", "zh-CN", "zh-TW", "hr", "cs", "da", "nl", "en", "et", "tl", "fi", "fr", "ka", "de", "el", "hi", "id", "it", "ja", "kk", "ko",   "lv", "ky", "mn", "no", "pl", "pt", "ro", "ru", "sr", "sl", "es", "sv", "tr", "uk", "vi", "uz"]
    if target_lang in accepted_lang:
      url = "https://microsoft-translator-text.p.rapidapi.com/translate"
      querystring = {"api-version":"3.0","to[0]":{target_lang},"textType":"plain","profanityAction":"NoAction"}
      payload = [{ "Text": text }]
      headers = {
      	"content-type": "application/json",
      	"X-RapidAPI-Key": "ab3ee107f1msh1bc49c1ad671524p113a86jsn0a4d4f35b046",
      	"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
      }
      response = requests.post(url, json=payload, headers=headers, params=querystring)
      await utils.answer(
        message,
        self.strings("translated").format(
          response.json()[0]["translations"][0]["text"]
        ),
      )
    else:
      await utils.answer(
        message,
        self.strings("error").format(
          "Not supported language."
        ),
      )
      return