class CalculatorTests:
    def test_navigate_to_app(self, app):
        app.calculator_menu_button.click()

    def test_check_displayed_names_for_all_web_elements(self, app):
        assert app.legend.text == 'Calculator:'
        assert app.x_label.text == 'X value:'
        assert app.y_label.text == 'Y value:'
        assert app.operation_label.text == 'Operation:'
        assert app.result_label.text == 'Result:'

    def test_check_initial_values(self, app):
        assert app.x_input.value == '0'
        assert app.y_input.value == '0'
        assert app.result.value == '0'
        assert app.operations.selected_value == '+'
        assert app.operations.selected_text == 'X+Y'

    def test_addition(self, app):
        app.x_input.send_keys('10.5')
        app.y_input.send_keys('13')
        assert app.result.value == '23.5'
        app.x_input.send_keys('123e-5')
        app.y_input.send_keys('4.23')
        assert app.result.value == '4.23123'
        app.x_input.send_keys('-23')
        app.y_input.send_keys('30.')
        assert app.result.value == '7'
        app.x_input.send_keys('-45.083')
        app.y_input.send_keys('-12')
        assert app.result.value == '-57.083'

    def test_subtraction(self, app):
        app.operations.select_by_text('X-Y')
        app.x_input.send_keys('104')
        app.y_input.send_keys('24')
        assert app.result.value == '80'
        app.x_input.send_keys('-24')
        app.y_input.send_keys('24.31')
        assert app.result.value == '-48.31'
        app.x_input.send_keys('10,23')
        app.y_input.send_keys('-75')
        assert app.result.value == '85.23'
        app.x_input.send_keys('-3')
        app.y_input.send_keys('-7')
        assert app.result.value == '4'

    def test_multiplication(self, app):
        app.operations.select_by_text('X*Y')
        app.x_input.send_keys('0,25')
        app.y_input.send_keys('0,25')
        assert app.result.value == '0.0625'
        app.x_input.send_keys('1e2')
        app.y_input.send_keys('0.002')
        assert app.result.value == '0.2'
        app.x_input.send_keys('8')
        app.y_input.send_keys('2')
        assert app.result.value == '16'
        app.x_input.send_keys('6')
        app.y_input.send_keys('-2')
        assert app.result.value == '-12'

    def test_deviation(self, app):
        app.operations.select_by_text('X/Y')
        app.x_input.send_keys('-248')
        app.y_input.send_keys('-2')
        assert app.result.value == '124'
        app.x_input.send_keys('02')
        app.y_input.send_keys('2')
        assert app.result.value == '1'
        app.x_input.send_keys('0.5')
        app.y_input.send_keys('2')
        assert app.result.value == '0.25'
        app.x_input.send_keys('2.0')
        app.y_input.send_keys('4.0')
        assert app.result.value == '0.5'

    def test_make_all_operations_for_same_x_y(self, app):
        app.x_input.send_keys('+100')
        app.y_input.send_keys('100')
        app.operations.select_by_text('X+Y')
        assert app.result.value == '200'
        app.operations.select_by_text('X-Y')
        assert app.result.value == '0'
        app.operations.select_by_text('X/Y')
        assert app.result.value == '1'
        app.operations.select_by_text('X*Y')
        assert app.result.value == '10000'

    def test_handling_infinity(self, app):
        app.x_input.send_keys('1e2')
        app.y_input.send_keys('0')
        app.operations.select_by_text('X/Y')
        assert app.result.value == 'Infinity'
        app.y_input.send_keys('1')
        assert app.result.value == '100'
        app.x_input.send_keys('Infinity')
        assert app.result.value == 'Infinity'
        app.operations.select_by_text('X-Y')
        assert app.result.value == 'Infinity'
        app.operations.select_by_text('X+Y')
        assert app.result.value == 'Infinity'
        app.operations.select_by_text('X*Y')
        assert app.result.value == 'Infinity'
        app.y_input.send_keys('0')
        assert app.result.value == 'NaN'
        app.y_input.send_keys('Infinity')
        assert app.result.value == 'Infinity'
        app.x_input.send_keys('-1')
        assert app.result.value == '-Infinity'
        app.operations.select_by_text('X-Y')
        assert app.result.value == '-Infinity'
        app.operations.select_by_text('X+Y')
        assert app.result.value == 'Infinity'
        app.operations.select_by_text('X*Y')
        assert app.result.value == '-Infinity'

    def test_put_forbbiden_sign_to_x_input(self, app):
        app.x_input.send_keys('NaN')
        app.y_input.send_keys('3')
        app.operations.select_by_text('X+Y')
        assert app.x_input.value == 'NaN'
        assert app.result.value == 'NaN'
        app.operations.select_by_text('X-Y')
        assert app.x_input.value == 'NaN'
        assert app.result.value == 'NaN'
        app.operations.select_by_text('X*Y')
        assert app.x_input.value == 'NaN'
        assert app.result.value == 'NaN'
        app.operations.select_by_text('X/Y')
        assert app.x_input.value == 'NaN'
        assert app.result.value == 'NaN'
        app.x_input.send_keys('300')
        assert app.result.value == '100'

    def test_put_forbbiden_sign_to_y_input(self, app):
        app.x_input.send_keys('-0')
        app.y_input.send_keys('&')
        app.operations.select_by_text('X+Y')
        assert app.y_input.value == '&'
        assert app.result.value == 'NaN'
        app.operations.select_by_text('X-Y')
        assert app.y_input.value == '&'
        assert app.result.value == 'NaN'
        app.operations.select_by_text('X*Y')
        assert app.y_input.value == '&'
        assert app.result.value == 'NaN'
        app.operations.select_by_text('X/Y')
        assert app.y_input.value == '&'
        assert app.result.value == 'NaN'
        app.y_input.send_keys('200')
        assert app.result.value == '0'
