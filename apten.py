from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flaskext.openid import OpenID 
