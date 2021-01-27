class CalculatorTests:
    def test_check_displayed_names_for_all_web_elements(self, calculator):
        assert calculator.legend.text == 'Kalkulator:'
        assert calculator.x_label.text == 'X value:'
        assert calculator.y_label.text == 'Y value:'
        assert calculator.operation_label.text == 'Operation:'
        assert calculator.result_label.text == 'Result:'

    def test_check_initial_values(self, calculator):
        assert calculator.x_input.value == '0'
        assert calculator.y_input.value == '0'
        assert calculator.result.value == '0'
        assert calculator.operations.selected_value == '+'
        assert calculator.operations.selected_text == 'X+Y'

    def test_addition(self, calculator):
        calculator.x_input.send_keys('10.5')
        calculator.y_input.send_keys('13')
        assert calculator.result.value == '23.5'
        calculator.x_input.send_keys('123e-5')
        calculator.y_input.send_keys('4.23')
        assert calculator.result.value == '4.23123'
        calculator.x_input.send_keys('-23')
        calculator.y_input.send_keys('30.')
        assert calculator.result.value == '7'
        calculator.x_input.send_keys('-45.083')
        calculator.y_input.send_keys('-12')
        assert calculator.result.value == '-57.083'

    def test_subtraction(self, calculator):
        calculator.operations.select_by_text('X-Y')
        calculator.x_input.send_keys('104')
        calculator.y_input.send_keys('24')
        assert calculator.result.value == '80'
        calculator.x_input.send_keys('-24')
        calculator.y_input.send_keys('24.31')
        assert calculator.result.value == '-48.31'
        calculator.x_input.send_keys('10,23')
        calculator.y_input.send_keys('-75')
        assert calculator.result.value == '85.23'
        calculator.x_input.send_keys('-3')
        calculator.y_input.send_keys('-7')
        assert calculator.result.value == '4'

    def test_multiplication(self, calculator):
        calculator.operations.select_by_text('X*Y')
        calculator.x_input.send_keys('0,25')
        calculator.y_input.send_keys('0,25')
        assert calculator.result.value == '0.0625'
        calculator.x_input.send_keys('1e2')
        calculator.y_input.send_keys('0.002')
        assert calculator.result.value == '0.2'
        calculator.x_input.send_keys('8')
        calculator.y_input.send_keys('2')
        assert calculator.result.value == '16'
        calculator.x_input.send_keys('6')
        calculator.y_input.send_keys('-2')
        assert calculator.result.value == '-12'

    def test_deviation(self, calculator):
        calculator.operations.select_by_text('X/Y')
        calculator.x_input.send_keys('-248')
        calculator.y_input.send_keys('-2')
        assert calculator.result.value == '124'
        calculator.x_input.send_keys('02')
        calculator.y_input.send_keys('2')
        assert calculator.result.value == '1'
        calculator.x_input.send_keys('0.5')
        calculator.y_input.send_keys('2')
        assert calculator.result.value == '0.25'
        calculator.x_input.send_keys('2.0')
        calculator.y_input.send_keys('4.0')
        assert calculator.result.value == '0.5'

    def test_make_all_operations_for_same_x_y(self, calculator):
        calculator.x_input.send_keys('+100')
        calculator.y_input.send_keys('100')
        calculator.operations.select_by_text('X+Y')
        assert calculator.result.value == '200'
        calculator.operations.select_by_text('X-Y')
        assert calculator.result.value == '0'
        calculator.operations.select_by_text('X/Y')
        assert calculator.result.value == '1'
        calculator.operations.select_by_text('X*Y')
        assert calculator.result.value == '10000'

    def test_handling_infinity(self, calculator):
        calculator.x_input.send_keys('1e2')
        calculator.y_input.send_keys('0')
        calculator.operations.select_by_text('X/Y')
        assert calculator.result.value == 'Infinity'
        calculator.y_input.send_keys('1')
        assert calculator.result.value == '100'
        calculator.x_input.send_keys('Infinity')
        assert calculator.result.value == 'Infinity'
        calculator.operations.select_by_text('X-Y')
        assert calculator.result.value == 'Infinity'
        calculator.operations.select_by_text('X+Y')
        assert calculator.result.value == 'Infinity'
        calculator.operations.select_by_text('X*Y')
        assert calculator.result.value == 'Infinity'
        calculator.y_input.send_keys('0')
        assert calculator.result.value == 'NaN'
        calculator.y_input.send_keys('Infinity')
        assert calculator.result.value == 'Infinity'
        calculator.x_input.send_keys('-1')
        assert calculator.result.value == '-Infinity'
        calculator.operations.select_by_text('X-Y')
        assert calculator.result.value == '-Infinity'
        calculator.operations.select_by_text('X+Y')
        assert calculator.result.value == 'Infinity'
        calculator.operations.select_by_text('X*Y')
        assert calculator.result.value == '-Infinity'


    def test_put_forbbiden_sign_to_x_input(self, calculator):
        calculator.x_input.send_keys('NaN')
        calculator.y_input.send_keys('3')
        calculator.operations.select_by_text('X+Y')
        assert calculator.x_input.value == 'NaN'
        assert calculator.result.value == 'NaN'
        calculator.operations.select_by_text('X-Y')
        assert calculator.x_input.value == 'NaN'
        assert calculator.result.value == 'NaN'
        calculator.operations.select_by_text('X*Y')
        assert calculator.x_input.value == 'NaN'
        assert calculator.result.value == 'NaN'
        calculator.operations.select_by_text('X/Y')
        assert calculator.x_input.value == 'NaN'
        assert calculator.result.value == 'NaN'
        calculator.x_input.send_keys('300')
        assert calculator.result.value == '100'

    def test_put_forbbiden_sign_to_y_input(self, calculator):
        calculator.x_input.send_keys('-0')
        calculator.y_input.send_keys('&')
        calculator.operations.select_by_text('X+Y')
        assert calculator.y_input.value == '&'
        assert calculator.result.value == 'NaN'
        calculator.operations.select_by_text('X-Y')
        assert calculator.y_input.value == '&'
        assert calculator.result.value == 'NaN'
        calculator.operations.select_by_text('X*Y')
        assert calculator.y_input.value == '&'
        assert calculator.result.value == 'NaN'
        calculator.operations.select_by_text('X/Y')
        assert calculator.y_input.value == '&'
        assert calculator.result.value == 'NaN'
        calculator.y_input.send_keys('200')
        assert calculator.result.value == '0'
