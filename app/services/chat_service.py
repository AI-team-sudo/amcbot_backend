from typing import Tuple, List, Optional
from app.core.config import settings
from app.services.openai_service import OpenAIService
from app.services.pinecone_service import PineconeService

class ChatService:
    def __init__(self):
        self.openai_service = OpenAIService()
        self.pinecone_service = PineconeService()

    async def process_query(
        self,
        query: str,
        namespace: Optional[str] = None
    ) -> Tuple[str, bool, List[str]]:
        try:
            # Get embeddings
            embedding = await self.openai_service.get_embedding(query)

            # Query Pinecone
            matches = await self.pinecone_service.query(
                embedding,
                namespace if namespace else None
            )

            if not matches:
                return "માફ કરશો, કોई સંબંધિત માહિતી મળી નથી.", False, []

            # Process matches
            context, references = self._process_matches(matches)

            # Generate response
            response = await self.openai_service.generate_response(
                context,
                query,
                references
            )

            return response, True, references

        except Exception as e:
            return f"Error: {str(e)}", False, []

    def _process_matches(self, matches):
        # Implementation of match processing
        # Similar to the original process_pinecone_results function
        pass
