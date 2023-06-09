class TarefaModel:
   def __init__(self,tarefa_id,descricao,concluido,criado_em,atualizado_em):
       self.tarefa_id = tarefa_id
       self.descricao = descricao
       self.concluido = concluido
       self.criado_em = criado_em
       self.atualizado_em = atualizado_em
    
   def json(self):
       return{
           'tarefa_id' : self.tarefa_id,  
           'descricao' : self.descricao,
           'concluido' : self.concluido,
           'criado_em' : self.criado_em, 
           'atualizado_em' : self.atualizado_em 
       }