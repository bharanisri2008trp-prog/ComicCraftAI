from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import get_settings
from .routes import router


get_settings()


app = FastAPI(
    title="ComicCraft AI",
        version="1.0.0",
            description="AI Comic Story Creator"
            )


            app.mount(
                "/static",
                    StaticFiles(directory="static"),
                        name="static"
                        )


                        app.include_router(router)
                                


                           

                                  

                     
                                            
                                       
                                              
                                                        


                                          