from typing import Iterable
from django.db import models

import requests


class AnalysisResult(models.Model):
    patient = models.ForeignKey("user.User", verbose_name = "Пациент", on_delete=models.CASCADE, related_name="patient_results")
    diagnosis = models.CharField("Диагноз", max_length=128, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    doctor = models.ForeignKey("user.User", on_delete=models.DO_NOTHING, related_name="doctor_results", null=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Результат анализа"
        verbose_name_plural = "Результаты анализов"

    def __str__(self) -> str:
        return f"{self.patient}"
    
    def save(self, *args, **kwargs):

        # получение картинок с объекта результата анализа
        # images_queryset = self.images.all()
        # images = []

        # url = "АПИ эндпоинт нейронки для обработки картинки"

        # for image in images_queryset:
            # images.append(image.image)
        
        
        # data = None # картинка (либо в байтах), либо же где-то хранить или иметь доступ к нейронке прямо из джанго приложения


        # запрос к нейронке
        # response = requests.post(url=url, data=data).json()
        

        # примерный ответ от нейронки
        # response = { 
        #     "diagnosis": "название диагноза",
        #     "description": "описание диагноза"
        # }

        # Изменение диагноза и описания должно работать только, когда от нейронки приходит нужный ответ
        # if response.get("diagnosis"):
        #     self.diagnosis = response["diagnosis"]
        #     self.description = response["description"]


        return super().save(*args, **kwargs)

class AnalysisResultImage(models.Model):
    result = models.ForeignKey("AnalysisResult", models.CASCADE, related_name="images")
    image = models.ImageField("Снимок", upload_to="patients/results", null=True, blank=True)
