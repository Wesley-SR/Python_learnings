from datetime import datetime

identificador = 0


def process_date(string_date: str):
    return datetime.strptime(string_date, '%d/%m/%Y')

def nova_task(task_name: str, data: str):
    """Insere uma nova task na lista de tasks

    Args:
        task_name (str): [description]
        data (str): [description]
    """
    global identificador
    identificador += 1

    task = {
        'id': identificador,
        'task_name': 'str',
        'date': process_date(data),
        'state': 'TODO'
    }

    return task