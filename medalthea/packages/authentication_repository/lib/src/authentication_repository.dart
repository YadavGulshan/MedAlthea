import 'dart:async';

import 'package:shared_preferences/shared_preferences.dart';

/// Enum that has different states of authentication
enum AuthenticationStatus {
  /// User is unkown
  unknown,

  /// User is authenticated
  authenticated,

  /// User is not authenticated
  unauthenticated,
}

/// A class that holds the authentication status of the user.
class AuthenticationRepository {
  final _controller = StreamController<AuthenticationStatus>();

  /// The current authentication status.
  Stream<AuthenticationStatus> get status async* {
    await Future<void>.delayed(const Duration(seconds: 1));
    await initAction();
    yield* _controller.stream;
  }

  /// Changes the authentication status to authenticated.
  /// if credentials are correct.
  Future<void> logIn({
    required String username,
    required String password,
  }) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('isLogged', 'true');
    await Future.delayed(
      const Duration(milliseconds: 300),
      () => _controller.add(AuthenticationStatus.authenticated),
    );
  }

  /// Creates a new user.
  ///
  /// Why Confirm Password? We're doing all the checks in frontent too right?
  /// Yes we are.
  ///
  /// But we're passing both password and confirm password to the backend.
  /// So that if any bug exists,
  /// backend won't create any account and will pass error to us
  Future<void> register({
    required String username,
    required String email,
    required String firstName,
    required String lastName,
    required String password,
    required String confirmPassword,
  }) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('isLogged', 'true');
    await Future.delayed(
      const Duration(milliseconds: 300),
      () => _controller.add(AuthenticationStatus.authenticated),
    );
  }

  /// Changes the authentication status to unauthenticated.
  Future<void> logOut() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('isLogged', 'false');
    _controller.add(AuthenticationStatus.unauthenticated);
  }

  /// Checks if the user is authenticated.
  Future<void> initAction() async {
    // Check the shared preferences for the user's credentials
    // and set the authentication status accordingly.
    final prefs = await SharedPreferences.getInstance();
    if (prefs.getString('isLogged') == 'true') {
      _controller.add(AuthenticationStatus.authenticated);
    } else {
      _controller.add(AuthenticationStatus.unauthenticated);
    }
  }

  /// Closes the stream.
  void dispose() => _controller.close();
}
