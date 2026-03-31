import base64
import time
import random
from urllib.parse import urlencode

from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from apps.ai_prompt_generations.data.data_prompt import get_data_prompts
from apps.ai_prompt_generations.services.ai_prompt_generation_service import AiPromptGenerationService
from apps.devs.services.ai_generation_service import AIGenerationService

from apps.devs.services.pdf_service import PdfService
from apps.devs.services.mail_service import MailService
from core.http.api_request import ApiRequest
from core.messages.message_channel import MessageChannel





class DevApiViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service_prompt = AiPromptGenerationService()
        self.service_generation = AIGenerationService()


    @action(detail=False, methods=['get'], url_path='test_pdf')
    def invoke_pdf(self, request):
        """
            Generación de PDF de prueba.
        """
        try:
            
            ## - Generar PDF y descargarlo
            
            # pdf_service = CreatePdfService()
            # pdf_bytes = pdf_service.generate_pdf({
            #     "title": "PDF de prueba",
            #     "body": "Hola, este es un PDF generado desde Django con wkhtmltopdf.",
            # })
            # response = HttpResponse(pdf_bytes, content_type="application/pdf")
            # response["Content-Disposition"] = 'attachment; filename="prueba.pdf"'
            # return response
        
        
            ## - Guardar PDF en carpeta uploads/pdfs
            
            pdf_service = PdfService(
                template_html="pdfs/test_pdf.html"
            )

            file_path = pdf_service.save(
                filename="prueba.pdf",
                context={
                    "title": "PDF guardado",
                    "body": "Hola, este PDF se ha guardado en la carpeta uploads/pdfs.",
                }
            )
            
            response = {
                "message": "PDF generado y guardado correctamente",
                "file_path": file_path,
            }
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



    
    @action(detail=False, methods=['get'], url_path='test_email')
    def invoke_email(self, request):
        ''' Envio de correo de prueba.'''
        try:
            
            mail_service = MailService(
                subject="Correo Prueba",
                to_emails=["doriandarren1@gmail.com"],
            )
            
            mail_service.send_html_mail(
                title="Correo de prueba",
                body="Hola,\n\nEste es un correo de prueba.\n\nGracias por tu tiempo."
            )
            
            
            response = {
                "message": "OK"
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    




    @action(detail=False, methods=['get'], url_path='test____')
    def invoke_sss(self, request):
        try:

            for payload in get_data_prompts():

                # Buscar por system_message y user_message
                ai_text_generation_prompt = self.service_prompt.list().filter(
                    system_message=payload.get("system_message", ""),
                    user_message=payload.get("user_message", ""),
                ).first()

                if ai_text_generation_prompt:
                    continue

                ai_text_generation_prompt = self.service_prompt.set_ai_prompt_generation(
                    payload.get("system_role", ""),
                    payload.get("system_message", ""),
                    payload.get("user_role", ""),
                    payload.get("user_message", ""),
                    False,
                    False,
                    False,
                )

                self.service_prompt.store(ai_text_generation_prompt)

            response = {
                "message": "OK"
            }
            return Response({
                'message': response,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




    @action(detail=False, methods=['get'], url_path='test__')
    def invoke__(self, request):  
        try:
            
            # prompt = self.service_prompt.findByIsProcessed()
            
            # 1.-
            prompts = self.service_prompt.list()
            prompt = prompts[random.randint(0, len(prompts)-1)]
            
            if not prompt:
                return Response(
                    {
                        "message": "No prompt found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            ai_text_generation = self.service_generation.get_comfyui_text(prompt)
            
            
            MessageChannel.send(
                text=f"invoke ejecutado: {time.time()}",
                title="CRON",
            )
            
            
            
            
            # 2.-
            prompt_id = self.get_comfyui_image(prompt)
            if not prompt_id:
                return Response(
                    {"error": "No se pudo obtener el prompt_id"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
         
                   
            # 3.-
            # response_history = {}
            # outputs = {}
            # image_base64 = ""
            
            # for _ in range(30):
            #     response_history = api_confyui.get(f"/history/{prompt_id}")
                
            #     if response_history and response_history.get(prompt_id):
            #         data = response_history.get(prompt_id, {})
            #         outputs = data.get("outputs", {})
            #         if outputs:
            #             image_base64 = self.get_comfyui_image_base64(outputs)
            #             break
                
            #     time.sleep(1)
            
            
            response = {
                "message": "OK",
                ##"text_generation": aiTextGenerationSerializer(ai_text_generation).data,
                "ai_text_generation": ai_text_generation.id,
                # "prompt_id": prompt_id,
                # "outputs": outputs,
                # "image_base64": image_base64
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
