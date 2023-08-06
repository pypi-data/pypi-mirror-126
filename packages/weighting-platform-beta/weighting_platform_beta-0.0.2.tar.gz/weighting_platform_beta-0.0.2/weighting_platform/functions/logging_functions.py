"""
Модуль содержит фунционал для логирования
Ключевую роль в логировании играет переменная current_round_info из модуля
cfg. Этот модуль импортируется во все остальные модули, и модули этих функций
меняют эту переменную. Дальше состояние этой переменной отправляется по
подписчикам демоном QPI
"""

import datetime
from weighting_platform import cfg


def init_gross_log(qdw):
    """ Создать новый лог, у которого пока не будет отмечено поле record """
    record_id = cfg.current_round['record_id']
    message = format_message('Начало взвешивания брутто')
    command = "INSERT INTO log_records (gross_log, record) " \
              "VALUES ('{}', {})".format(message, record_id)
    response = qdw.try_execute(command)['info'][0][0]
    return response


def init_tare_log(qdw):
    """ Поставить отметку, что начали взвешивать тару """
    record_id = cfg.current_round['record_id']
    message = format_message('Начало взвешивания тары')
    command = "INSERT INTO log_records (tare_log, record) values (%s, %s) " \
              "ON CONFLICT (record) DO UPDATE SET tare_log=%s"
    values = (message, record_id, message)
    response = qdw.try_execute_double(command, values)
    return response


def fix_record_id(qdw, log_id):
    """ Закрепить за логом заезд """
    record_id = cfg.current_round['record_id']
    command = "UPDATE log_records SET record={} WHERE id={}"
    command = command.format(record_id, log_id)
    response = qdw.try_execute(command)
    fix_log_end(qdw)
    return response


def fix_event(qdw, message):
    """ Закрепить событие в логах """
    has_gross = cfg.current_round['has_gross']
    if has_gross:
        fix_tare_event(qdw, message)
    else:
        fix_gross_event(qdw, message)


def fix_gross_event(qdw, message):
    record_id = cfg.current_round['record_id']
    message = format_message(message)
    command = "UPDATE log_records SET gross_log = gross_log || '{}' " \
              "WHERE record = {}".format(message, record_id)
    response = qdw.try_execute(command)
    return response


def fix_tare_event(qdw, message):
    record_id = cfg.current_round['record_id']
    message = format_message(message)
    command = "UPDATE log_records SET tare_log = tare_log || '{}' " \
              "WHERE record = {}".format(message, record_id)
    response = qdw.try_execute(command)
    return response


def format_message(message):
    message = str(message).replace("'", "")
    timestamp = datetime.datetime.now()
    frmt = "DATETIME:{}|MESSAGE:{}\n".format(timestamp, message)
    return frmt


def delete_old_logs(sql_shell):
    """ Удалить логи, старше 30 дней """
    command = "DELETE FROM log_records WHERE init_time < now() - interval '30 days'"
    response = sql_shell.try_execute(command)
    return response


def fix_log_end(sql_shell):
    if cfg.current_round['has_gross']:
        fix_tare_log_end(sql_shell)
    else:
        fix_gross_log_end(sql_shell)


def fix_gross_log_end(sql_shell):
    """ Сделать отметку о конце логгироавния взвешивания брутто """
    msg = 'Конец взвешивания брутто'
    msg = format_message(msg)
    command = "UPDATE log_records SET gross_log = gross_log || '{}' " \
              "WHERE record={}".format(msg, cfg.current_round['record_id'])
    return sql_shell.try_execute(command)


def fix_tare_log_end(sql_shell):
    """ Сделать отметку о конце логгироавния взвешивания тары """
    msg = 'Конец взвешивания брутто'
    msg = format_message(msg)
    command = "UPDATE log_records SET tare_log = tare_log || '{}' " \
              "WHERE record={}".format(msg, cfg.current_round['record_id'])
    return sql_shell.try_execute(command)


def software_start_logging(sql_shell):
    """ Зафиксировать факт старта программы """
    return log_sys_event(sql_shell, 1, 'START', 'Weighting_platform')


def fix_round_fail(sql_shell, error_text):
    """ Зафиксировать провал взвешивания """
    return log_sys_event(sql_shell, 3, error_text, 'Weighting_platform')


def log_sys_event(sql_shell, event_type, log, module):
    """ Функция для логгирования системного события """
    command = "INSERT INTO log_events (event_type, log, datetime, module) " \
              "VALUES ({}, '{}', '{}', '{}')"
    command = command.format(event_type, log, datetime.datetime.now(), module)
    return sql_shell.try_execute(command)


class PhotoSendLogger:
    """
    Логгер для отправки фотографий.
    """

    def log_photo_send(self, sql_shell, record_id, photo_path):
        """
        Функция для логгирования отправки фото.

        :param sql_shell: Объект типа sql_shell для работы с БД.
        :param record_id: ID акта.
        :param photo_path: Путь к фото.
        :return:
        """
        command = "INSERT INTO photo_send_control (record, photo, send_time) " \
                  "VALUES ({}, '{}', '{}')".format(record_id, photo_path,
                                                   datetime.datetime.now())
        response = sql_shell.try_execute(command)
        if response:
            return response['info'][0][0]

    def log_photo_get(self, sql_shell, log_id, wserver_id, wserver_response):
        """
        Логгирования получение фото by wserver.

        :param sql_shell: Объект типа sql_shell для работы с БД.
        :param log_id: ID лога, в котоом уже есть wserver_send событие.
        :param wserver_id: ID wserver.
        :param wserver_response: Ответ wserver
        :return:
        """
        command = "UPDATE photo_send_control SET wserver_id={}, response='{}'," \
                  "get_time='{}' WHERE id={}".format(wserver_id,
                                                     wserver_response,
                                                     datetime.datetime.now(),
                                                     log_id)
        response = sql_shell.try_execute(command)
        return response


class ActSendLogger:
    """ Логгер отправки актов """

    def log_act_send(self, sql_shell, record_id):
        """
        Логгировать факт отправки.

        :param sql_shell: Объект типа sql_shell для работы с БД.
        :param record_id: ID акта.
        :return:
        """
        command = "INSERT INTO acts_send_control (record, send_time) " \
                  "VALUES ({}, '{}')".format(record_id,
                                             datetime.datetime.now())
        response = sql_shell.try_execute(command)
        if response:
            return response['info'][0][0]

    def log_act_get(self, sql_shell, log_id, wserver_id):
        """
        Логгировать факт получения акта by wserver.

        :param sql_shell: Объект типа wsqluse для работы с БД.
        :param log_id: ID лога.
        :param wserver_id: ID wserver.
        :return:
        """
        command = "UPDATE acts_send_control SET wserver_id={}," \
                  "get_time='{}' WHERE id={}".format(wserver_id,
                                                     datetime.datetime.now(),
                                                     log_id)
        response = sql_shell.try_execute(command)
        return response
