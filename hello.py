from hikka import loader, utils  # Импорт API Hikka
import asyncio  # Для задержки перед удалением

@loader.tds
class HelloMod(loader.Module):
    """Простой модуль для Hikka, который отвечает 'Привет, бро!'"""

    strings = {"name": "HelloMod"}  # Название модуля

    @loader.command()
    async def hello(self, message):
        """Отвечает 'Привет, бро!' и самоуничтожается"""
        args = utils.get_args_raw(message)  # Получаем текст после команды
        text = f"Привет, {args}!" if args else "Привет, бро!"  

        reply = await utils.answer(message, text)  # Отправляем ответ
        await message.delete()  # Удаляем команду пользователя
        await asyncio.sleep(5)  # Ждём 5 секунд
        await reply.delete()  # Удаляем ответ
