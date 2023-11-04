import sqlite3

import click
from flask import current_app, g
from supabase import create_client, Client



def get_db():
    if 'db' not in g:
        url: str = 'https://bfgckhvkvehgsitmiafk.supabase.co'
        key: str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmZ2NraHZrdmVoZ3NpdG1pYWZrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg4MjY5OTgsImV4cCI6MjAxNDQwMjk5OH0.JFaiMlq3E5wDw4k_XWOk_4eyH2NzBPfFwxTArul0Pqc'
        g.db = create_client(url, key)
        # g.db.row_factory = sqlite3.Row


    return g.db


def close_db(e=None):
    db:Client = g.pop('db', None)

    if db is not None:
        pass

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)