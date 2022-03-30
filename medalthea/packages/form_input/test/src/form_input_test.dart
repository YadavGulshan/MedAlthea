// ignore_for_file: prefer_const_constructors
import 'package:flutter_test/flutter_test.dart';
import 'package:form_input/form_input.dart';

void main() {
  group('Test Email', () {
    test('Correct Email', () {
      final email = Email.dirty('test@gmail.com');
      expect(email.valid, true);
    });

    test('Wrong email', () {
      final email = Email.dirty('testgmail.com');
      expect(email.valid, false);
    });
  });

  group('Test password', () {
    test('Weak Password', () {
      final password = Password.dirty('123456');
      expect(password.valid, false);
    });

    test('Strong Password', () {
      final password = Password.dirty('thebestPassword@758');
      expect(password.valid, true);
    });
  });

  group('Username is there or not?', () {
    test('If username is empty', () {
      final value = Username.dirty();
      expect(value.valid, false);
    });

    test('If username is not empty', () {
      final value = Username.dirty('test');
      expect(value.valid, true);
    });
  });
}
