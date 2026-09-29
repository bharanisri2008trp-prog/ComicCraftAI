from google import genai
from google.genai import types

from .config import get_settings
from .models import OutlineResponse, PromptRequest


def get_client():

    settings = get_settings()

        if not settings.gemini_api_key:
                raise RuntimeError(
                            "GEMINI_API_KEY is missing. "
                                        "Please add it to your .env file."
                                                )

                                                    return genai.Client(
                                                            api_key=settings.gemini_api_key
                                                                )


                                                                def generate_outline(request: PromptRequest):

                                                                    settings = get_settings()

                                                                        prompt = f"""
                                                                        Create a five-panel comic outline.

                                                                        Story idea:
                                                                        {request.story_prompt}

                                                                        Main character:
                                                                        {request.character_name}

                                                                        Setting:
                                                                        {request.setting}

                                                                        Tone:
                                                                        {request.tone}

                                                                        Art style:
                                                                        {request.art_style}

                                                                        Requirements:

                                                                        1. Create exactly 5 panels.
                                                                        2. Number panels from 1 to 5.
                                                                        3. Keep the same main character throughout.
                                                                        4. Give every panel a short title.
                                                                        5. Give every panel a clear scene description.
                                                                        6. Give every panel a detailed image-generation prompt.
                                                                        7. The panels must form one connected story.
                                                                        8. The story should have a beginning, middle and ending.
                                                                        9. Do not put dialogue inside image prompts.
                                                                        """

                                                                            client = get_client()

                                                                                response = client.models.generate_content(

                                                                                        model=settings.gemini_flash_model,

                                                                                                contents=prompt,

                                                                                                        config=types.GenerateContentConfig(

                                                                                                                    temperature=0.8,

                                                                                                                                response_mime_type="application/json",

                                                                                                                                            response_schema=OutlineResponse
                                                                                                                                                    )
                                                                                                                                                        )

                                                                                                                                                            parsed = response.parsed

                                                                                                                                                                if parsed is None:

                                                                                                                                                                        parsed = OutlineResponse.model_validate_json(
                                                                                                                                                                                    response.text
                                                                                                                                                                                            )

                                                                                                                                                                                                return [
                                                                                                                                                                                                        panel.model_dump()
                                                                                                                                                                                                                for panel in parsed.panels
                                                                                                                                                                                                                    ]