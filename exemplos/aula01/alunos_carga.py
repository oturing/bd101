#!/usr/bin/env python3

import sqlite3
from contextlib import closing

ARQ_DADOS = 'alunos.txt'
DATABASE = 'escola.sqlite'

def conectar():
    return sqlite3.connect(DATABASE)

def recriar_tabela():
    sql = '''
        drop table if exists alunos;
        create table alunos (
            id integer primary key asc,
            nome text not null,
            genero text,
            media real
        );
    '''
    with closing(conectar()) as cnx:
        cnx.cursor().executescript(sql)
        cnx.commit()

def carregar_alunos():
    sql = '''INSERT INTO alunos (id, media, genero, nome) VALUES (?,?,?,?)'''
    with closing(conectar()) as cnx:
        with open(ARQ_DADOS, encoding='utf-8') as arq:
            dados = (lin.split('\t') for lin in arq)
            cnx.cursor().executemany(sql, dados)
        cnx.commit()

recriar_tabela()
carregar_alunos()

