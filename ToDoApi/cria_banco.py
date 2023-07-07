import sqlite3

connection = sqlite3.connect('database/db.sqlite3')
cursor = connection.cursor()

""" cria_tabela = "CREATE TABLE IF NOT EXISTS tarefas(tarefa_id char(36) default (lower(hex(randomblob(4))) || '-' || lower(hex(randomblob(2))) || '-4' || substr(lower(hex(randomblob(2))),2) || '-' || substr('89ab',abs(random()) % 4 + 1, 1) || substr(lower(hex(randomblob(2))),2) || '-' || lower(hex(randomblob(6)))) PRIMARY KEY,\
                                          descricao TEXT,\
                                          concluido BOOL,\
                                          criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,\
                                          atualizado_em DATETIME DEFAULT CURRENT_TIMESTAMP)"
 """


cria_tarefa ="INSERT INTO tarefas(descricao,concluido) VALUES('Arrumar guarda-roupa',false)"

#ursor.execute(cria_tabela)
cursor.execute(cria_tarefa)
connection.commit()
connection.close()