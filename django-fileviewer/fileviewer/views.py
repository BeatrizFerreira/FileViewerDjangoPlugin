from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime


class FileViwer():
    def pdf_viewer(file_path):
        pdf = open(file_path, 'rb') 
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename='+(file_path)
        return response
        pdf.closed