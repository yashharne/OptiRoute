import sqlite3
import os
import click
from flask import current_app, g
from supabase import create_client, Client



def get_db():
    if 'db' not in g:
        url = os.environ.get('DATABASE_URL')
        key = os.environ.get('API_KEY')
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