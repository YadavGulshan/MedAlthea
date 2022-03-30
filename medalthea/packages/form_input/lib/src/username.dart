import 'package:formz/formz.dart';

/// possible states of username error
enum UsernameValidatonError {
  /// Username is empty
  empty,
}

/// {@template username_formz}
/// A validator for a username.
/// {@endtemplate}
class Username extends FormzInput<String, UsernameValidatonError> {
  /// {@macro username_formz}
  const Username.pure() : super.pure('');

  /// {@macro username_formz}
  const Username.dirty([String value = '']) : super.dirty(value);

  @override
  UsernameValidatonError? validator(String value) {
    return value.isEmpty ? UsernameValidatonError.empty : null;
  }
}
