'''                                
___________________ ______ ________
_  _ \_  __ \_  __ `/  __ `/_  ___/
/  __/  / / /  /_/ // /_/ /_  /    
\___//_/ /_/_\__, / \__,_/ /_/     
            /____/                 

        (c) 2022 - fuck you
'''
from engar.bot import Engar
import asyncio

async def main():
    async with Engar() as bot:
        try:
            await bot.run_async()
        except (KeyboardInterrupt, RuntimeError):
            exit(0)

if __name__ == '__main__':
    asyncio.run(main())

# funfact, this is actually "main" file of engar.
