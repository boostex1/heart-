from hikka import loader, utils  

@loader.tds
class HelloMod(loader.Module):
    """Простой модуль для Hikka, который отвечает 'Привет, бро!'"""

    strings = {"name": "HelloModBoost"}  

    @loader.command()
    async def hello(self, message):
        """Отвечает 'Привет, бро!'"""
        args = utils.get_args_raw(message)  
        text = f"Привет, {args}!" if args else "Привет, бро!"  
        
        await utils.answer(message, text)  
