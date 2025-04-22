import 'package:flutter/material.dart';
import 'camera_screen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Durian Leaf Disease Detector',
      theme: ThemeData(primarySwatch: Colors.green),
      home: CameraScreen(),
    );
  }
}
