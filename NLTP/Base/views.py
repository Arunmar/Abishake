from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputText
from .helpers import *
import flask
from flask import Flask, request, render_template
from flask_cors import CORS
from newspaper import Article

app = Flask(__name__)
CORS(app)
app = flask.Flask(__name__,template_folder='templates')
with open(r'C:\Users\shree\abishek\NLTP\Base\pickle_data\model.pkl','rb') as handle:
    model = pickle.load(handle)

# Create your views here.
def welcome(request):
    return render(request,"IntroText.html")

def InputFormatter(request):
    return render(request,"InputFormater.html")
def process(request):
    if request.method == 'POST':
        form=InputText(request.POST)
        if form.is_valid():
            Text=form.cleaned_data['Text']
            pred=model.predict([Text])
            context={"data":pred[0]}
            return render(request,"InputFormater.html",context=context)
    else:
        form=InputText()
    return render(request,'InputFormater.html',{'form':form})