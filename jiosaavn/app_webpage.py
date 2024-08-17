from aiohttp.web import Application, AppRunner, TCPSite, RouteTableDef, Request, json_response

from jiosaavn.config.settings import HOST, PORT

routes = RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request: Request):
    """ Handles the root route ("/") of the web application. """
    return json_response("ʙᴏᴛ ʀᴜɴɴɪɴɢ...")

async def start_web():
    """ Initializes and starts the web server. """

    web_app = Application()
    web_app.add_routes(routes)
    runner = AppRunner(web_app)
    await runner.setup()
    await TCPSite(runner, HOST, PORT).start()
    print("ᴡᴇʙ sᴇʀᴠᴇʀ sᴛᴀʀᴛᴇᴅ!!")
    return runner

async def stop_web(runner: AppRunner):
    """Stops the web server and performs cleanup."""

    print("sᴛᴏᴘᴘɪɴɢ ᴡᴇʙ sᴇʀᴠᴇʀ!!")
    await runner.cleanup()
