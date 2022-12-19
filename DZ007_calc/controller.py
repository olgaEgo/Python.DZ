import model
import view
import logger


def start():
    try:
        num1 = view.first_input()
        if model.not_str(num1):
            try:
                num1 = float(num1)
                oper = view.input_oper()
                num = view.input_num()
                res1 = model.operation(num1, oper, num)
                logger.logg(num1, oper, num, res1)
                oper = view.input_oper()

                while model.result(oper):
                    num = view.input_num()
                    result = model.operation(res1, oper, num)
                    logger.logg(res1, oper, num, result)
                    res1 = result
                    oper = view.input_oper()

                else:
                    view.result_data(res1)
            except ValueError:
                print('Неверный ввод')
        else:
            view.result_data(model.calc_str(num1))
    except ValueError:
        print('Неверный ввод')
