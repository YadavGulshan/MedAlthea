import 'package:flutter/material.dart';

ThemeData lightTheme = ThemeData.light().copyWith(
  appBarTheme: const AppBarTheme(color: Color(0xFF13B9FF)),
  colorScheme: ColorScheme.fromSwatch(
    accentColor: const Color(0xFF13B9FF),
  ),
);
ThemeData darkTheme = ThemeData.dark().copyWith();
