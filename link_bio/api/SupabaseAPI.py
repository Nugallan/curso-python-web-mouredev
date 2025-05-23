import os
import dotenv
# pip install supabase
from supabase import create_client, Client
from link_bio.model.Featured import Featured

class SupabaseAPI:
    
    dotenv.load_dotenv()
    
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(
                self.SUPABASE_URL, self.SUPABASE_KEY
            )
    
    def featured(self) -> list[Featured]: # lista de featured
        
        response = self.supabase.table("featured").select("*").order("init_date", desc=True).limit(2).execute() # 'limit' limita la selección de consulta a 2 items y order de fecha descendente.
        
        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data[0]:
                featured_data.append(
                    Featured(
                        title=featured_item["title"], 
                        image=featured_item["image"], 
                        url=featured_item["url"]
                    )
                )
        
        return featured_data