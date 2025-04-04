
from typing import Any
import click
from os import system 
from pyperclip import copy as cp
from db_manager import DBManager


HOST : str = "bandit.labs.overthewire.org"
PORT : str = "2220"
manager = DBManager()

@click.group()
def cli(): pass

@cli.command()
@click.option("-l", "--level", prompt="Level", type=int)
@click.option("-f", "--flag", prompt="Flag")
def add_level(level, flag):
    manager.insert_level(level, flag) 

@cli.command()
def connect():
    last_bandit : Any = manager.get_last_level()
    level : str =  last_bandit["level"]
    flag : str = last_bandit["flag"]
    click.secho(f"connection to bandit level {level}", fg="green")
    cp(flag)
    click.secho("password copied", fg="blue")
    system(f"ssh bandit{level}@{HOST} -p {PORT}")
