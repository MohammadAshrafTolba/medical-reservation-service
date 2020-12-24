"""
This file is responsible for routing requests to the appropriate handlers
"""

from app.init_app import app, api
from flask import render_template, request