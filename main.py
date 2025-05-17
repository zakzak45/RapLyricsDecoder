from transformers import pipeline


import matplotlib.pyplot as plt
from wordcloud import WordCloud

from better_profanity import profanity
from unidecode import unidecode
import re
import string

import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

import pronouncing
from flask import Flask, request, render_template  # uncomment if using Flask

import os
import json



