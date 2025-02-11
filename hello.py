from hikka import loader, utils  
import asyncio  

@loader.tds
class HelloMod(loader.Module):
    """Простой модуль для Hikka, который отвечает 'Привет, бро!'"""

    strings = {"name": "HelloMod"} 

    @loader.command()
    async def hello(self, message):
        """Отвечает 'Привет, бро!' и самоуничтожается"""
        args = utils.get_args_raw(message)  
        text = f"Привет, {args}!" if args else "Привет, бро!"  

        reply = await utils.answer(message, text)  
        await message.delete()  
        await asyncio.sleep(5)  
        await reply.delete()  
